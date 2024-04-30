import time

import integrate
import integrate_cython

if __name__ == '__main__':
    N = 1_0000_0000
    a = 1
    b = 1000

    start = time.perf_counter()
    integrate.integrate_f(a, b, N)
    print("python", time.perf_counter() - start)

    start = time.perf_counter()
    integrate_cython.integrate_f(a, b, N)
    print("cython", time.perf_counter() - start)
