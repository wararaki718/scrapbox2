#include <pybind11/pybind11.h>

int add(int i, int j)
{
    return i + j;
}

int sub(int i, int j)
{
    return i - j;
}


PYBIND11_MODULE(example, m)
{
    m.doc() = "pybind11 example plugin";
    m.def("add", &add, "A function which adds two numbers");
    m.def("sub", &sub, "A function which subs two numbers");
}
