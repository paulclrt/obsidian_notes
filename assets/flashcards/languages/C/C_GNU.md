#flashcards/languages/C/C_GNU

## 1. What is GNU C
What is "GNU C" and which compiler flags enable it?
?
**Answer:**
ISO C plus the extensions provided by GCC/Clang (attributes, builtins, statement expressions, inline asm, computed goto). Enabled by default; explicit via `-std=gnu11`, `-std=gnu17`, `-std=gnu23`.

## 2. Statement expressions
What does `({ ... })` do and why is it useful in macros?
?
**Answer:**
It turns a block into an expression whose value is the last statement, letting a macro hold local variables safely:
```c
#define MAX(a,b) ({ typeof(a) _a=(a); typeof(b) _b=(b); _a>_b?_a:_b; })
```

## 3. typeof
What does `typeof(x)` give you, and what is its standardized name?
?
**Answer:**
The type of expression `x` (standardized in C23 as `typeof`). GCC/Clang also provide `__typeof__` which survives `-std=c11` strict mode.

## 4. noreturn
How do you tell the compiler a function never returns?
?
**Answer:**
```c
void die(void) __attribute__((noreturn));
```
The compiler then knows code after a call to it is unreachable.

## 5. format attribute
How does GCC type-check a custom `printf`-like function?
?
**Answer:**
```c
void log(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
```
Args 1 and 2 tell GCC: parameter 1 is the format string, variadic args start at parameter 2.

## 6. packed
What does `__attribute__((packed))` do and what is its danger?
?
**Answer:**
It removes padding/alignment, packing members tightly (useful for ABI/binary formats). Danger: unaligned access can be slow or fault on some architectures.

## 7. aligned
What does `__attribute__((aligned(64)))` guarantee?
?
**Answer:**
The object is aligned to at least a 64-byte boundary. Useful for cache lines, DMA, SIMD buffers.

## 8. section
What does `__attribute__((section(".dma")))` do, and what decides the final placement?
?
**Answer:**
It places the object in an ELF section named `.dma`. The linker script ultimately decides where that section lives in the final image.

## 9. constructor / destructor
How do you run code automatically before/after `main`?
?
**Answer:**
```c
void init(void) __attribute__((constructor));
void fini(void) __attribute__((destructor));
```
ELF user-space mechanism; in bare-metal it depends on startup code actually invoking constructors.

## 10. likely / unlikely
How do you give a branch-prediction hint?
?
**Answer:**
```c
#define likely(x)   __builtin_expect(!!(x), 1)
#define unlikely(x) __builtin_expect(!!(x), 0)

if (unlikely(ptr == NULL)) { handle_error(); }
```

## 11. __builtin_unreachable
What does `__builtin_unreachable()` promise, and what happens if violated?
?
**Answer:**
It tells the compiler this path can never be reached, enabling aggressive optimization. If actually reached at runtime, it's undefined behavior.

## 12. __builtin_trap vs unreachable
What is the difference between `__builtin_trap()` and `__builtin_unreachable()`?
?
**Answer:**
`unreachable` = "this cannot happen" (UB if it does). `trap` = "if this happens, abort immediately" (emits a trap instruction).

## 13. __builtin_constant_p
What does `__builtin_constant_p(x)` enable?
?
**Answer:**
Compile-time detection of whether `x` is a known constant, enabling static specialization inside macros/functions without templates.

## 14. cleanup attribute
How does `__attribute__((cleanup(fn)))` simulate RAII in C?
?
**Answer:**
`fn(&var)` is called automatically when `var` leaves scope:
```c
void free_p(int **p) { free(*p); }
int *p __attribute__((cleanup(free_p))) = malloc(100);
```

## 15. visibility
What does `__attribute__((visibility("hidden")))` control?
?
**Answer:**
ELF symbol visibility for dynamic linking: `hidden` symbols are not exported/preemptable across shared-library boundaries (smaller, faster `.so`).

## 16. Computed goto
What is a computed goto and where is it used?
?
**Answer:**
`&&label` yields a label's address; `goto *ptr` jumps to it. Used for fast dispatch in interpreters/VMs/state machines:
```c
static void *t[] = { &&A, &&B };
goto *t[op];
A: ; B: ;
```

## 17. Extended asm syntax
Decode the three colon sections of extended `asm`.
?
**Answer:**
`asm("insn" : outputs : inputs : clobbers);`
- outputs: `"=r"(y)` write-only register
- inputs: `"r"(x)` register input
- clobbers: registers/`"memory"` that may be modified

## 18. Compiler barrier
What does `asm volatile ("" ::: "memory");` do, and what does it NOT do?
?
**Answer:**
A compiler barrier: it prevents the compiler from reordering memory accesses across it. It is not a CPU memory fence and not an atomic operation.

## 19. Read/write operand
What does `"+r"(x)` mean in an asm operand?
?
**Answer:**
A read-write operand: the asm both reads and modifies `x`. Required so the compiler doesn't keep a stale value of `x`.

## 20. Case ranges
How do you match a range of values in a `switch`?
?
**Answer:**
```c
switch (c) {
case 'a' ... 'z': break;
case '0' ... '9': break;
}
```

## 21. __builtin_expect semantics
What exactly does `__builtin_expect(x, c)` influence?
?
**Answer:**
It gives the compiler a branch-prediction heuristic (expected value of `x`) that influences code layout and branch ordering. Not a hardware prediction guarantee.

## 22. pure vs const
Distinguish `__attribute__((pure))` and `__attribute__((const))`.
?
**Answer:**
`pure`: no side effects; result depends only on arguments and global memory (may read globals). `const`: no side effects and reads no memory; result depends only on arguments. Enables CSE across calls.

## 23. malloc attribute
What does `__attribute__((malloc))` tell the optimizer?
?
**Answer:**
The returned pointer does not alias any other pointer, so the compiler can assume the memory is fresh and perform more aggressive optimizations.

## 24. unused vs used
Contrast `__attribute__((unused))` and `__attribute__((used))`.
?
**Answer:**
`unused` silences "defined but not used" warnings. `used` forces the compiler to emit the function/object even if it appears unreferenced (e.g. for asm/linker references).

## 25. Inline asm: sum two ints
Write a snippet using extended asm to add two ints and store the result.
?
**Answer:**
```c
int x = 10, y;
asm volatile ("addl %1, %0"
              : "=r"(y)   // output
              : "r"(x)    // input
              :           // no clobbers
);
```

## 26. Build a likely/unlikely macro
Write `likely`/`unlikely` macros with correct double-bang usage.
?
**Answer:**
```c
#define likely(x)   __builtin_expect(!!(x), 1)
#define unlikely(x) __builtin_expect(!!(x), 0)
```
`!!` normalizes the argument to 0 or 1.

## 27. State machine with computed goto
Sketch an accumulator loop using computed goto dispatch.
?
**Answer:**
```c
int acc = 0;
static void *next[] = { &&ADD, &&END };
int op = 0;
goto *next[op];
ADD:
    acc += 1;
    op = 1;
    goto *next[op];
END:
    return acc;
```

## 28. Place a function in a custom section
Put a function in `.boot.text` so the linker can locate it specially.
?
**Answer:**
```c
void boot_init(void) __attribute__((section(".boot.text")));
```
Common in bootloaders/firmware to control ROM/RAM placement via the linker script.

## 29. likely in a hot loop
Show an idiomatic hot loop that uses `unlikely` for the rare error branch.
?
**Answer:**
```c
for (int i = 0; i < n; i++) {
    if (unlikely(data[i] < 0)) {
        handle_negative();   // rare path kept out of line
        break;
    }
    process(data[i]);
}
```

## 30. Detect a constant argument
Write a macro/function that behaves differently for a compile-time constant.
?
**Answer:**
```c
#define SIZEOF(x) (__builtin_constant_p(x) ? (int)sizeof(x) : -1)
```
Lets you choose a static path when the size is known at compile time.

## 31. Zero-cost bounds check
Use `__builtin_object_size` to add a compile-time overflow check helper.
?
**Answer:**
```c
#define SAFE_CPY(d, s) \
    do { if (__builtin_object_size(d, 0) < strlen(s) + 1) \
             handle_overflow(); \
         strcpy(d, s); } while (0)
```
The compiler can statically determine the destination size and optimize/eliminate the check.

## 32. Byte swap and bit builtins
Name the builtins for byte-swap, leading zeros, and popcount.
?
**Answer:**
`__builtin_bswap32/64` (byte swap), `__builtin_clz/ctz` (count leading/trailing zeros), `__builtin_popcount` (set bits). Map to single machine instructions where available.
