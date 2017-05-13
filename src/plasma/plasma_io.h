#include <inttypes.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/un.h>

#include <vector>

#define RAY_PROTOCOL_VERSION 0x0000000000000000
#define DISCONNECT_CLIENT 0

int write_bytes(int fd, uint8_t *cursor, size_t length);

int write_message(int fd, int64_t type, int64_t length, uint8_t *bytes);

int read_bytes(int fd, uint8_t *cursor, size_t length);

int64_t read_message(int fd, int64_t *type, std::vector<uint8_t> &buffer);

int bind_ipc_sock(const char *socket_pathname, bool shall_listen);

int accept_client(int socket_fd);
