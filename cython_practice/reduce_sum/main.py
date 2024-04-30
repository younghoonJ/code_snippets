import array
import time
import numpy as np
import reduce_sum_cython


def reduce_sum(vals):
    ret = 0
    for v in vals:
        ret += v

    return ret


def reduce_sum_loop_unroll(vals):
    q, r = divmod(len(vals), 5)
    ret = 0
    for i in range(q):
        ii = i * 5
        ret += vals[ii] + vals[1 + ii] + vals[2 + ii] + vals[3 + ii] + vals[4 + ii]
    for v in vals[:-r]:
        ret += v
    return ret


if __name__ == "__main__":
    vals = [1 for _ in range(100000000)]
    arr_vals = array.array("i", vals)
    np_arr = np.array(vals)

    ans = sum(vals)

    ts = time.perf_counter()
    a0 = reduce_sum_cython.reduce_sum(vals)
    print("cy", time.perf_counter() - ts)
    assert a0 == ans

    ts = time.perf_counter()
    a1 = reduce_sum(vals)
    print("py", time.perf_counter() - ts)
    assert a1 == ans

    ts = time.perf_counter()
    a2 = sum(vals)
    print("py_sum_func", time.perf_counter() - ts)
    assert a2 == ans

    ts = time.perf_counter()
    a3 = reduce_sum_loop_unroll(vals)
    print("py_loop_unroll", time.perf_counter() - ts)
    assert a3 == ans

    ts = time.perf_counter()
    a4 = reduce_sum_cython.reduce_sum_arr(arr_vals, len(arr_vals))
    print("cy_arr_sum", time.perf_counter() - ts)
    assert a4 == ans

    ts = time.perf_counter()
    a5 = np_arr.sum()
    print("py_numpy", time.perf_counter() - ts)
    assert a5 == ans

    ts = time.perf_counter()
    a6 = reduce_sum_cython.reduce_sum_np_arr(np_arr)
    print("cy_numpy", time.perf_counter() - ts)
    assert a6 == ans

    ts = time.perf_counter()
    a7 = reduce_sum_cython.reduce_sum_np_arr_with_dt(np_arr)
    print("cy_numpy_with_dt", time.perf_counter() - ts)
    assert a7 == ans

    ts = time.perf_counter()
    a8 = reduce_sum_cython.reduce_sum_np_arr_with_dt_no_bound_check(np_arr)
    print("cy_numpy_with_dt_no_bound_check", time.perf_counter() - ts)
    assert a8 == ans

    ts = time.perf_counter()
    a9 = reduce_sum_cython.reduce_sum_np_arr_with_dt_no_bound_check2(np_arr)
    print("cy_numpy_with_dt_no_bound_check2", time.perf_counter() - ts)
    assert a9 == ans