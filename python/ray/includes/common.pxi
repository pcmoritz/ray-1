from cpython cimport Py_buffer
from libc.stdint cimport uint8_t, int32_t
from libcpp.memory cimport (
    make_shared,
    shared_ptr,
    static_pointer_cast,
)


cdef class Buffer:
    """TODO."""
    cdef:
        shared_ptr[CBuffer] buf

    def __cinit__(self, buf):
        self.buf = buf

    def __getbuffer__(self, Py_buffer *buffer, int flags):
        cdef Py_ssize_t len = buf.get().Size()
        cdef Py_ssize_t itemsize = sizeof(uint8_t)

        buffer.buf = buf.get().Data()
        buffer.len = buf.get().Size()
        buffer.itemsize = itemsize
        buffer.readonly = 1
        buffer.obj = self
        buffer.ndim = 1

    def __release_buffer__(self, PyBuffer *buffer):
        pass
