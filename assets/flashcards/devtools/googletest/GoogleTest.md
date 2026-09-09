#flashcards/devtools/googletest

## 1. ASSERT vs EXPECT
What is the difference between `ASSERT_*` and `EXPECT_*`?
?
**Answer:**
`ASSERT_*` is fatal: aborts the current test on failure. `EXPECT_*` is non-fatal: records the failure and continues. Prefer `EXPECT_*` unless later code depends on the assertion passing.

## 2. Minimal test
Write the smallest possible GoogleTest test.
?
**Answer:**
```cpp
#include <gtest/gtest.h>

int add(int a, int b) { return a + b; }

TEST(MySuite, AddWorks) {
    EXPECT_EQ(add(1, 2), 3);
}
```

## 3. TEST vs TEST_F
When do you use `TEST_F` instead of `TEST`?
?
**Answer:**
When tests need shared setup/teardown state. `TEST_F` uses a fixture class derived from `::testing::Test`, giving each test a fresh instance.

## 4. Test fixture
Write a fixture that sets up a vector before each test.
?
**Answer:**
```cpp
class VectorTest : public ::testing::Test {
protected:
    void SetUp() override { vec = {1, 2, 3, 4, 5}; }
    std::vector<int> vec;
};

TEST_F(VectorTest, HasSizeFive) { EXPECT_EQ(vec.size(), 5u); }
```

## 5. SetUp vs SetUpTestSuite
When do you use `SetUpTestSuite` instead of `SetUp`?
?
**Answer:**
`SetUp`/`TearDown` run around each test; `SetUpTestSuite`/`TearDownTestSuite` run once for the whole suite (for expensive shared init, using static members).

## 6. Floating-point assertions
Why use `EXPECT_NEAR` / `EXPECT_DOUBLE_EQ` instead of `EXPECT_EQ` for floats?
?
**Answer:**
Floating-point arithmetic has rounding error; `EXPECT_EQ` requires exact equality and fails. `EXPECT_NEAR(a, b, err)` checks `|a - b| <= err`.

## 7. String assertions
How do you compare C strings vs `std::string`?
?
**Answer:**
`EXPECT_STREQ` for C strings (compares content, not pointers); `EXPECT_EQ` works for `std::string`.

## 8. Exception assertions
How do you assert that a statement throws (or does not throw)?
?
**Answer:**
```cpp
EXPECT_THROW(throw std::runtime_error("x"), std::runtime_error);
EXPECT_NO_THROW(do_something());
```

## 9. Test filtering
How do you run a single test or a suite from the command line?
?
**Answer:**
```bash
./tests --gtest_filter=MySuite.TestName   # one test
./tests --gtest_filter=MySuite.*          # one suite
./tests --gtest_filter=-MySuite.Broken    # exclude one
```

## 10. List tests
How do you list all available tests without running them?
?
**Answer:**
```bash
./tests --gtest_list_tests
```

## 11. EXPECT_THAT matchers
Rewrite `EXPECT_EQ(v.size(), 3u)` using a matcher, and name two string matchers.
?
**Answer:**
```cpp
EXPECT_THAT(v.size(), ::testing::SizeIs(3));
```
String matchers: `HasSubstr`, `StartsWith`, `EndsWith`.

## 12. Death test
How do you verify that a statement crashes or aborts?
?
**Answer:**
```cpp
EXPECT_DEATH({ std::abort(); }, "");
```

## 13. Parameterized tests
What do `TEST_P` and `INSTANTIATE_TEST_SUITE_P` do together?
?
**Answer:**
`TEST_P` defines a test over parameters; `INSTANTIATE_TEST_SUITE_P` supplies the values. Each value becomes a separate test instance.

## 14. Parameterized test example
Write a parameterized test checking primality for several values.
?
**Answer:**
```cpp
TEST_P(PrimeTest, IsPrime) { EXPECT_TRUE(is_prime(GetParam())); }
INSTANTIATE_TEST_SUITE_P(Primes, PrimeTest, ::testing::Values(2, 3, 5, 7));
```

## 15. MOCK_METHOD
What does `MOCK_METHOD(int, fetch, (int id), (override));` declare?
?
**Answer:**
A mock of a virtual method: return type `int`, name `fetch`, one `int id` argument, with `override` specifier. It lets gmock intercept calls and set expectations.

## 16. EXPECT_CALL basics
Write a mock expectation returning a fixed value for a given argument.
?
**Answer:**
```cpp
MockDataSource mock;
EXPECT_CALL(mock, fetch(42)).WillOnce(::testing::Return(7));
```

## 17. Wildcard arguments
How do you match any argument in `EXPECT_CALL`?
?
**Answer:**
Use the wildcard `_`:
```cpp
using ::testing::_;
EXPECT_CALL(mock, fetch(_));
```

## 18. Multiple return values
Make two consecutive calls return different values.
?
**Answer:**
```cpp
EXPECT_CALL(mock, fetch(1))
    .WillOnce(::testing::Return(10))
    .WillOnce(::testing::Return(20));
```

## 19. Custom failure message
How do you add context to a failing assertion?
?
**Answer:**
Stream to the assertion:
```cpp
EXPECT_EQ(a, b) << "context: a=" << a << " b=" << b;
```

## 20. Skipping a test
How do you skip a test at runtime?
?
**Answer:**
```cpp
GTEST_SKIP() << "not supported on this platform";
```

## 21. Custom matcher
Write a matcher that checks a number is even.
?
**Answer:**
```cpp
MATCHER(IsEven, "is even") { return (arg % 2) == 0; }
EXPECT_THAT(4, IsEven());
```

## 22. Typed tests
How do you run the same test body over multiple types?
?
**Answer:**
```cpp
template <typename T> class TypeTest : public ::testing::Test {};
using MyTypes = ::testing::Types<int, long, double>;
TYPED_TEST_SUITE(TypeTest, MyTypes);

TYPED_TEST(TypeTest, DefaultConstructible) {
    TypeParam x{};
    EXPECT_EQ(x, TypeParam{});
}
```

## 23. CMake wiring
Write the CMake snippet to fetch GoogleTest and register a test executable.
?
**Answer:**
```cmake
include(FetchContent)
FetchContent_Declare(googletest GIT_REPOSITORY https://github.com/google/googletest.git GIT_TAG v1.15.2)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(tests tests/test_main.cpp)
target_link_libraries(tests PRIVATE GTest::gtest_main my_lib)
add_test(NAME my_tests COMMAND tests)
```

## 24. Test a class end to end
Write a fixture and two tests for a stack class (push/pop and empty behavior).
?
**Answer:**
```cpp
class StackTest : public ::testing::Test {
protected:
    void SetUp() override { s.push(1); s.push(2); }
    std::stack<int> s;
};

TEST_F(StackTest, Top) { EXPECT_EQ(s.top(), 2); }
TEST_F(StackTest, PopEmpties) {
    s.pop(); s.pop();
    EXPECT_TRUE(s.empty());
}
```

## 25. Mocking in a unit test
Mock a database interface and test a function that uses it.
?
**Answer:**
```cpp
class Repo {
public:
    virtual ~Repo() = default;
    virtual int get(int id) = 0;
};
class MockRepo : public Repo {
public:
    MOCK_METHOD(int, get, (int id), (override));
};

TEST(ServiceTest, UsesRepo) {
    MockRepo repo;
    EXPECT_CALL(repo, get(5)).WillOnce(::testing::Return(42));
    Service svc(&repo);
    EXPECT_EQ(svc.lookup(5), 42);
}
```

## 26. Times control
How do you assert an expectation is called at least twice?
?
**Answer:**
```cpp
EXPECT_CALL(mock, fetch(_)).Times(::testing::AtLeast(2));
```
Other cards: `.Times(2)`, `.Times(0)`, `WillRepeatedly(Return(x))`.

## 27. Death test with exit code
Verify a program exits with a specific code.
?
**Answer:**
```cpp
EXPECT_EXIT(std::exit(42), ::testing::ExitedWithCode(42), "");
```

## 28. Best practices
List three GoogleTest best practices.
?
**Answer:**
1. Descriptive names and roughly one assertion per test. 2. Use `EXPECT_NEAR` (never `EXPECT_EQ`) for floats. 3. Keep tests fast, independent, and deterministic (no shared mutable state).
