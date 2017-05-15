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

/* Satus messages. */

int SendStatusRequest(int sock,
                              ObjectID object_ids[],
                              int64_t num_objects);

int64_t ReadStatusRequest_num_objects(uint8_t *data);

void ReadStatusRequest(uint8_t *data,
                               ObjectID object_ids[],
                               int64_t num_objects);

int SendStatusReply(int sock,
                            ObjectID object_ids[],
                            int object_status[],
                            int64_t num_objects);

int64_t ReadStatusReply_num_objects(uint8_t *data);

void ReadStatusReply(uint8_t *data,
                             ObjectID object_ids[],
                             int object_status[],
                             int64_t num_objects);

/* Plasma Constains message functions. */

int SendContainsRequest(int sock, ObjectID object_id);

void ReadContainsRequest(uint8_t *data, ObjectID *object_id);

int SendContainsReply(int sock, ObjectID object_id, int has_object);

void ReadContainsReply(uint8_t *data, ObjectID *object_id, int *has_object);

/* Plasma Connect message functions. */

int SendConnectRequest(int sock);

void ReadConnectRequest(uint8_t *data);

int SendConnectReply(int sock, int64_t memory_capacity);

void ReadConnectReply(uint8_t *data, int64_t *memory_capacity);

/* Plasma Evict message functions (no reply so far). */

int SendEvictRequest(int sock, int64_t num_bytes);

void ReadEvictRequest(uint8_t *data, int64_t *num_bytes);

int SendEvictReply(int sock, int64_t num_bytes);

void ReadEvictReply(uint8_t *data, int64_t *num_bytes);

/* Plasma Fetch Remote message functions. */

int SendFetchRequest(int sock,
                             ObjectID object_ids[],
                             int64_t num_objects);

int64_t ReadFetchRequest_num_objects(uint8_t *data);

void ReadFetchRequest(uint8_t *data,
                              ObjectID object_ids[],
                              int64_t num_objects);

/* Plasma Wait message functions. */

int SendWaitRequest(int sock,
                            ObjectRequest object_requests[],
                            int num_requests,
                            int num_ready_objects,
                            int64_t timeout_ms);

int ReadWaitRequest_num_object_ids(uint8_t *data);

void ReadWaitRequest(uint8_t *data,
                             ObjectRequestMap &object_requests,
                             int num_object_ids,
                             int64_t *timeout_ms,
                             int *num_ready_objects);

int SendWaitReply(int sock,
                          const ObjectRequestMap &object_requests,
                          int num_ready_objects);

void ReadWaitReply(uint8_t *data,
                           ObjectRequest object_requests[],
                           int *num_ready_objects);

/* Plasma Subscribe message functions. */

int SendSubscribeRequest(int sock);

/* Data messages. */

int SendDataRequest(int sock,
                    ObjectID object_id,
                    const char *address,
                    int port);

void ReadDataRequest(uint8_t *data,
                     ObjectID *object_id,
                     char **address,
                     int *port);

int SendDataReply(int sock,
                  ObjectID object_id,
                  int64_t object_size,
                  int64_t metadata_size);

void ReadDataReply(uint8_t *data,
                   ObjectID *object_id,
                   int64_t *object_size,
                   int64_t *metadata_size);

#endif /* PLASMA_PROTOCOL */
