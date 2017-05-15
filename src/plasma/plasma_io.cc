#include "status.h"
#include "plasma_io.h"
#include "plasma_common.h"

int write_bytes(int fd, uint8_t *cursor, size_t length) {
  ssize_t nbytes = 0;
  size_t bytesleft = length;
  size_t offset = 0;
  while (bytesleft > 0) {
    /* While we haven't written the whole message, write to the file
     * descriptor, advance the cursor, and decrease the amount left to write. */
    nbytes = write(fd, cursor + offset, bytesleft);
    if (nbytes < 0) {
      if (errno == EAGAIN || errno == EWOULDBLOCK || errno == EINTR) {
        continue;
      }
      return -1; /* Errno will be set. */
    } else if (0 == nbytes) {
      /* Encountered early EOF. */
      return -1;
    }
    ARROW_CHECK(nbytes > 0);
    bytesleft -= nbytes;
    offset += nbytes;
  }

  return 0;
}

int write_message(int fd, int64_t type, int64_t length, uint8_t *bytes) {
  int64_t version = RAY_PROTOCOL_VERSION;
  int closed;
  closed = write_bytes(fd, reinterpret_cast<uint8_t *>(&version), sizeof(version));
  if (closed) {
    return closed;
  }
  closed = write_bytes(fd, reinterpret_cast<uint8_t *>(&type), sizeof(type));
  if (closed) {
    return closed;
  }
  closed = write_bytes(fd, reinterpret_cast<uint8_t *>(&length), sizeof(length));
  if (closed) {
    return closed;
  }
  closed = write_bytes(fd, bytes, length * sizeof(char));
  if (closed) {
    return closed;
  }
  return 0;
}

int read_bytes(int fd, uint8_t *cursor, size_t length) {
  ssize_t nbytes = 0;
  /* Termination condition: EOF or read 'length' bytes total. */
  size_t bytesleft = length;
  size_t offset = 0;
  while (bytesleft > 0) {
    nbytes = read(fd, cursor + offset, bytesleft);
    if (nbytes < 0) {
      if (errno == EAGAIN || errno == EWOULDBLOCK || errno == EINTR) {
        continue;
      }
      return -1; /* Errno will be set. */
    } else if (0 == nbytes) {
      /* Encountered early EOF. */
      return -1;
    }
    ARROW_CHECK(nbytes > 0);
    bytesleft -= nbytes;
    offset += nbytes;
  }

  return 0;
}

int64_t read_message(int fd, int64_t *type, std::vector<uint8_t> &buffer) {
  int64_t version;
  int closed = read_bytes(fd, reinterpret_cast<uint8_t *>(&version), sizeof(version));
  if (closed) {
    goto disconnected;
  }
  ARROW_CHECK(version == RAY_PROTOCOL_VERSION);
  int64_t length;
  closed = read_bytes(fd, reinterpret_cast<uint8_t *>(type), sizeof(*type));
  if (closed) {
    goto disconnected;
  }
  closed = read_bytes(fd, reinterpret_cast<uint8_t *>(&length), sizeof(length));
  if (closed) {
    goto disconnected;
  }
  if (length > buffer.size()) {
    buffer.resize(length);
  }
  closed = read_bytes(fd, buffer.data(), length);
  if (closed) {
    goto disconnected;
  }
  return length;
disconnected:
  /* Handle the case in which the socket is closed. */
  *type = DISCONNECT_CLIENT;
  return 0;
}

int bind_ipc_sock(const char *socket_pathname, bool shall_listen) {
  struct sockaddr_un socket_address;
  int socket_fd = socket(AF_UNIX, SOCK_STREAM, 0);
  if (socket_fd < 0) {
    ARROW_LOG(ERROR) << "socket() failed for pathname " << socket_pathname;
    return -1;
  }
  /* Tell the system to allow the port to be reused. */
  int on = 1;
  if (setsockopt(socket_fd, SOL_SOCKET, SO_REUSEADDR, (char *) &on,
                 sizeof(on)) < 0) {
    ARROW_LOG(ERROR) << "setsockopt failed for pathname " << socket_pathname;
    close(socket_fd);
    return -1;
  }

  unlink(socket_pathname);
  memset(&socket_address, 0, sizeof(socket_address));
  socket_address.sun_family = AF_UNIX;
  if (strlen(socket_pathname) + 1 > sizeof(socket_address.sun_path)) {
    ARROW_LOG(ERROR) << "Socket pathname is too long.";
    close(socket_fd);
    return -1;
  }
  strncpy(socket_address.sun_path, socket_pathname,
          strlen(socket_pathname) + 1);

  if (bind(socket_fd, (struct sockaddr *) &socket_address,
           sizeof(socket_address)) != 0) {
    ARROW_LOG(ERROR) << "Bind failed for pathname " << socket_pathname;
    close(socket_fd);
    return -1;
  }
  if (shall_listen && listen(socket_fd, 5) == -1) {
    ARROW_LOG(ERROR) << "Could not listen to socket " << socket_pathname;
    close(socket_fd);
    return -1;
  }
  return socket_fd;
}

int accept_client(int socket_fd) {
  int client_fd = accept(socket_fd, NULL, NULL);
  if (client_fd < 0) {
    ARROW_LOG(ERROR) << "Error reading from socket.";
    return -1;
  }
  return client_fd;
}
