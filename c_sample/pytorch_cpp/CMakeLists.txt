cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(pytorch_cpp)

find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

add_executable(pytorch_cpp main.cpp)
target_link_libraries(pytorch_cpp "${TORCH_LIBRARIES}")
set_property(TARGET pytorch_cpp PROPERTY CXX_STANDARD 14)
