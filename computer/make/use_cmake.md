# cmake 使用指南

- Set GDB debug flag (-g) with cmake

  ```cmake
  # Solution 1:
  # Add the following line to your CMakeLists.txt file
  set(CMAKE_BUILD_TYPE Debug)
  ```

  ```sh
  # Solution 2:
  # Add a command line argument to your cmake command
  cmake -DCMAKE_BUILD_TYPE=Debug <path and other arguments>
  ```