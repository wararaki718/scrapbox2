from Cython.Distutils import build_ext
from Cython.Build import cythonize
from distutils.core import setup
from distutils.extension import Extension

setup (
    name='mypackage',
    version='1.0',
    ext_modules=cythonize([Extension('mypackage.clogic', ['mypackage/clogic.pyx'])]),
    cmdclass={'build_ext': build_ext}
)
