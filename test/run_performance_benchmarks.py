from collections import namedtuple
import json
import os
import pickle
import requests
import subprocess
import time

url = "https://api.github.com/repos/ray-project/ray/commits"

result_directory = "results"
subprocess.check_call(["mkdir", "-p", result_directory])

def install(sha):
  start_time = time.time()
  subprocess.check_call(["pip", "install", "git+git://github.com/ray-project/ray.git@{}#egg=numbuf&subdirectory=numbuf".format(sha)])
  subprocess.check_call(["pip", "install", "git+git://github.com/ray-project/ray.git@{}#egg=ray&subdirectory=lib/python".format(sha)])
  end_time = time.time()
  return end_time - start_time

def run_benchmarks(output_file_name, num_workers):
  subprocess.check_call(["python", "compute_performance_benchmarks.py",
                         "--output-file-name", output_file_name,
                         "--num-workers", num_workers])
  return {}

def cleanup(sha=None):
  subprocess.call(["pip", "uninstall", "-y", "ray", "numbuf"])

def test_commit(sha, output_file_name):
  install_time = install(sha)
  print("{} - took {} seconds to install.".format(sha))
  results = run_benchmarks(output_file_name, 1)
  return results

def success_filename(sha):
  return os.path.join(result_directory, "{}.{}".format(sha, "success"))

def failure_filename(sha):
  return os.path.join(result_directory, "{}.{}".format(sha, "failure"))

def sha_is_new(sha):
  return not os.path.exists(success_filename(sha)) and not os.path.exists(failure_filename(sha))

def save_results(sha, results):
  result_file = os.path.join(result_directory, sha)
  assert not os.path.exists(result_file)
  with open(result_file, "wb") as f:
    pickle.dump(results, f)

def get_new_shas():
  r = requests.get(url)
  commits = json.loads(r.content)
  try:
    shas = [commit["sha"] for commit in commits]
    return [sha for sha in shas if sha_is_new(sha)]
  except:
    return []

if __name__ == "__main__":
  cleanup()
  while True:
    new_shas = get_new_shas()
    for sha in new_shas:
      print("Testing commit {}".format(sha))
      try:
        results = test_commit(sha, os.path.join(result_file, sha))
      except:
        print("Failed to test commit {}.".format(sha))
        subprocess.check_call(["touch", failure_filename(sha)])
      finally:
        cleanup(sha)
    time.sleep(120)
