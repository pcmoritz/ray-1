#ifndef RAY_GCS_REDIS_CONTEXT_H
#define RAY_GCS_REDIS_CONTEXT_H

#include <functional>
#include <memory>
#include <unordered_map>

#include "absl/strings/str_cat.h"
#include "absl/strings/str_join.h"

#include "ray/id.h"
#include "ray/status.h"
#include "ray/util/logging.h"

#include "ray/gcs/format/gcs_generated.h"

struct redisContext;
struct redisAsyncContext;
struct aeEventLoop;

namespace ray {

namespace gcs {
/// Every callback should take in a vector of the results from the Redis
/// operation and return a bool indicating whether the callback should be
/// deleted once called.
using RedisCallback = std::function<bool(const std::string &)>;

class RedisCallbackManager {
 public:
  static RedisCallbackManager &instance() {
    static RedisCallbackManager instance;
    return instance;
  }

  int64_t add(const RedisCallback &function);

  RedisCallback &get(int64_t callback_index);

  /// Remove a callback.
  void remove(int64_t callback_index);

 private:
  RedisCallbackManager() : num_callbacks_(0){};

  ~RedisCallbackManager() {}

  int64_t num_callbacks_ = 0;
  std::unordered_map<int64_t, RedisCallback> callbacks_;
};

class RedisCommandBuilder {
 public:
  void StartCommand(int size) {
    command_.clear();
    command_.reserve(1000);
    absl::StrAppend(&command_, "*", size, "\r\n");
  }
  void AppendString(const absl::string_view &str) {
    absl::StrAppend(&command_, "$", str.length(), "\r\n", str, "\r\n");
  }
  void BuildCommand(const std::string &command, const UniqueID &id,
                    const uint8_t *data, int64_t length,
                    const TablePrefix prefix, const TablePubsub pubsub_channel,
                    int log_length) {
    std::string prefix_str = absl::StrCat(static_cast<int>(prefix));
    std::string pubsub_str = absl::StrCat(static_cast<int>(pubsub_channel));
    if (length <= 0) {
      StartCommand(4);
    } else {
      if (log_length < 0) {
        StartCommand(5);
      } else {
        StartCommand(6);
      }
    }
    AppendString(command);
    AppendString(prefix_str);
    AppendString(pubsub_str);
    absl::StrAppend(&command_, "$20\r\n");
    command_.append(reinterpret_cast<const char *>(id.data()), id.size());
    if (length > 0) {
      absl::StrAppend(&command_, "\r\n$", length, "\r\n");
      command_.append(reinterpret_cast<const char *>(data), length);
    }
    if (log_length >= 0) {
      std::string s = absl::StrCat(log_length);
      absl::StrAppend(&command_, "\r\n$", s.size(), "\r\n", s);
    }
    absl::StrAppend(&command_, "\r\n");
  }
  const std::string& command() {
    return command_;
  }
 private:
  std::string command_;
};

class RedisContext {
 public:
  RedisContext()
      : context_(nullptr), async_context_(nullptr), subscribe_context_(nullptr) {}
  ~RedisContext();
  Status Connect(const std::string &address, int port, bool sharding,
                 const std::string &password);
  Status AttachToEventLoop(aeEventLoop *loop);

  /// Run an operation on some table key.
  ///
  /// \param command The command to run. This must match a registered Ray Redis
  /// command. These are strings of the format "RAY.TABLE_*".
  /// \param id The table key to run the operation at.
  /// \param data The data to add to the table key, if any.
  /// \param length The length of the data to be added, if data is provided.
  /// \param prefix
  /// \param pubsub_channel
  /// \param redisCallback The Redis callback function.
  /// \param log_length The RAY.TABLE_APPEND command takes in an optional index
  /// at which the data must be appended. For all other commands, set to
  /// -1 for unused. If set, then data must be provided.
  /// \return Status.
  Status RunAsync(const std::string &command, const UniqueID &id, const uint8_t *data,
                  int64_t length, const TablePrefix prefix,
                  const TablePubsub pubsub_channel, RedisCallback redisCallback,
                  int log_length = -1);

  /// Run an arbitrary Redis command without a callback.
  ///
  /// \param args The vector of command args to pass to Redis.
  /// \return Status.
  Status RunArgvAsync(const std::vector<std::string> &args);

  Status RunBuilderAsync();

  RedisCommandBuilder& command_builder() { return command_builder_; }

  /// Subscribe to a specific Pub-Sub channel.
  ///
  /// \param client_id The client ID that subscribe this message.
  /// \param pubsub_channel The Pub-Sub channel to subscribe to.
  /// \param redisCallback The callback function that the notification calls.
  /// \param out_callback_index The output pointer to callback index.
  /// \return Status.
  Status SubscribeAsync(const ClientID &client_id, const TablePubsub pubsub_channel,
                        const RedisCallback &redisCallback, int64_t *out_callback_index);
  redisContext *sync_context() { return context_; }
  redisAsyncContext *async_context() { return async_context_; }
  redisAsyncContext *subscribe_context() { return subscribe_context_; };

 private:
  redisContext *context_;
  redisAsyncContext *async_context_;
  redisAsyncContext *subscribe_context_;
  RedisCommandBuilder command_builder_;
};

}  // namespace gcs

}  // namespace ray

#endif  // RAY_GCS_REDIS_CONTEXT_H
