# C (GNU extensions)

GNU C = ISO C + extensions used by GCC/Clang and heavily by Linux, GLibC, and low-level code. Enable with `-std=gnu11`, `-std=gnu17` or `-std=gnu23` (the default for GCC). Not portable to other compilers.

## Compile

```bash
gcc -std=gnu17 -Wall -Wextra -o prog main.c
```

## Statement expressions

A block `({ ... })` that evaluates to a value — lets macros declare temporaries safely.

```c
#define MAX(a, b) ({           \
    typeof(a) _a = (a);        \
    typeof(b) _b = (b);        \
    _a > _b ? _a : _b;         \
})

int m = MAX(3, 4);   // no double-evaluation of arguments
```

## `typeof` / `__typeof__`

Deduce the type of an expression (standardized in C23 as `typeof`).

```c
typeof(x) y;            // y has x's type
__typeof__(*ptr) *p;    // pointer to pointed-to type
```

## Attributes: `__attribute__((...))`

The workhorse of GNU C. Double-underscore forms (`__attribute__`) stay valid even with `-std=c11` (strict ISO).

### Functions

```c
void die(void) __attribute__((noreturn));        // never returns
void *alloc(size_t) __attribute__((malloc));     // allocator hint
int square(int) __attribute__((pure));           // no side effects, result depends only on args
int rand(void) __attribute__((const));           // no side effects, no memory reads
void log(const char *fmt, ...) __attribute__((format(printf, 1, 2)));  // printf-style checking
static void used(void) __attribute__((used));    // emit even if "unused"
static void no(void) __attribute__((noinline));
static void inl(void) __attribute__((always_inline));
void cold(void) __attribute__((cold));           // rarely taken path
void hot(void) __attribute__((hot));             // hot path
void ctor(void) __attribute__((constructor));    // run before main()
void dtor(void) __attribute__((destructor));     // run after main()
void *f(void) __attribute__((returns_nonnull));
void vis(void) __attribute__((visibility("hidden")));
```

### Types and variables

```c
struct __attribute__((packed)) S { char a; int b; };   // no padding
struct __attribute__((aligned(64))) A { int x; };
char buf[4096] __attribute__((section(".dma"), aligned(64)));  // place in ELF section
int *p __attribute__((cleanup(free_me)));            // call free_me(&p) on scope exit
void *u __attribute__((may_alias));
```

### `likely` / `unlikely` (branch hints)

```c
#define likely(x)   __builtin_expect(!!(x), 1)
#define unlikely(x) __builtin_expect(!!(x), 0)

if (unlikely(ptr == NULL)) { handle_error(); }
```

## Builtins

```c
__builtin_expect(expr, c)          // branch prediction hint
__builtin_unreachable()            // "this can never happen" (UB if reached)
__builtin_trap()                   // generate a trap instruction
__builtin_constant_p(x)            // is x a compile-time constant?
__builtin_object_size(p, 0)        // statically known object size (hardening)
__builtin_prefetch(&arr[i])        // prefetch into cache
__builtin_bswap32(x)               // byte-swap
__builtin_clz(x) / __builtin_ctz(x) / __builtin_popcount(x)  // bit ops
__builtin_types_compatible_p(T1, T2)  // type comparison
__builtin_assume_aligned(p, 64)    // tell compiler alignment
__builtin_choose_expr(cond, e1, e2)   // compile-time conditional (needs constant_p)
```

## Computed goto

`&&label` yields the address of a label; `goto *ptr` jumps to it. Used for fast interpreters/VMs/state machines.

```c
static void *dispatch[] = { &&L_ADD, &&L_SUB, &&L_END };

#define NEXT() goto *dispatch[op]

L_ADD:
    acc += 1;
    op = next_op();
    NEXT();
L_SUB:
    acc -= 1;
    op = next_op();
    NEXT();
L_END:
    return acc;
```

## Inline assembly (`asm`)

Basic:

```c
__asm__ volatile ("nop");
```

Extended asm — `: outputs : inputs : clobbers`:

```c
int x = 10, y;
asm volatile (
    "addl %1, %0"
    : "=r"(y)          // output: y in a register
    : "r"(x)           // input: x in a register
    :                  // no clobbers
);
```

```c
// input+output operand
asm ("add %0, %0" : "+r"(x));

// compiler memory barrier (not a CPU fence)
asm volatile ("" ::: "memory");
```

Constraint letters: `r` register, `m` memory, `i` immediate, `=` write-only, `+` read-write.

## Nested functions

Functions defined inside another function, can access outer locals:

```c
void outer(void) {
    int n = 10;
    int inner(void) { return n + 1; }   // closure over n
    int r = inner();
}
```

(Requires an executable stack on some platforms — rarely used.)

## Case ranges

```c
switch (c) {
case 'a' ... 'z':   // range
    break;
case '0' ... '9':
    break;
}
```

## Zero-length arrays and flexible array members

```c
struct packet {
    int len;
    char data[];       // flexible array member (standard C99)
};
// allocate: malloc(sizeof(struct packet) + n)
```

## C23 in GNU C

`typeof` and `typeof_unqual` are now standard; GCC still provides `__typeof__`:

```c
typeof(x) y;             // keeps qualifiers
typeof_unqual(x) z;      // strips const/volatile/restrict
```

## When to use which

| Need | Tool |
|---|---|
| Portable code | ISO C ([[C_ANSI]]) |
| Linux/kernel, GLibC, low-level | GNU C |
| Branch hints | `__builtin_expect` / `likely` |
| Layout control | `__attribute__((packed/aligned/section))` |
| Safe multi-statement macros | statement expressions + `typeof` |
| Fast dispatch loops | computed goto |
| Hardware/MMIO, barriers | inline `asm` |

## Links

[[C_ANSI]]
[[C++ modern (17+)]]
[[Linux kernel]]
