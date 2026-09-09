#flashcards/languages/C/C_ANSI

## 1. Fixed-width integers
Which header gives you `int32_t` and `uint64_t`, and why prefer them over `int`?
?
**Answer:**
`#include <stdint.h>`. They guarantee exact width and signedness across platforms, unlike `int` whose size is implementation-defined.
<!--SR:!2026-09-13,4,270-->

## 2. Array vs pointer decay
What happens when you pass an array to a function, and how do you keep the size?
?
**Answer:**
It decays to a pointer to its first element; size is lost. Pass the length explicitly:
```c
int sum(int *arr, size_t n) { ... }
```

## 3. sizeof inside a function
Why is `sizeof(arr)` different inside a function that received the array?
?
**Answer:**
Inside the function `arr` is a pointer, so `sizeof(arr)` is the pointer size, not the array size. Use `sizeof` only where the array's full type is visible.

## 4. const pointer vs pointer to const
Decode `const int *p` vs `int *const p`.
?
**Answer:**
Read right-to-left: `const int *p` is a pointer to const int (can't modify through it); `int *const p` is a const pointer to int (can't reassign). `const int *const p` is both.

## 5. void* pointer
What is `void*` and can you assign it to a typed pointer without a cast?
?
**Answer:**
The generic object pointer. Conversion to/from any object pointer type is implicit in C (no cast needed), unlike C++.
<!--SR:!2026-09-12,3,250-->

## 6. Pointer arithmetic
If `int *p = arr;`, what does `*(p + 2)` equal and why?
?
**Answer:**
`arr[2]`. Pointer arithmetic scales by the pointed-to type's size, so `p + 2` advances by `2 * sizeof(int)`.

## 7. malloc/free
How do you allocate an array of `n` ints, check the result, and free it?
?
**Answer:**
```c
int *arr = malloc(n * sizeof(int));
if (!arr) { perror("malloc"); return 1; }
// use arr...
free(arr);
```
Always check for NULL, and `free` exactly once. `free(NULL)` is safe.

## 8. calloc vs malloc
What is the difference between `malloc` and `calloc`?
?
**Answer:**
`malloc(n)` returns uninitialized memory; `calloc(count, size)` zero-initializes the block. Both return NULL on failure.

## 9. realloc pitfall
What is the classic bug with `realloc`, and how do you avoid it?
?
**Answer:**
Assigning the result directly to the original pointer leaks memory if `realloc` fails:
```c
int *tmp = realloc(arr, new_size);
if (!tmp) { free(arr); return 1; }
arr = tmp;
```

## 10. Include guards
What do include guards do and how are they written?
?
**Answer:**
Prevent a header from being included multiple times in one translation unit:
```c
#ifndef MYLIB_H
#define MYLIB_H
// declarations...
#endif
```

## 11. Macro pitfalls
Why is `#define SQUARE(x) x*x` broken? Give the correct version.
?
**Answer:**
It breaks operator precedence and double-evaluates: `SQUARE(1+2)` → `1+2*1+2` = 5, and `SQUARE(i++)` increments twice. Correct:
```c
#define SQUARE(x) ((x) * (x))
```

## 12. static keyword
What does `static` mean on (a) a file-scope variable, (b) a local variable, (c) a function?
?
**Answer:**
(a) internal linkage (file-local); (b) value persists across calls (static storage duration); (c) function visible only in its own translation unit.

## 13. extern
What does `extern int x;` declare?
?
**Answer:**
A declaration (not definition) of a variable defined in another translation unit, giving it external linkage so it can be shared.

## 14. volatile
When do you use `volatile`?
?
**Answer:**
For variables the compiler must not optimize away or reorder: memory-mapped hardware registers, variables modified by signal handlers/ISRs, etc. It does not provide thread synchronization.

## 15. String functions
Give the safe equivalents of `strcpy`, `sprintf`, and note the return of `strcmp`.
?
**Answer:**
Use `snprintf` instead of `sprintf`, and `strncpy`/`strncat` carefully (they may not NUL-terminate). `strcmp(a,b)` returns 0 if equal, negative if `a<b`, positive if `a>b`.

## 16. memcpy vs memmove
When must you use `memmove` instead of `memcpy`?
?
**Answer:**
`memcpy` requires non-overlapping buffers (UB if they overlap). `memmove` handles overlapping regions correctly.

## 17. Undefined behavior
List four common sources of undefined behavior in C.
?
**Answer:**
Buffer overflow, signed integer overflow, use-after-free / double free, dereferencing NULL, out-of-bounds access, reading uninitialized memory, `= ` vs `==` mistakes.

## 18. = vs ==
What bug does `if (x = 0)` introduce and how do you avoid it?
?
**Answer:**
It assigns 0 to `x` and evaluates as false always. Compile with `-Wall` (catches it), or write `if (0 == x)`.

## 19. Signed vs unsigned comparison
Why can `if (i < n)` misbehave when `i` is `int` and `n` is `size_t`?
?
**Answer:**
The `int` is converted to `unsigned`, so a negative `i` becomes huge. This can silently break loop conditions; keep types consistent or cast explicitly.

## 20. Flexible array member
What is a flexible array member and how do you allocate it?
?
**Answer:**
A zero-size array as the last struct member for variable-length data (C99):
```c
struct packet { int len; char data[]; };
struct packet *p = malloc(sizeof(struct packet) + n);
```

## 21. struct alignment
Why is `sizeof(struct { char a; int b; })` often 8 and not 5? How to inspect the layout?
?
**Answer:**
Padding is inserted to align `b` on a 4-byte boundary. Use `offsetof(struct S, b)` (from `<stddef.h>`) to see the actual offset.

## 22. Read a file line by line
Write a loop that prints each line of a text file safely.
?
**Answer:**
```c
FILE *f = fopen("file.txt", "r");
if (!f) { perror("fopen"); return 1; }
char line[256];
while (fgets(line, sizeof(line), f)) {
    printf("%s", line);
}
fclose(f);
```

## 23. Parse a config line
Parse `key=value` pairs from a line using sscanf.
?
**Answer:**
```c
char key[64], value[64];
if (sscanf(line, "%63[^=]=%63s", key, value) == 2) {
    // key and value extracted
}
```
Width limits (`%63s`) prevent overflow.

## 24. Dynamic array grow
Write a helper that appends to a dynamically-grown int array.
?
**Answer:**
```c
typedef struct { int *data; size_t len, cap; } Vec;

void push(Vec *v, int x) {
    if (v->len == v->cap) {
        v->cap = v->cap ? v->cap * 2 : 8;
        v->data = realloc(v->data, v->cap * sizeof(int));
    }
    v->data[v->len++] = x;
}
```

## 25. qsort comparator
Sort an array of structs by a field using `qsort`.
?
**Answer:**
```c
typedef struct { int id; char name[32]; } Person;
int cmp(const void *a, const void *b) {
    const Person *pa = a, *pb = b;
    return (pa->id > pb->id) - (pa->id < pb->id);   // safe compare
}
qsort(people, n, sizeof(Person), cmp);
```
<!--SR:!2026-09-10,1,230-->

## 26. String tokenize
Split a comma-separated string into tokens.
?
**Answer:**
```c
char input[] = "a,b,c";           // strtok modifies its argument
for (char *tok = strtok(input, ",");
     tok; tok = strtok(NULL, ",")) {
    printf("%s\n", tok);
}
```

## 27. Safe integer input
Read an integer from stdin robustly, rejecting non-numeric input.
?
**Answer:**
```c
char buf[64];
if (fgets(buf, sizeof(buf), stdin)) {
    char *end;
    long v = strtol(buf, &end, 10);
    if (end != buf && *end == '\n') {
        // v is valid
    }
}
```

## 28. Type dispatch with _Generic
Write a macro that prints an int or a double with the right format specifier.
?
**Answer:**
```c
#define print(x) printf(_Generic((x), \
    int: "%d\n", double: "%f\n"), (x))
```

## 29. Compile-time checks
Enforce a struct size at compile time.
?
**Answer:**
```c
#include <assert.h>
_Static_assert(sizeof(struct packet) == 32, "ABI mismatch");
```
(C11 `_Static_assert`; C23 also allows `static_assert`.)

## 30. Bit manipulation
Write a macro to test, set, and clear the n-th bit of an integer.
?
**Answer:**
```c
#define BIT(n) (1UL << (n))
#define TEST(x, n) ((x) & BIT(n))
#define SET(x, n)  ((x) |= BIT(n))
#define CLR(x, n)  ((x) &= ~BIT(n))
```

## 31. Swap without temp (XOR)
Write an XOR swap and note why it's usually discouraged.
?
**Answer:**
```c
a ^= b; b ^= a; a ^= b;
```
Fragile: UB/failure if `a` and `b` alias the same object, and less clear than a temp variable. Prefer `int t = a; a = b; b = t;`.

## 32. Counting bits
Implement popcount (number of set bits) with Kernighan's trick.
?
**Answer:**
```c
int popcount(unsigned x) {
    int c = 0;
    while (x) { x &= x - 1; c++; }   // clears lowest set bit
    return c;
}
```

## 33. Function pointer
Declare a function pointer and use it as a callback.
?
**Answer:**
```c
int add(int a, int b) { return a + b; }
int (*op)(int, int) = add;
int r = op(1, 2);            // 3
```
<!--SR:!2026-09-12,3,250-->

## 34. Variadic function
Write a variadic `sum` using `<stdarg.h>`.
?
**Answer:**
```c
#include <stdarg.h>
int sum(int n, ...) {
    va_list ap; va_start(ap, n);
    int total = 0;
    for (int i = 0; i < n; i++) total += va_arg(ap, int);
    va_end(ap);
    return total;
}
```
<!--SR:!2026-09-10,1,230-->

## 35. Error handling pattern
Write a small program skeleton that cleans up resources on every error path.
?
**Answer:**
```c
int main(void) {
    FILE *f = fopen("in.txt", "r");
    if (!f) { perror("fopen"); return 1; }
    char *buf = malloc(1024);
    if (!buf) { fclose(f); return 1; }   // clean up before returning
    // ...
    free(buf);
    fclose(f);
    return 0;
}
```
