#include "flatbuffers/flatbuffers.h"
#include "format/plasma_generated.h"

#include "plasma_protocol.h"

#include "plasma_io.h"

#define FLATBUFFER_BUILDER_DEFAULT_SIZE 1024

flatbuffers::Offset<
    flatbuffers::Vector<flatbuffers::Offset<flatbuffers::String>>>
to_flatbuf(flatbuffers::FlatBufferBuilder &fbb,
           ObjectID object_ids[],
           int64_t num_objects) {
  std::vector<flatbuffers::Offset<flatbuffers::String>> results;
  for (size_t i = 0; i < num_objects; i++) {
    results.push_back(fbb.CreateString(object_ids[i].binary()));
  }
  return fbb.CreateVector(results);
}

void plasma_receive(int sock, int64_t message_type, std::vector<uint8_t> &buffer) {
  int64_t type;
  read_message(sock, &type, buffer);
  ARROW_CHECK(type == message_type) << "type = " << type << ", message_type = " << message_type;
}

/* Create messages. */

int plasma_send_CreateRequest(int sock,
                              ObjectID object_id,
                              int64_t data_size,
                              int64_t metadata_size) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaCreateRequest(fbb, fbb.CreateString(object_id.binary()),
                                           data_size, metadata_size);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaCreateRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_CreateRequest(uint8_t *data,
                               ObjectID *object_id,
                               int64_t *data_size,
                               int64_t *metadata_size) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaCreateRequest>(data);
  *data_size = message->data_size();
  *metadata_size = message->metadata_size();
  *object_id = ObjectID::from_binary(message->object_id()->str());
}

int plasma_send_CreateReply(int sock,
                            ObjectID object_id,
                            PlasmaObject *object,
                            int error_code) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  PlasmaObjectSpec plasma_object(
      object->handle.store_fd, object->handle.mmap_size, object->data_offset,
      object->data_size, object->metadata_offset, object->metadata_size);
  auto message =
      CreatePlasmaCreateReply(fbb, fbb.CreateString(object_id.binary()),
                              &plasma_object, (PlasmaError) error_code);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaCreateReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_CreateReply(uint8_t *data,
                             ObjectID *object_id,
                             PlasmaObject *object,
                             int *error_code) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaCreateReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  object->handle.store_fd = message->plasma_object()->segment_index();
  object->handle.mmap_size = message->plasma_object()->mmap_size();
  object->data_offset = message->plasma_object()->data_offset();
  object->data_size = message->plasma_object()->data_size();
  object->metadata_offset = message->plasma_object()->metadata_offset();
  object->metadata_size = message->plasma_object()->metadata_size();
  *error_code = message->error();
}

/* Seal messages. */

int plasma_send_SealRequest(int sock,
                            ObjectID object_id,
                            unsigned char *digest) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto digest_string = fbb.CreateString((char *) digest, kDigestSize);
  auto message =
      CreatePlasmaSealRequest(fbb, fbb.CreateString(object_id.binary()), digest_string);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaSealRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_SealRequest(uint8_t *data,
                             ObjectID *object_id,
                             unsigned char *digest) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaSealRequest>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  ARROW_CHECK(message->digest()->size() == kDigestSize);
  memcpy(digest, message->digest()->data(), kDigestSize);
}

int plasma_send_SealReply(int sock,
                          ObjectID object_id,
                          int error) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaSealReply(fbb, fbb.CreateString(object_id.binary()),
                                       (PlasmaError) error);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaSealReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_SealReply(uint8_t *data, ObjectID *object_id, int *error) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaSealReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  *error = message->error();
}

/* Release messages. */

int plasma_send_ReleaseRequest(int sock,
                               ObjectID object_id) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaSealRequest(fbb, fbb.CreateString(object_id.binary()));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaReleaseRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_ReleaseRequest(uint8_t *data, ObjectID *object_id) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaReleaseRequest>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
}

int plasma_send_ReleaseReply(int sock,
                             ObjectID object_id,
                             int error) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaReleaseReply(fbb, fbb.CreateString(object_id.binary()),
                                          (PlasmaError) error);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaReleaseReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_ReleaseReply(uint8_t *data, ObjectID *object_id, int *error) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaReleaseReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  *error = message->error();
}

/* Delete messages. */

int plasma_send_DeleteRequest(int sock,
                              ObjectID object_id) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaDeleteRequest(fbb, fbb.CreateString(object_id.binary()));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaDeleteRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_DeleteRequest(uint8_t *data, ObjectID *object_id) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaReleaseReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
}

int plasma_send_DeleteReply(int sock,
                            ObjectID object_id,
                            int error) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaDeleteReply(fbb, fbb.CreateString(object_id.binary()),
                                         (PlasmaError) error);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaDeleteReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_DeleteReply(uint8_t *data, ObjectID *object_id, int *error) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaDeleteReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  *error = message->error();
}

/* Satus messages. */

int plasma_send_StatusRequest(int sock,
                              ObjectID object_ids[],
                              int64_t num_objects) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message =
      CreatePlasmaStatusRequest(fbb, to_flatbuf(fbb, object_ids, num_objects));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaStatusRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

int64_t plasma_read_StatusRequest_num_objects(uint8_t *data) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaStatusRequest>(data);
  return message->object_ids()->size();
}

void plasma_read_StatusRequest(uint8_t *data,
                               ObjectID object_ids[],
                               int64_t num_objects) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaStatusRequest>(data);
  for (int64_t i = 0; i < num_objects; ++i) {
    object_ids[i] = ObjectID::from_binary(message->object_ids()->Get(i)->str());
  }
}

int plasma_send_StatusReply(int sock,
                            ObjectID object_ids[],
                            int object_status[],
                            int64_t num_objects) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message =
      CreatePlasmaStatusReply(fbb, to_flatbuf(fbb, object_ids, num_objects),
                              fbb.CreateVector(object_status, num_objects));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaStatusReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

int64_t plasma_read_StatusReply_num_objects(uint8_t *data) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaStatusReply>(data);
  return message->object_ids()->size();
}

void plasma_read_StatusReply(uint8_t *data,
                             ObjectID object_ids[],
                             int object_status[],
                             int64_t num_objects) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaStatusReply>(data);
  for (int64_t i = 0; i < num_objects; ++i) {
    object_ids[i] = ObjectID::from_binary(message->object_ids()->Get(i)->str());
  }
  for (int64_t i = 0; i < num_objects; ++i) {
    object_status[i] = message->status()->data()[i];
  }
}

/* Contains messages. */

int plasma_send_ContainsRequest(int sock,
                                ObjectID object_id) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaContainsRequest(fbb, fbb.CreateString(object_id.binary()));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaContainsRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_ContainsRequest(uint8_t *data, ObjectID *object_id) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaContainsRequest>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
}

int plasma_send_ContainsReply(int sock,
                              ObjectID object_id,
                              int has_object) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message =
      CreatePlasmaContainsReply(fbb, fbb.CreateString(object_id.binary()), has_object);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaContainsReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_ContainsReply(uint8_t *data,
                               ObjectID *object_id,
                               int *has_object) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaContainsReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  *has_object = message->has_object();
}

/* Connect messages. */

int plasma_send_ConnectRequest(int sock) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaConnectRequest(fbb);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaConnectRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_ConnectRequest(uint8_t *data) {}

int plasma_send_ConnectReply(int sock,
                             int64_t memory_capacity) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaConnectReply(fbb, memory_capacity);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaConnectReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_ConnectReply(uint8_t *data, int64_t *memory_capacity) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaConnectReply>(data);
  *memory_capacity = message->memory_capacity();
}

/* Evict messages. */

int plasma_send_EvictRequest(int sock, int64_t num_bytes) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaEvictRequest(fbb, num_bytes);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaEvictRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_EvictRequest(uint8_t *data, int64_t *num_bytes) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaEvictRequest>(data);
  *num_bytes = message->num_bytes();
}

int plasma_send_EvictReply(int sock, int64_t num_bytes) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaEvictReply(fbb, num_bytes);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaEvictReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_EvictReply(uint8_t *data, int64_t *num_bytes) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaEvictReply>(data);
  *num_bytes = message->num_bytes();
}

/* Get messages. */

int plasma_send_GetRequest(int sock,
                           ObjectID object_ids[],
                           int64_t num_objects,
                           int64_t timeout_ms) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaGetRequest(
      fbb, to_flatbuf(fbb, object_ids, num_objects), timeout_ms);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaGetRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_GetRequest(uint8_t *data,
                            std::vector<ObjectID>& object_ids,
                            int64_t *timeout_ms) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaGetRequest>(data);
  for (int64_t i = 0; i < message->object_ids()->size(); ++i) {
    auto object_id = message->object_ids()->Get(i)->str();
    object_ids.push_back(ObjectID::from_binary(object_id));
  }
  *timeout_ms = message->timeout_ms();
}

int plasma_send_GetReply(
    int sock,
    ObjectID object_ids[],
    std::unordered_map<ObjectID, PlasmaObject, UniqueIDHasher> &plasma_objects,
    int64_t num_objects) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  std::vector<PlasmaObjectSpec> objects;

  for (int i = 0; i < num_objects; ++i) {
    const PlasmaObject &object = plasma_objects[object_ids[i]];
    objects.push_back(PlasmaObjectSpec(
        object.handle.store_fd, object.handle.mmap_size, object.data_offset,
        object.data_size, object.metadata_offset, object.metadata_size));
  }
  auto message = CreatePlasmaGetReply(
      fbb, to_flatbuf(fbb, object_ids, num_objects),
      fbb.CreateVectorOfStructs(objects.data(), num_objects));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaGetReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_GetReply(uint8_t *data,
                          ObjectID object_ids[],
                          PlasmaObject plasma_objects[],
                          int64_t num_objects) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaGetReply>(data);
  for (int64_t i = 0; i < num_objects; ++i) {
    object_ids[i] = ObjectID::from_binary(message->object_ids()->Get(i)->str());
  }
  for (int64_t i = 0; i < num_objects; ++i) {
    const PlasmaObjectSpec *object = message->plasma_objects()->Get(i);
    plasma_objects[i].handle.store_fd = object->segment_index();
    plasma_objects[i].handle.mmap_size = object->mmap_size();
    plasma_objects[i].data_offset = object->data_offset();
    plasma_objects[i].data_size = object->data_size();
    plasma_objects[i].metadata_offset = object->metadata_offset();
    plasma_objects[i].metadata_size = object->metadata_size();
  }
}

/* Fetch messages. */

int plasma_send_FetchRequest(int sock,
                             ObjectID object_ids[],
                             int64_t num_objects) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message =
      CreatePlasmaFetchRequest(fbb, to_flatbuf(fbb, object_ids, num_objects));
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaFetchRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

int64_t plasma_read_FetchRequest_num_objects(uint8_t *data) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaFetchRequest>(data);
  return message->object_ids()->size();
}

void plasma_read_FetchRequest(uint8_t *data,
                              ObjectID object_ids[],
                              int64_t num_objects) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaFetchRequest>(data);
  for (int64_t i = 0; i < num_objects; ++i) {
    object_ids[i] = ObjectID::from_binary(message->object_ids()->Get(i)->str());
  }
}

/* Wait messages. */

int plasma_send_WaitRequest(int sock,
                            ObjectRequest object_requests[],
                            int num_requests,
                            int num_ready_objects,
                            int64_t timeout_ms) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);

  std::vector<flatbuffers::Offset<ObjectRequestSpec>> object_request_specs;
  for (int i = 0; i < num_requests; i++) {
    object_request_specs.push_back(CreateObjectRequestSpec(
        fbb, fbb.CreateString(object_requests[i].object_id.binary()),
        object_requests[i].type));
  }

  auto message =
      CreatePlasmaWaitRequest(fbb, fbb.CreateVector(object_request_specs),
                              num_ready_objects, timeout_ms);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaWaitRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

int plasma_read_WaitRequest_num_object_ids(uint8_t *data) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaWaitRequest>(data);
  return message->object_requests()->size();
}

void plasma_read_WaitRequest(uint8_t *data,
                             ObjectRequestMap &object_requests,
                             int num_object_ids,
                             int64_t *timeout_ms,
                             int *num_ready_objects) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaWaitRequest>(data);
  *num_ready_objects = message->num_ready_objects();
  *timeout_ms = message->timeout();

  ARROW_CHECK(num_object_ids == message->object_requests()->size());
  for (int i = 0; i < num_object_ids; i++) {
    ObjectID object_id =
        ObjectID::from_binary(message->object_requests()->Get(i)->object_id()->str());
    ObjectRequest object_request({object_id,
                                  message->object_requests()->Get(i)->type(),
                                  ObjectStatus_Nonexistent});
    object_requests[object_id] = object_request;
  }
}

int plasma_send_WaitReply(int sock,
                          const ObjectRequestMap &object_requests,
                          int num_ready_objects) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);

  std::vector<flatbuffers::Offset<ObjectReply>> object_replies;
  for (const auto &entry : object_requests) {
    const auto &object_request = entry.second;
    object_replies.push_back(CreateObjectReply(
        fbb, fbb.CreateString(object_request.object_id.binary()), object_request.status));
  }

  auto message = CreatePlasmaWaitReply(
      fbb, fbb.CreateVector(object_replies.data(), num_ready_objects),
      num_ready_objects);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaWaitReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_WaitReply(uint8_t *data,
                           ObjectRequest object_requests[],
                           int *num_ready_objects) {
  DCHECK(data);

  auto message = flatbuffers::GetRoot<PlasmaWaitReply>(data);
  *num_ready_objects = message->num_ready_objects();
  for (int i = 0; i < *num_ready_objects; i++) {
    object_requests[i].object_id =
        ObjectID::from_binary(message->object_requests()->Get(i)->object_id()->str());
    object_requests[i].status = message->object_requests()->Get(i)->status();
  }
}

/* Subscribe messages. */

int plasma_send_SubscribeRequest(int sock) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaSubscribeRequest(fbb);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaSubscribeRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

/* Data messages. */

int plasma_send_DataRequest(int sock,
                            ObjectID object_id,
                            const char *address,
                            int port) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto addr = fbb.CreateString((char *) address, strlen(address));
  auto message =
      CreatePlasmaDataRequest(fbb, fbb.CreateString(object_id.binary()), addr, port);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaDataRequest, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_DataRequest(uint8_t *data,
                             ObjectID *object_id,
                             char **address,
                             int *port) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaDataRequest>(data);
  DCHECK(message->object_id()->size() == sizeof(object_id->id));
  *object_id = ObjectID::from_binary(message->object_id()->str());
  *address = strdup(message->address()->c_str());
  *port = message->port();
}

int plasma_send_DataReply(int sock,
                          ObjectID object_id,
                          int64_t object_size,
                          int64_t metadata_size) {
  flatbuffers::FlatBufferBuilder fbb(FLATBUFFER_BUILDER_DEFAULT_SIZE);
  auto message = CreatePlasmaDataReply(fbb, fbb.CreateString(object_id.binary()),
                                       object_size, metadata_size);
  fbb.Finish(message);
  return write_message(sock, MessageType_PlasmaDataReply, fbb.GetSize(),
                       fbb.GetBufferPointer());
}

void plasma_read_DataReply(uint8_t *data,
                           ObjectID *object_id,
                           int64_t *object_size,
                           int64_t *metadata_size) {
  DCHECK(data);
  auto message = flatbuffers::GetRoot<PlasmaDataReply>(data);
  *object_id = ObjectID::from_binary(message->object_id()->str());
  *object_size = (int64_t) message->object_size();
  *metadata_size = (int64_t) message->metadata_size();
}
