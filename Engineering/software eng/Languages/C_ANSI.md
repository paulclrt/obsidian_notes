# C (ANSI / ISO standard)

The standardized C language: C89/C90, C99, C11, C17, C23. This note covers portable, standard C — no compiler extensions (those are in [[C_GNU]]).

## Compile & run

```bash
gcc -std=c17 -Wall -Wextra -o prog main.c   # strict ISO C17
cc main.c -o prog
./prog
```

Compilation pipeline: preprocess → compile → assemble → link.

```bash
gcc -E main.c      # preprocess only
gcc -S main.c      # compile to assembly
gcc -c main.c      # compile to object (no link)
```

## Types

```c
// integers
char            // 1 byte, implementation-defined signedness
short, int, long, long long
// fixed-width (stdint.h, preferred)
int8_t, uint8_t, int16_t, uint16_t, int32_t, uint32_t, int64_t, uint64_t
// sizes
size_t (stddef.h), ssize_t, ptrdiff_t
// floating point
float, double, long double
```

```c
#include <stdint.h>
#include <stdbool.h>   // bool, true, false (C99)

int32_t x = 42;
uint64_t big = 0xFFFFFFFFFFFFFFFFULL;
float f = 3.14f;
double d = 3.14;
bool ok = true;
char c = 'A';
```

Integer literals can specify type via suffixes: `42U` (unsigned), `42L` (long), `42LL` (long long). Hex/octal/binary: `0x2A`, `052`, `0b101010`.

## Control flow

```c
if (x > 0) { ... } else if (x < 0) { ... } else { ... }

switch (x) {
    case 1: ...; break;
    case 2: ...; break;
    default: ...;
}

for (int i = 0; i < 10; i++) { ... }
while (cond) { ... }
do { ... } while (cond);
```

## Functions

Declarations (prototypes) vs definitions:

```c
int add(int a, int b);        // declaration (in header)

int add(int a, int b) {       // definition (in source)
    return a + b;
}
```

In C (unlike C++), `void f();` means unspecified parameters. Use `void f(void);` for "no parameters".

## Pointers

```c
int x = 10;
int *p = &x;      // pointer to x
*p = 20;          // dereference
int **pp = &p;    // pointer to pointer

// const pointers: read right-to-left
const int *a;     // pointer to const int (can't modify through it)
int *const b;     // const pointer to int (can't reassign)

// void* is the generic pointer
void *v = &x;
int *q = v;       // void* converts implicitly to any object pointer
```

Arithmetic scales by the pointed-to size:

```c
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;         // arr decays to &arr[0]
*(p + 2) == arr[2];   // true
```

## Arrays and strings

```c
int a[5] = {1, 2, 3, 4, 5};
int a2[5] = {0};          // all zeros
int a3[] = {1, 2, 3};     // size inferred
int matrix[2][3] = {{1,2,3},{4,5,6}};

char s[] = "hello";       // includes trailing '\0'
char buf[64];
```

Arrays decay to pointers when passed to functions; pass the size explicitly:

```c
int sum(int *arr, size_t n) {
    int total = 0;
    for (size_t i = 0; i < n; i++) total += arr[i];
    return total;
}
```

## Structs, unions, enums, typedef

```c
struct Point { int x; int y; };
struct Point p = {1, 2};
p.x = 3;

// typedef removes the need for 'struct'
typedef struct { int x; int y; } Point;
Point q = {1, 2};

// designated initializers (C99)
Point r = { .x = 1, .y = 2 };

// union: one member at a time, same memory
union Value { int i; float f; char c; };
union Value v = { .i = 42 };

// enum
enum Color { RED, GREEN, BLUE };        // 0, 1, 2
enum { A = 1, B = 5, C };               // C = 6

// struct size: padded for alignment; use offsetof (stddef.h)
#include <stddef.h>
offsetof(Point, y);
```

## Storage classes & qualifiers

```c
static int file_local;     // internal linkage (file scope)
extern int shared;         // declared elsewhere
const int N = 10;          // read-only
volatile int flag;         // don't optimize away (hardware/signals)
```

- `static` on a function = visible only in its translation unit.
- `static` on a local variable = persists between calls.
- `extern` = defined in another translation unit.

## Preprocessor

```c
#include <stdio.h>       // system header
#include "mylib.h"       // local header

#define MAX 100
#define SQUARE(x) ((x) * (x))      // parenthesize args AND whole expr
#define MAX_OF(a, b) ((a) > (b) ? (a) : (b))

// include guards
#ifndef MYLIB_H
#define MYLIB_H
// ...
#endif
```

Macro pitfalls: multiple evaluation (`SQUARE(i++)`), no types, operator precedence.

## Dynamic memory

```c
#include <stdlib.h>

int *arr = malloc(10 * sizeof(int));   // uninitialized
int *z = calloc(10, sizeof(int));      // zero-initialized
arr = realloc(arr, 20 * sizeof(int));  // resize (assign back!)
free(arr);                             // always free
```

Rules: check `malloc` returns non-NULL, always `free` (exactly once), never use after free, `free(NULL)` is safe.

```c
int *arr = malloc(n * sizeof(int));
if (!arr) { perror("malloc"); return 1; }
```

## stdio

```c
#include <stdio.h>

printf("%d %s %f %c %p\n", 42, "hi", 3.14, 'x', (void*)ptr);
// %d int, %u unsigned, %ld long, %zu size_t, %x hex, %f float, %lf double, %s string, %p pointer

int n; scanf("%d", &n);              // note the &

// files
FILE *f = fopen("file.txt", "r");    // r w a rb wb
if (!f) { perror("fopen"); return 1; }
char line[256];
while (fgets(line, sizeof(line), f)) { printf("%s", line); }
fclose(f);
```

## String functions (string.h)

```c
#include <string.h>

strlen(s)                       // length
strcpy(dst, src)                // copy (unsafe if src too big)
strncpy(dst, src, n)            // copy at most n (no guaranteed NUL)
strcat(dst, src)                // concat
strcmp(a, b)                    // 0 if equal, <0 / >0
strchr(s, c)                    // find char
strstr(hay, needle)             // find substring
memcpy(dst, src, n)             // raw copy (no overlap)
memmove(dst, src, n)            // copy (handles overlap)
memset(dst, v, n)               // fill
snprintf(buf, sizeof(buf), "x=%d", x)   // safe formatting
```

Prefer `snprintf` over `sprintf`, `strncpy`/`strncat` over the unsafe `strcpy`/`strcat`, `memcpy` for fixed-size non-overlapping buffers.

## Common pitfalls

- **Undefined behavior**: buffer overflow, signed integer overflow, use-after-free, dereferencing NULL, out-of-bounds array access, reading uninitialized memory.
- `=` vs `==` in conditions (`if (x = 0)`).
- Integer promotion / sign issues: compare signed and unsigned carefully.
- Array is not a pointer: `sizeof(arr)` (inside a function) is the pointer size, not the array size.
- `scanf("%s")` overflows — use a width or `fgets`.

## Modern C (C11 / C17 / C23)

```c
// _Static_assert: compile-time check (C11)
_Static_assert(sizeof(int) == 4, "int must be 4 bytes");
static_assert(sizeof(int) == 4);          // C23 keyword

// _Generic: type dispatch at compile time (C11)
#define print_val(x) _Generic((x), int: "%d", double: "%f")(x)

// _Atomic (C11): atomic types + memory model (stdatomic.h)
#include <stdatomic.h>
atomic_int counter;
atomic_fetch_add(&counter, 1);

// _Alignas / _Alignof (C11)
alignas(64) char buffer[256];
size_t a = alignof(double);

// _Thread_local (C11)
_Thread_local int per_thread;

// _Noreturn (C11) / [[noreturn]] (C23)
_Noreturn void die(void);

// C23 additions
nullptr;                    // typed null pointer constant
typeof(x) y;                // type of expression
bool / true / false;        // now built-in keywords
// binary literals, digit separators: 0b1010, 1'000'000
```

## Links

[[C_GNU]]
[[C++ modern (17+)]]
[[GDB]]
