import numpy as np
cimport numpy as np
cimport cython

np.import_array()


def reduce_sum(object input_list):
    cdef long long ret
    ret = 0
    for val in input_list:
        ret += val
    return ret

def reduce_sum_arr(int[:] input_arr, int array_len):
    cdef long long i
    cdef long long ret = 0
    for i in range(array_len):
        ret += input_arr[i]
    return ret

def reduce_sum_np_arr(np.ndarray arr):
    cdef long long ret = 0
    cdef long long data_len = arr.shape[0]
    cdef long long i
    for i in range(data_len):
        ret += arr[i] # here is an python indexing
    return ret

def reduce_sum_np_arr_with_dt(np.ndarray[np.int_t, ndim=1] arr):
    cdef long long ret = 0
    cdef long long data_len = arr.shape[0]
    cdef long long i
    for i in range(data_len):
        ret += arr[i]
    return ret


ctypedef np.int_t DTYPE_t

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def reduce_sum_np_arr_with_dt_no_bound_check(np.ndarray[DTYPE_t, ndim=1] arr):
    cdef long long ret = 0
    cdef long long data_len = arr.shape[0]
    cdef long long i
    for i in range(data_len):
        ret += arr[i]
    return ret


@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def reduce_sum_np_arr_with_dt_no_bound_check2(DTYPE_t[:] arr):
    cdef long long ret = 0
    cdef long long data_len = arr.shape[0]
    cdef long long i
    for i in range(data_len):
        ret += arr[i]
    return ret