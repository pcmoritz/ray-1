import argparse
import pickle
import time

import ray

parser = argparse.ArgumentParser(description="Run the performance benchmarks.")
parser.add_argument("--output-file-name", type=str, help="Name of file to store the results in.")
parser.add_argument("--num-workers", type=int, help="The number of workers to use.")

@ray.remote
def f():
  return 1

if __name__ == "__main__":
  args = parser.parse_args()
  ray.init(start_ray_local=True, num_workers=args.num_workers)
  time.sleep(1)

  results = {}

  start_time = time.time()
  ids = []
  num_trials = 1000
  for _ in range(num_trials):
    ids.append(f.remote())
  end_time = time.time()
  ray.get(ids)
  results["submit"] = (end_time - start_time) / num_trials

  if args.output_file_name is not None:
    with open(args.output_file_name, "wb") as f:
      pickle.dump(repr(results), f)
  else:
    print(f)
