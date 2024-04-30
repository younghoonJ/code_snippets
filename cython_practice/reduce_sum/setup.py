import numpy
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="reduce_sum_cython",
    ext_modules=cythonize("reduce_sum_cython.pyx"),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)
