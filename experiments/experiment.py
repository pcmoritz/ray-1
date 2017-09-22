@ray.remote
def f(x):
    return None

@ray.remote
def g(x):
    ray.get([f.remote(x) for i in range(50000)])
    return 1

%time l = [g.remote(1) for i in range(10)]; ray.get(l)


# without replication:

# 31.4s

# 32.5s

# 33.1s

# 39.1s

# 43.2s

# with replication:

# 36.2s

# 39.7s

# 39.3s

# 37.9s

# 40.6s
