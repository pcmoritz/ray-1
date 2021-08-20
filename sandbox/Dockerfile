# From the ray root directory, run
# docker build -f sandbox/Dockerfile .
FROM rayproject/ray:latest
COPY python/dist/ray-2.0.0.dev0-cp37-cp37m-linux_x86_64.whl /tmp
RUN pip uninstall -y ray
RUN pip install /tmp/ray-2.0.0.dev0-cp37-cp37m-linux_x86_64.whl
