#flashcards/devtools/cmake

## 1. What is CMake
What does CMake actually do (vs a compiler or a build system like make)?
?
**Answer:**
It is a build-system **generator**: it reads `CMakeLists.txt` and produces native build files (Makefiles, Ninja, VS, Xcode). The underlying toolchain does the actual compiling.

## 2. Configure and build
What two commands configure and build a project out-of-source?
?
**Answer:**
```bash
cmake -S . -B build      # configure (generate)
cmake --build build      # compile
```

## 3. cmake_minimum_required and project
What are the first two commands in a `CMakeLists.txt`?
?
**Answer:**
```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp VERSION 1.0 LANGUAGES CXX)
```

## 4. Minimal executable
Write a minimal CMakeLists.txt for a single-file C++ executable with C++17.
?
**Answer:**
```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp LANGUAGES CXX)

add_executable(my_app src/main.cpp)
target_compile_features(my_app PRIVATE cxx_std_17)
```

## 5. Targets vs global commands
Why is `target_include_directories` preferred over `include_directories()`?
?
**Answer:**
`target_*` commands attach properties to a specific target and propagate correctly; global/directory commands leak settings to everything and break when targets are composed.

## 6. PUBLIC / PRIVATE / INTERFACE
Explain the three propagation keywords.
?
**Answer:**
`PUBLIC`: used by the target and propagated to consumers. `PRIVATE`: used only by the target. `INTERFACE`: not used by the target, only propagated to consumers.

## 7. add_library variants
What do `STATIC`, `SHARED`, and `INTERFACE` produce in `add_library`?
?
**Answer:**
`STATIC` → `.a`/`.lib`; `SHARED` → `.so`/`.dll`; `INTERFACE` → header-only (no artifact), just propagates properties.

## 8. Header-only library
Write a CMake snippet for an INTERFACE (header-only) library.
?
**Answer:**
```cmake
add_library(utils INTERFACE)
target_include_directories(utils INTERFACE include)
target_compile_features(utils INTERFACE cxx_std_17)
```

## 9. Linking libraries
Create a library and an executable that uses it, exposing the library's public headers.
?
**Answer:**
```cmake
add_library(core src/core.cpp)
target_include_directories(core PUBLIC include)

add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE core)
```

## 10. Variables
How do you set, append to, and print a list variable?
?
**Answer:**
```cmake
set(SRCS src/a.cpp src/b.cpp)
list(APPEND SRCS src/c.cpp)
message(STATUS "sources: ${SRCS}")
```

## 11. Cache variables
How do you make a variable user-settable via `-D` on the command line?
?
**Answer:**
```cmake
set(ENABLE_FEATURE OFF CACHE BOOL "Enable feature")
```
Then `cmake -S . -B build -DENABLE_FEATURE=ON`.

## 12. option()
What does `option()` do?
?
**Answer:**
Creates an ON/OFF boolean cache variable:
```cmake
option(BUILD_TESTS "Build tests" ON)
```

## 13. Conditionals
Write an `if` that checks a boolean option and a string.
?
**Answer:**
```cmake
if(BUILD_TESTS)
    enable_testing()
endif()
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    message("debug build")
endif()
```

## 14. find_package
How do you locate and link an external package, and what are the two modes?
?
**Answer:**
`find_package(OpenSSL REQUIRED)` then link `OpenSSL::SSL`. Two modes: Module (`FindXxx.cmake`) and Config (`XxxConfig.cmake`, preferred, ships with the package).

## 15. CTest basics
Register and run tests with CTest.
?
**Answer:**
```cmake
enable_testing()
add_test(NAME my_tests COMMAND my_test_exe)
```
```bash
ctest --test-dir build -R my_tests
```

## 16. Build types
How do you request a Release build, and what are the common types?
?
**Answer:**
`-DCMAKE_BUILD_TYPE=Release`. Types: `Debug`, `Release`, `RelWithDebInfo`, `MinSizeRel` (single-config generators).

## 17. Generator expressions
When are generator expressions (`$<...>`) evaluated, and give an example.
?
**Answer:**
At generate time (after configure), unlike normal variables (configure time). Example: `$<$<CONFIG:Debug>:-DDEBUG_BUILD>` adds a define only in Debug.

## 18. BUILD_INTERFACE vs INSTALL_INTERFACE
Why wrap include dirs in `$<BUILD_INTERFACE:...>` / `$<INSTALL_INTERFACE:...>`?
?
**Answer:**
So the same target uses the source-tree path when built in-tree, but the install-tree path (`include`) when consumed by an installed package.

## 19. FetchContent
How do you fetch and build a dependency at configure time?
?
**Answer:**
```cmake
include(FetchContent)
FetchContent_Declare(googletest GIT_REPOSITORY https://github.com/google/googletest.git GIT_TAG v1.15.2)
FetchContent_MakeAvailable(googletest)
```

## 20. Install targets
Install a library and its headers so another project can use it.
?
**Answer:**
```cmake
install(TARGETS core LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
install(DIRECTORY include/ DESTINATION include)
```

## 21. Full project with tests
Write a complete CMakeLists.txt: a library, an app, and a GTest-based test target.
?
**Answer:**
```cmake
cmake_minimum_required(VERSION 3.16)
project(Demo LANGUAGES CXX)

add_library(core src/core.cpp)
target_include_directories(core PUBLIC include)

add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE core)

include(FetchContent)
FetchContent_Declare(googletest GIT_REPOSITORY https://github.com/google/googletest.git GIT_TAG v1.15.2)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(tests tests/test_core.cpp)
target_link_libraries(tests PRIVATE core GTest::gtest_main)
add_test(NAME core_tests COMMAND tests)
```

## 22. Interface library for warnings
Create an INTERFACE target that centralizes warning flags and link it into an app.
?
**Answer:**
```cmake
add_library(warnings INTERFACE)
target_compile_options(warnings INTERFACE -Wall -Wextra -Wpedantic)

add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE warnings)
```

## 23. Export a package
Export targets so downstream `find_package` can use `mylib::core`.
?
**Answer:**
```cmake
install(TARGETS core EXPORT MyLibTargets ...)
install(EXPORT MyLibTargets NAMESPACE mylib:: DESTINATION lib/cmake/MyLib)
```

## 24. CMakePresets.json
What is a preset file and how do you use it?
?
**Answer:**
`CMakePresets.json` stores shared configure/build/test settings. Use `cmake --preset default`, `cmake --build --preset default`, `ctest --preset default`.

## 25. Custom command (code generation)
Write an `add_custom_command` that generates a file from a template.
?
**Answer:**
```cmake
add_custom_command(
    OUTPUT generated.cpp
    COMMAND my_generator template.txt generated.cpp
    DEPENDS template.txt
)
```
Then add `generated.cpp` to a target's sources.

## 26. Function with arguments
Write a CMake function that wraps `add_library` and sets public includes.
?
**Answer:**
```cmake
function(add_my_lib name)
    add_library(${name} ${ARGN})
    target_include_directories(${name} PUBLIC include)
endfunction()
add_my_lib(core src/core.cpp)
```

## 27. Choose a generator
How do you use Ninja instead of the default Makefiles generator?
?
**Answer:**
`cmake -S . -B build -G Ninja`. Check generators with `cmake --help`.

## 28. Toolchain for cross-compilation
How do you cross-compile with a toolchain file?
?
**Answer:**
`cmake -S . -B build --toolchain arm-none-eabi.cmake`. The file sets `CMAKE_SYSTEM_NAME`, `CMAKE_C_COMPILER`, etc.

## 29. Compile-time define per config
Add a `DEBUG_BUILD` macro only in Debug using a generator expression.
?
**Answer:**
```cmake
target_compile_definitions(app PRIVATE $<$<CONFIG:Debug>:DEBUG_BUILD>)
```

## 30. Common pitfalls
Name three CMake anti-patterns to avoid.
?
**Answer:**
1. Global `include_directories`/`link_libraries` (prefer `target_*`). 2. Hardcoded absolute paths. 3. Forgetting `cmake_minimum_required` as the first line (or omitting re-configure after edits).
