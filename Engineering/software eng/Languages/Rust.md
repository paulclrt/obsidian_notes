# Rust

Systems language with memory safety **without** a garbage collector. The compiler enforces ownership/borrowing rules at compile time, so "if it compiles, there are no data races / no use-after-free". Modern alternative to C/C++ for anything from CLI tools to kernels.

## Tooling: Cargo

`cargo` is the build system + package manager + test runner, all in one.

```bash
cargo new my_project        # create a new binary crate
cargo new --lib my_lib      # create a library crate
cargo build                 # debug build -> target/debug/
cargo build --release       # optimized build -> target/release/
cargo run                   # build + run
cargo check                 # type-check only (fast, no codegen)
cargo test                  # run tests
cargo add serde             # add a dependency (edits Cargo.toml)
cargo fmt                   # format code
cargo clippy                # lints
```

A project looks like:

```text
my_project/
├── Cargo.toml      # manifest: name, version, dependencies
└── src/
    └── main.rs     # entry point: fn main()
```

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = "1"
```

## Basics

### Variables, immutability, shadowing

Variables are **immutable by default**.

```rust
let x = 5;          // immutable
// x = 6;           // ERROR: cannot assign twice to immutable variable

let mut y = 5;      // mutable
y = 6;              // ok

let z = 5;
let z = z + 1;      // shadowing: a *new* variable, allowed even without mut
```

Shadowing lets you reuse a name and even change its type:

```rust
let s = "hello";          // &str
let s = s.len();          // usize  (shadowed, different type)
```

Constants are compile-time:

```rust
const MAX_POINTS: u32 = 100_000;
```

### Scalar types

```rust
// integers: i8 i16 i32 i64 i128 isize  (signed)
//           u8 u16 u32 u64 u128 usize  (unsigned)  -> default i32
// floats:   f32 f64                      -> default f64
// bool, char (4 bytes, Unicode scalar)
let a: i32 = 42;
let b = 42u8;            // type suffix
let c: f64 = 3.14;
let d = true;
let e = '🦀';
```

### Compound types

```rust
// Tuple: fixed size, heterogeneous
let tup: (i32, f64, char) = (500, 6.4, 'z');
let (x, y, z) = tup;             // destructuring
let first = tup.0;               // indexed access

// Array: fixed size, homogeneous (stack)
let arr = [1, 2, 3, 4, 5];
let zeros = [0; 5];              // [0, 0, 0, 0, 0]
let a0 = arr[0];

// Slice: a view into an array/Vec
let slice: &[i32] = &arr[1..4];  // [2, 3, 4]
```

### Control flow

```rust
// if is an expression
let n = 5;
let msg = if n > 0 { "positive" } else { "not positive" };

// loop, while, for
loop {
    // infinite; use break / continue
    break;
}

while n < 10 { /* ... */ }

// for + ranges: the idiomatic way to iterate
for i in 0..5 {        // 0,1,2,3,4  (exclusive end)
    println!("{i}");
}
for i in 0..=5 {       // 0..5 inclusive
    println!("{i}");
}
```

## Ownership, Borrowing, Lifetimes

The core idea: **every value has exactly one owner**; when the owner goes out of scope the value is dropped (freed).

```rust
{
    let s = String::from("hello");  // s owns the string
    let t = s;                       // ownership MOVED to t
    // println!("{s}");              // ERROR: s was moved
    println!("{t}");
} // t dropped here
```

Types that implement `Copy` (ints, floats, bools, char, tuples of Copy) are copied instead of moved:

```rust
let a = 5;
let b = a;      // copied (i32 is Copy)
println!("{a}"); // fine
```

### Borrowing: references

Instead of moving, you can **borrow** with a reference.

```rust
fn len(s: &String) -> usize { s.len() }   // borrows, does not take ownership

let s = String::from("hello");
let l = len(&s);          // &s borrows
println!("{s}");          // still valid
```

Rules (enforced at compile time):

- Either **one mutable reference** `&mut T` **or** any number of immutable references `&T`, never both at once.
- References must always be valid (no dangling references).

```rust
let mut s = String::from("hello");
let r = &mut s;
r.push_str(" world");   // ok
// let r2 = &s;         // ERROR: cannot borrow as immutable while mutably borrowed
```

### Lifetimes

Lifetimes tell the compiler how long references are valid. Most of the time they are **elided** (inferred). You only annotate them when the compiler can't tell the relationship between inputs and output:

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

`'a` says: the returned reference lives as long as the shorter of the two inputs.

```rust
struct Excerpt<'a> {
    part: &'a str,       // struct holding a reference needs a lifetime
}
```

## Structs, Enums, Matching

### Structs

```rust
struct User {
    username: String,
    active: bool,
}

let u = User { username: String::from("alice"), active: true };
println!("{}", u.username);

// field init shorthand + update syntax
let u2 = User { active: false, ..u };

// tuple structs
struct Point(i32, i32);
let p = Point(1, 2);
let x = p.0;

// unit struct
struct Marker;
```

Methods via `impl`:

```rust
impl User {
    fn new(name: &str) -> Self {
        Self { username: name.to_string(), active: true }
    }
    fn is_active(&self) -> bool { self.active }
}
```

### Enums and `match`

Enums in Rust can carry data (algebraic data types) — the workhorse of the language.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

// match is exhaustive
fn handle(m: Message) -> i32 {
    match m {
        Message::Quit => 0,
        Message::Move { x, y } => x + y,
        Message::Write(s) => s.len() as i32,
        Message::ChangeColor(r, _, _) => r,
    }
}
```

`if let` for single-case matching:

```rust
if let Message::Write(s) = m {
    println!("{s}");
}
```

## Option and Result: error handling

Rust has **no `null`** and **no exceptions**. Errors are values.

```rust
// Option<T>: Some(T) or None
enum Option<T> { Some(T), None }

// Result<T, E>: Ok(T) or Err(E)
enum Result<T, E> { Ok(T), Err(E) }
```

```rust
fn divide(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 { None } else { Some(a / b) }
}

match divide(4.0, 2.0) {
    Some(v) => println!("{v}"),
    None => println!("can't divide by zero"),
}
```

### The `?` operator

`?` unwraps `Ok`/`Some`, or early-returns the error. Only usable in functions returning `Result`/`Option`.

```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
    let content = fs::read_to_string(path)?;   // returns Err on failure
    Ok(content)
}
```

Common unwraps (use sparingly in production):

```rust
let v = opt.unwrap();                    // panics on None
let v = opt.expect("bad state");         // panics with a message
let v = opt.unwrap_or_default();         // fallback
let v = opt.unwrap_or(42);
```

### `panic!` and `main` returning `Result`

```rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = std::fs::read_to_string("file.txt")?;
    println!("{content}");
    Ok(())
}
```

## Collections

```rust
// Vec<T>: growable array (heap)
let mut v: Vec<i32> = Vec::new();
v.push(1);
v.push(2);
let v2 = vec![1, 2, 3];                 // macro
let third = v2[2];                      // panics if out of bounds
let third = v2.get(2);                  // Option<&i32> -> safe

for x in &v2 { println!("{x}"); }
for x in &mut v { *x += 1; }

// String: growable UTF-8
let mut s = String::new();
s.push_str("hello");
s.push('!');
let s2 = format!("{s} world");          // easy formatting

// HashMap
use std::collections::HashMap;
let mut scores = HashMap::new();
scores.insert("Blue", 10);
scores.insert("Red", 50);
let blue = scores.get("Blue");          // Option<&i32>
scores.entry("Blue").or_insert(0);      // insert if absent
for (k, v) in &scores { println!("{k}: {v}"); }
```

## Generics and Traits

### Generics

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest { largest = item; }
    }
    largest
}
```

### Traits

Traits define shared behavior — similar to interfaces.

```rust
trait Summary {
    fn summarize(&self) -> String;

    fn default_summary(&self) -> String {   // default impl
        String::from("(read more...)")
    }
}

impl Summary for User {
    fn summarize(&self) -> String {
        format!("{} (active={})", self.username, self.active)
    }
}

// trait bound syntax (equivalent)
fn notify(item: &impl Summary) { println!("{}", item.summarize()); }
fn notify2<T: Summary>(item: &T) { println!("{}", item.summarize()); }
```

### Derivable traits

```rust
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
struct Point { x: i32, y: i32 }
```

`Debug` enables `{:?}`, `Clone` gives `.clone()`, `PartialEq` gives `==`.

## Iterators and Closures

### Closures

Anonymous functions that capture their environment.

```rust
let add = |a, b| a + b;
let x = add(1, 2);

// closures with explicit types
let f = |a: i32, b: i32| -> i32 { a + b };

// capturing by reference / by value (move)
let s = String::from("hi");
let c = move || println!("{s}");   // takes ownership of s
```

### Iterators (lazy, zero-cost)

```rust
let nums = vec![1, 2, 3, 4, 5];

let sum: i32 = nums.iter().sum();
let squares: Vec<i32> = nums.iter().map(|x| x * x).collect();
let evens: Vec<i32> = nums.iter().filter(|x| **x % 2 == 0).copied().collect();
let first_even = nums.iter().find(|x| **x % 2 == 0);
let total = nums.iter().fold(0, |acc, x| acc + x);
```

## Modules and Crates

```rust
// modules group code; files/dirs map to modules
mod my_module {
    pub fn public_fn() {}          // pub = visible outside
    fn private_fn() {}
}

use my_module::public_fn;          // import
```

Module file layout:

```text
src/
├── main.rs          // mod my_module; -> looks for my_module.rs or my_module/mod.rs
├── my_module.rs
└── my_module/
    └── sub.rs       // pub mod sub;
```

## Concurrency

Rust's type system makes data races compile errors: you can't share mutable state without synchronization.

```rust
use std::thread;
use std::sync::{Arc, Mutex};
use std::sync::mpsc;

// spawn a thread (moves captured data)
let handle = thread::spawn(|| {
    println!("hello from a thread");
});
handle.join().unwrap();

// channels: message passing (the "share by communicating" idiom)
let (tx, rx) = mpsc::channel();
let tx2 = tx.clone();
thread::spawn(move || { tx.send(42).unwrap(); });
thread::spawn(move || { tx2.send(7).unwrap(); });
let received: i32 = rx.recv().unwrap();

// shared mutable state: Arc (reference counting) + Mutex
let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];
for _ in 0..10 {
    let counter = Arc::clone(&counter);
    handles.push(thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    }));
}
for h in handles { h.join().unwrap(); }
println!("{}", *counter.lock().unwrap());
```

## Advanced (still everyday-relevant)

### Smart pointers

```rust
// Box<T>: heap allocation, or recursion
let b = Box::new(5);

// Recursive type (needs Box because size is unknown)
enum List { Cons(i32, Box<List>), Nil }

// Rc<T>: multiple owners (single-threaded), Arc<T> = atomic (thread-safe)
use std::rc::Rc;
let a = Rc::new(String::from("shared"));
let b = Rc::clone(&a);   // increments count

// RefCell<T>: interior mutability checked at RUNTIME
use std::cell::RefCell;
let data = RefCell::new(5);
*data.borrow_mut() += 1;
```

### Trait objects: `dyn`

Dynamic dispatch for heterogeneous collections:

```rust
trait Draw { fn draw(&self); }

let shapes: Vec<Box<dyn Draw>> = vec![Box::new(Circle), Box::new(Square)];
for s in &shapes { s.draw(); }
```

### Generic types and associated types

```rust
trait Iterator {
    type Item;                       // associated type
    fn next(&mut self) -> Option<Self::Item>;
}
```

### Pattern matching power

```rust
// match guards, ranges, @ bindings, or-patterns
match value {
    0 => println!("zero"),
    1..=9 => println!("single digit"),
    n @ 10..=99 => println!("two digits: {n}"),
    _ => println!("other"),
}

// destructuring structs, enums, slices
let Point { x, y } = p;
let [first, second, ..] = arr;
```

### `impl Trait` in return position

```rust
fn make_iter() -> impl Iterator<Item = i32> {
    (0..10).map(|x| x * 2)
}
```

### Macros

```rust
// declarative macro
macro_rules! my_vec {
    ( $( $x:expr ),* ) => {
        {
            let mut v = Vec::new();
            $( v.push($x); )*
            v
        }
    };
}

let v = my_vec![1, 2, 3];
```

### `unsafe`

Opt-in escape hatch for the rare cases the compiler can't verify (FFI, raw pointers, some data structures). Keep it minimal and isolated.

```rust
unsafe fn dangerous() {}
// must be called inside an unsafe block
unsafe { dangerous(); }
```

### Async/await (requires `tokio` or similar)

```rust
// tokio = { version = "1", features = ["full"] }
#[tokio::main]
async fn main() {
    let a = fetch_data().await;
    println!("{a}");
}

async fn fetch_data() -> String {
    String::from("data")
}
```

### Error handling crates

```rust
// thiserror: ergonomic custom errors
// anyhow: application-level error handling
use anyhow::{Result, Context};

fn main() -> Result<()> {
    let content = std::fs::read_to_string("config.toml")
        .with_context(|| "failed to read config.toml")?;
    println!("{content}");
    Ok(())
}
```

## Useful crates (common starting set)

- `serde` / `serde_json` — serialization
- `clap` — CLI argument parsing
- `anyhow` / `thiserror` — error handling
- `rayon` — easy data parallelism
- `tokio` — async runtime
- `regex`, `rand`, `chrono` — general utilities

## Links

[[C_ANSI]]
[[C_GNU]]
[[C++ modern (17+)]]
