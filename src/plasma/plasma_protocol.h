#ifndef PLASMA_PROTOCOL_H
#define PLASMA_PROTOCOL_H

#include "format/plasma_generated.h"

#include "plasma.h"

/* Plasma receive message. */

void plasma_receive(int sock, int64_t message_type, std::vector<uint8_t>& buffer);

/* Plasma Create message functions. */

int SendCreateRequest(int sock,
                      ObjectID object_id,
                      int64_t data_size,
                      int64_t metadata_size);

void ReadCreateRequest(uint8_t *data,
                       ObjectID *object_id,
                       int64_t *data_size,
                       int64_t *metadata_size);

int SendCreateReply(int sock,
                    ObjectID object_id,
                    PlasmaObject *object,
                    int error);

void ReadCreateReply(uint8_t *data,
                     ObjectID *object_id,
                     PlasmaObject *object,
                     int *error);

/* Plasma Seal message functions. */

int SendSealRequest(int sock, ObjectID object_id, unsigned char *digest);

void ReadSealRequest(uint8_t *data, ObjectID *object_id, unsigned char *digest);

int SendSealReply(int sock, ObjectID object_id, int error);

void ReadSealReply(uint8_t *data, ObjectID *object_id, int *error);

/* Plasma Get message functions. */

int SendGetRequest(int sock,
                   ObjectID object_ids[],
                   int64_t num_objects,
                   int64_t timeout_ms);

void ReadGetRequest(uint8_t *data,
                    std::vector<ObjectID>& object_ids,
                    int64_t *timeout_ms);

int SendGetReply(
    int sock,
    ObjectID object_ids[],
    std::unordered_map<ObjectID, PlasmaObject, UniqueIDHasher> &plasma_objects,
    int64_t num_objects);

void ReadGetReply(uint8_t *data,
                  ObjectID object_ids[],
                  PlasmaObject plasma_objects[],
                  int64_t num_objects);

/* Plasma Release message functions. */

int SendReleaseRequest(int sock, ObjectID object_id);

void ReadReleaseRequest(uint8_t *data, ObjectID *object_id);

int SendReleaseReply(int sock, ObjectID object_id, int error);

void ReadReleaseReply(uint8_t *data, ObjectID *object_id, int *error);

/* Plasma Delete message functions. */

int SendDeleteRequest(int sock, ObjectID object_id);

void ReadDeleteRequest(uint8_t *data, ObjectID *object_id);

int SendDeleteReply(int sock, ObjectID object_id, int error);

void ReadDeleteReply(uint8_t *data, ObjectID *object_id, int *error);

/* Plasma Constains message functions. */

int plasma_send_ContainsRequest(int sock, ObjectID object_id);

void plasma_read_ContainsRequest(uint8_t *data, ObjectID *object_id);

int plasma_send_ContainsReply(int sock,
                              ObjectID object_id,
                              int has_object);

void plasma_read_ContainsReply(uint8_t *data,
                               ObjectID *object_id,
                               int *has_object);

/* Plasma Connect message functions. */

int plasma_send_ConnectRequest(int sock);

void plasma_read_ConnectRequest(uint8_t *data);

int plasma_send_ConnectReply(int sock, int64_t memory_capacity);

void plasma_read_ConnectReply(uint8_t *data, int64_t *memory_capacity);

/* Plasma Evict message functions (no reply so far). */

int plasma_send_EvictRequest(int sock, int64_t num_bytes);

void plasma_read_EvictRequest(uint8_t *data, int64_t *num_bytes);

int plasma_send_EvictReply(int sock, int64_t num_bytes);

void plasma_read_EvictReply(uint8_t *data, int64_t *num_bytes);

/* Plasma Fetch Remote message functions. */

int plasma_send_FetchRequest(int sock,
                             ObjectID object_ids[],
                             int64_t num_objects);

int64_t plasma_read_FetchRequest_num_objects(uint8_t *data);

void plasma_read_FetchRequest(uint8_t *data,
                              ObjectID object_ids[],
                              int64_t num_objects);

/* Plasma Wait message functions. */

int plasma_send_WaitRequest(int sock,
                            ObjectRequest object_requests[],
                            int num_requests,
                            int num_ready_objects,
                            int64_t timeout_ms);

int plasma_read_WaitRequest_num_object_ids(uint8_t *data);

void plasma_read_WaitRequest(uint8_t *data,
                             ObjectRequestMap &object_requests,
                             int num_object_ids,
                             int64_t *timeout_ms,
                             int *num_ready_objects);

int plasma_send_WaitReply(int sock,
                          const ObjectRequestMap &object_requests,
                          int num_ready_objects);

void plasma_read_WaitReply(uint8_t *data,
                           ObjectRequest object_requests[],
                           int *num_ready_objects);

/* Plasma Subscribe message functions. */

int plasma_send_SubscribeRequest(int sock);

#endif /* PLASMA_PROTOCOL */
