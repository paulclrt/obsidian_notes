# CMake

Cross-platform build system **generator**: it reads `CMakeLists.txt` and produces a native build (Makefiles, Ninja, Visual Studio, Xcode...). It does not build by itself — it drives the underlying toolchain.

## Why CMake

- One `CMakeLists.txt` builds on Linux/macOS/Windows.
- Manages dependencies, compiler flags, targets, installs.
- The de-facto standard for C/C++ projects.

## Minimal project

```text
my_project/
├── CMakeLists.txt
├── src/
│   └── main.cpp
└── include/
    └── mylib.h
```

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyProject VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(my_app src/main.cpp)
target_include_directories(my_app PRIVATE include)
```

## The build workflow

```bash
cmake -S . -B build                 # configure (generate) into build/
cmake --build build                 # compile
cmake --build build -j 8            # parallel build
cmake --build build --target my_app # build a specific target
cmake --install build               # install
```

Common presets:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release   # Release/Debug/RelWithDebInfo
cmake -S . -B build -G Ninja                     # use Ninja generator
```

## Targets, not variables (Modern CMake)

Prefer **targets** and their properties over global variables and directory-scoped commands. This is the biggest mental shift.

```cmake
add_library(my_lib src/lib.cpp)      # STATIC by default unless BUILD_SHARED_LIBS
add_executable(my_app src/main.cpp)

# PUBLIC / PRIVATE / INTERFACE control propagation
target_include_directories(my_lib
    PUBLIC include          # consumers of my_lib also get it
    PRIVATE src)            # only my_lib itself

target_link_libraries(my_app PRIVATE my_lib)
```

Keyword semantics:

- `PUBLIC` — used by the target **and** propagated to anything linking it.
- `PRIVATE` — used only by the target itself.
- `INTERFACE` — not used by the target, only propagated to consumers.

## Libraries

```cmake
add_library(foo STATIC src/foo.cpp)   # libfoo.a
add_library(foo SHARED src/foo.cpp)   # libfoo.so
add_library(foo INTERFACE)            # header-only library
add_library(foo ALIAS bar::foo)       # namespaced alias for install/export
```

Header-only (INTERFACE) library:

```cmake
add_library(header_only INTERFACE)
target_include_directories(header_only INTERFACE include)
target_compile_features(header_only INTERFACE cxx_std_17)
```

## Variables

```cmake
set(MY_VAR "hello")
set(SRCS src/a.cpp src/b.cpp)
list(APPEND SRCS src/c.cpp)        # append to list

message(STATUS "var is ${MY_VAR}")

# cache variables (settable with -D)
set(ENABLE_FEATURE OFF CACHE BOOL "Enable feature")

if(ENABLE_FEATURE)
    message("feature on")
endif()
```

`if` conditions use `AND`, `OR`, `NOT`, `STREQUAL`, `DEFINED`, etc.

## find_package

Two modes: **Module** (`FindXxx.cmake`) and **Config** (`XxxConfig.cmake`, preferred, ships with the package).

```cmake
find_package(OpenSSL REQUIRED)
target_link_libraries(my_app PRIVATE OpenSSL::SSL OpenSSL::Crypto)

# version requirement
find_package(fmt 9.0 REQUIRED)
```

For Config packages installed elsewhere, point CMake at the install prefix:

```bash
cmake -S . -B build -DCMAKE_PREFIX_PATH=/path/to/installed/package
```

## Options and build types

```cmake
option(BUILD_TESTS "Build tests" ON)
option(BUILD_SHARED_LIBS "Build shared libs" OFF)  # built-in option

if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()
```

```cmake
# per-configuration compile options (avoid hardcoding in target_compile_options)
target_compile_options(my_lib PRIVATE
    $<$<CONFIG:Debug>:-Wall -Wextra>)
```

## FetchContent / CPM for dependencies

Fetch (download + build) dependencies at configure time:

```cmake
include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        v1.15.2
)
FetchContent_MakeAvailable(googletest)

target_link_libraries(my_test PRIVATE GTest::gtest_main)
```

[CPM.cmake](https://github.com/cpm-cmake/CPM.cmake) is a thin, cache-friendly wrapper around FetchContent used widely for dependency management.

## CTest: testing

```cmake
enable_testing()
add_executable(tests test_main.cpp)
target_link_libraries(tests PRIVATE my_lib GTest::gtest_main)

add_test(NAME my_tests COMMAND tests)
```

```bash
ctest --test-dir build          # run all tests
ctest --test-dir build -R my_   # filter by regex
ctest --test-dir build -V       # verbose output
```

## Install and export

```cmake
install(TARGETS my_lib
    EXPORT MyProjectTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
install(DIRECTORY include/ DESTINATION include)

install(EXPORT MyProjectTargets
    NAMESPACE myproject::
    DESTINATION lib/cmake/MyProject
)
```

This lets other projects `find_package(MyProject)` and link `myproject::my_lib`.

## Advanced (still everyday-relevant)

### Generator expressions

Evaluated at **generate time** (after configure), between `$<...>`:

```cmake
target_compile_definitions(my_lib PRIVATE
    $<$<CONFIG:Debug>:DEBUG_BUILD>
    $<$<PLATFORM_ID:Windows>:WINDOWS>)

# export/import macro for shared libraries
target_compile_definitions(my_lib PRIVATE MYLIB_BUILDING)
target_compile_definitions(my_lib INTERFACE $<$<STREQUAL:$<TARGET_PROPERTY:my_lib,TYPE>,SHARED_LIBRARY>:MYLIB_SHARED>)

# propagate include dirs to consumers of a specific build tree
target_include_directories(my_lib INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>)
```

### Interface libraries for flags/conventions

```cmake
add_library(my_project_warnings INTERFACE)
target_compile_options(my_project_warnings INTERFACE -Wall -Wextra -Wpedantic)

target_link_libraries(my_app PRIVATE my_project_warnings)
```

### Presets: `CMakePresets.json`

Shareable configure/build/test configurations, versioned with the project:

```json
{
  "version": 6,
  "configurePresets": [
    {
      "name": "default",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build",
      "cacheVariables": { "CMAKE_BUILD_TYPE": "Release" }
    }
  ],
  "buildPresets": [
    { "name": "default", "configurePreset": "default" }
  ],
  "testPresets": [
    { "name": "default", "configurePreset": "default", "output": { "outputOnFailure": true } }
  ]
}
```

```bash
cmake --preset default
cmake --build --preset default
ctest --preset default
```

### Toolchains and cross-compilation

```bash
cmake -S . -B build --toolchain arm-none-eabi.cmake
```

A toolchain file sets the compiler and system for cross-building.

### Custom commands (code generation)

```cmake
add_custom_command(
    OUTPUT generated.cpp
    COMMAND my_generator generated.cpp
    DEPENDS template.txt
)
```

### Functions and macros

```cmake
function(add_my_lib name)
    add_library(${name} ${ARGN})
    target_include_directories(${name} PUBLIC include)
endfunction()

add_my_lib(core src/core.cpp)
```

## Common pitfalls

- Always prefer `target_*` over `include_directories()` / `link_libraries()` (global).
- Never hardcode absolute paths; use `${CMAKE_CURRENT_SOURCE_DIR}`.
- `cmake_minimum_required(VERSION ...)` should be the first line.
- Re-run configure after editing `CMakeLists.txt`; a build normally triggers it automatically.

## Links

[[C_ANSI]]
[[C_GNU]]
[[C++ modern (17+)]]
[[GDB]]
