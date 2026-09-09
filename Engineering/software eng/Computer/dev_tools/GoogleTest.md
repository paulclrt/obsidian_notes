# GoogleTest

C++ testing framework (Google Test) + mock framework (Google Mock). The de-facto standard for unit testing C++.

## Setup with CMake (FetchContent)

```cmake
include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        v1.15.2
)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(tests tests/test_main.cpp)
target_link_libraries(tests PRIVATE GTest::gtest_main my_lib)
add_test(NAME my_tests COMMAND tests)
```

`gtest_main` links a `main()` for you; `gtest` requires your own `main`.

## Minimal test

```cpp
#include <gtest/gtest.h>

int add(int a, int b) { return a + b; }

TEST(MyTestSuite, AddWorks) {
    EXPECT_EQ(add(1, 2), 3);
}
```

## Assertions

- `ASSERT_*` — **fatal**: aborts the current test on failure.
- `EXPECT_*` — **non-fatal**: records failure and continues.

| Kind | Assertions |
|---|---|
| Equality / comparison | `EXPECT_EQ`, `NE`, `LT`, `LE`, `GT`, `GE` |
| Boolean | `EXPECT_TRUE(x)`, `EXPECT_FALSE(x)` |
| Strings | `EXPECT_STREQ` (C strings), `EXPECT_EQ` (`std::string`) |
| Floating point | `EXPECT_FLOAT_EQ`, `EXPECT_DOUBLE_EQ`, `EXPECT_NEAR(a, b, err)` |
| Exceptions | `EXPECT_THROW(stmt, Type)`, `EXPECT_NO_THROW(stmt)` |
| Death | `EXPECT_DEATH(stmt, regex)` |

```cpp
EXPECT_NEAR(0.1 + 0.2, 0.3, 1e-9);   // floats: never EXPECT_EQ
EXPECT_THROW(throw std::runtime_error("x"), std::runtime_error);
```

## Test fixtures (`TEST_F`)

Share setup/teardown state. Each test gets a fresh instance of the fixture.

```cpp
class VectorTest : public ::testing::Test {
protected:
    void SetUp() override { vec = {1, 2, 3, 4, 5}; }   // before EACH test
    std::vector<int> vec;
};

TEST_F(VectorTest, HasCorrectSize) { EXPECT_EQ(vec.size(), 5u); }
```

One-time setup: `SetUpTestSuite()` / `TearDownTestSuite()` (static members).

## Naming and filtering

```bash
./tests --gtest_list_tests                     # list all tests
./tests --gtest_filter=MyTestSuite.*          # one suite
./tests --gtest_filter=MyTestSuite.AddWorks   # one test
./tests --gtest_filter=*Add*                  # wildcard
```

## Matchers: `EXPECT_THAT`

```cpp
#include <gmock/gmock.h>
using ::testing::HasSubstr;
using ::testing::ElementsAre;

EXPECT_THAT("hello world", HasSubstr("world"));
EXPECT_THAT(std::vector<int>{1, 2, 3}, ElementsAre(1, 2, 3));
```

Common matchers: `Eq`, `Ne`, `Lt`, `Le`, `Gt`, `Ge`, `IsNull`, `NotNull`, `HasSubstr`, `StartsWith`, `Contains`, `ElementsAre`, `IsEmpty`, `SizeIs`, `DoubleNear`.

## Parameterized tests (`TEST_P`)

Same test body over many inputs:

```cpp
TEST_P(PrimeTest, IsPrime) { EXPECT_TRUE(is_prime(GetParam())); }

INSTANTIATE_TEST_SUITE_P(Primes, PrimeTest, ::testing::Values(2, 3, 5, 7, 11));
INSTANTIATE_TEST_SUITE_P(Ranges, PrimeTest, ::testing::Range(1, 20));
```

## Google Mock (gmock)

```cpp
#include <gmock/gmock.h>

class DataSource {
public:
    virtual ~DataSource() = default;
    virtual int fetch(int id) = 0;
};

class MockDataSource : public DataSource {
public:
    MOCK_METHOD(int, fetch, (int id), (override));
};

TEST(MockTest, UsesMock) {
    MockDataSource mock;
    EXPECT_CALL(mock, fetch(42)).WillOnce(::testing::Return(7));
    EXPECT_EQ(mock.fetch(42), 7);
}
```

```cpp
using ::testing::_;
EXPECT_CALL(mock, fetch(_));               // any argument
EXPECT_CALL(mock, fetch(1)).WillOnce(Return(10)).WillOnce(Return(20));
EXPECT_CALL(mock, fetch(0)).WillRepeatedly(Return(-1));
```

## Advanced

### Custom messages, skip

```cpp
EXPECT_EQ(a, b) << "context: a=" << a;
GTEST_SKIP() << "not supported here";
```

### Custom matchers

```cpp
MATCHER(IsEven, "is even") { return (arg % 2) == 0; }
EXPECT_THAT(4, IsEven());
```

### Typed tests

```cpp
template <typename T> class TypeTest : public ::testing::Test {};
using MyTypes = ::testing::Types<int, long, double>;
TYPED_TEST_SUITE(TypeTest, MyTypes);

TYPED_TEST(TypeTest, DefaultConstructible) {
    TypeParam x{};
    EXPECT_EQ(x, TypeParam{});
}
```

### Good practices

- Descriptive names, one assertion per test where practical.
- Use `EXPECT_*` unless a later assertion depends on the earlier one.
- Never `EXPECT_EQ` on floats; use `EXPECT_NEAR`.
- Keep tests fast, independent, deterministic.

## Links

[[C++ modern (17+)]]
[[CMake]]
[[GDB]]
