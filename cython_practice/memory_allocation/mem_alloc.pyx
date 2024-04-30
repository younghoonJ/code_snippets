import random
from libc.stdlib cimport malloc, free

def random_noise(int number=1):
    cdef int i

    cdef double *my_array = <double *> malloc(number * sizeof(double))

    try:
        sampler = random.normalvariate
        for i in range(number):
            my_array[i] = sampler(0, 1)
        return [x for x in my_array[:number]]
    finally:
        free(my_array)

cdef int(*add)(int, int)
cdef int _add_fn(int a, int b):
    return a + b

add = _add_fn
