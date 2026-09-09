#flashcards/languages/rust

## 1. Mutability
In Rust, variables are immutable by default. How do you make a binding mutable, and what happens if you try to reassign an immutable one?
?
**Answer:**
Use `let mut`. Reassigning an immutable binding is a compile error.
```rust
let x = 5;
// x = 6;              // error: cannot assign twice to immutable variable
let mut y = 5;
y = 6;                 // ok
```

## 2. Shadowing vs mutability
What is the difference between shadowing and `mut`?
?
**Answer:**
Shadowing creates a new binding (and may change type); `mut` mutates the same binding in place (type stays fixed).
```rust
let s = "hello";       // &str
let s = s.len();       // usize — shadowing, new type allowed
let mut n = 5;         // must stay i32
```

## 3. Ownership and moves
Why does this not compile?
```rust
let s = String::from("hello");
let t = s;
println!("{}", s);
```
?
**Answer:**
`String` is not `Copy`, so ownership is moved from `s` to `t`; `s` is invalidated. Only `Copy` types (ints, floats, bool, char, tuples of Copy) are copied implicitly.

## 4. Borrowing rules
State the two core borrowing rules enforced at compile time.
?
**Answer:**
1. Either one mutable reference `&mut T` or any number of immutable references `&T` — never both at once.
2. References must always be valid (no dangling references).

## 5. References vs moving
How do you pass a value to a function without transferring ownership?
?
**Answer:**
Borrow it with a reference:
```rust
fn len(s: &String) -> usize { s.len() }
let s = String::from("hello");
let l = len(&s);   // borrows; s still usable afterwards
```

## 6. String vs &str
What is the difference between `String` and `&str`?
?
**Answer:**
`String` is an owned, growable, heap-allocated UTF-8 buffer; `&str` is an immutable borrowed slice of a string (a view). `&String` coerces to `&str`.

## 7. Vec vs array vs slice
When do you use `Vec<T>`, an array `[T; N]`, or a slice `&[T]`?
?
**Answer:**
Array `[T; N]`: fixed size, on the stack. `Vec<T>`: growable, heap. Slice `&[T]`: a borrowed view into either, for functions that don't need ownership.

## 8. Option and Result
What are the two core enums for handling absence and errors?
?
**Answer:**
```rust
enum Option<T> { Some(T), None }
enum Result<T, E> { Ok(T), Err(E) }
```
`Option` replaces `null`; `Result` replaces exceptions.

## 9. The ? operator
What does `?` do, and where can it be used?
?
**Answer:**
It unwraps `Ok`/`Some` or early-returns the `Err`/`None`. Usable only in functions returning `Result` or `Option` (or a type implementing `FromResidual`):
```rust
fn read() -> Result<String, std::io::Error> {
    Ok(std::fs::read_to_string("f.txt")?)
}
```

## 10. unwrap vs expect
What do `unwrap()` and `expect(msg)` do?
?
**Answer:**
Both return the inner value or panic on `None`/`Err`. `expect` panics with the provided message, giving better diagnostics than `unwrap`.

## 11. match exhaustiveness
Why is `match` safer than a chain of `if`?
?
**Answer:**
`match` is exhaustive: the compiler checks that all possible cases are covered, so you cannot forget a variant.

## 12. Methods: self vs &self vs &mut self
Explain the three receiver forms.
?
**Answer:**
`self` consumes the value; `&self` borrows immutably; `&mut self` borrows mutably. Choose the least powerful one that works.

## 13. Traits
What is a trait, and how do you implement one for a type?
?
**Answer:**
A trait defines shared behavior (like an interface). Implement with `impl Trait for Type { ... }`. Trait bounds: `fn f(x: &impl Trait)` or `fn f<T: Trait>(x: &T)`.

## 14. Derive macros
What does `#[derive(Debug, Clone, PartialEq)]` give you?
?
**Answer:**
Auto-implements those traits: `Debug` for `{:?}` printing, `Clone` for `.clone()`, `PartialEq` for `==`. Useful for structs/enums with plain data.

## 15. Lifetimes
When do you need to annotate lifetimes, and what does `'a` mean?
?
**Answer:**
Only when the compiler cannot infer the relationship between input and output references. `'a` ties the returned reference's lifetime to the shortest-lived input:
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

## 16. panic! vs Result
When should you `panic!` instead of returning `Result`?
?
**Answer:**
`Result` for expected/recoverable errors (user input, I/O); `panic!` for unrecoverable programmer bugs or invariant violations (e.g. out-of-bounds in logic you control).

## 17. HashMap entry API
How do you insert a value only if a key is absent?
?
**Answer:**
```rust
use std::collections::HashMap;
let mut m = HashMap::new();
*m.entry("k").or_insert(0) += 1;
```

## 18. iter vs into_iter vs iter_mut
What are the three iterator methods on collections?
?
**Answer:**
`iter()` yields `&T`, `iter_mut()` yields `&mut T`, `into_iter()` consumes the collection yielding `T` by value.

## 19. Closures and move
What does `move` do on a closure?
?
**Answer:**
It forces the closure to take ownership of captured variables (needed when moving data into a spawned thread):
```rust
let s = String::from("hi");
let c = move || println!("{s}");
```

## 20. Modules
How do Rust modules map to files, and what does `use` do?
?
**Answer:**
`mod foo;` looks for `foo.rs` or `foo/mod.rs`; `pub` makes items visible outside; `use path::to::item;` brings it into scope.

## 21. Read a file with ?
Write a function that reads a file into a String and propagates errors.
?
**Answer:**
```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
    fs::read_to_string(path)
}
```
Or with `?` if you need extra logic after the call.

## 22. Error handling with anyhow
Write a `main` that reads a config file and adds context to the error.
?
**Answer:**
```rust
use anyhow::{Result, Context};

fn main() -> Result<()> {
    let content = std::fs::read_to_string("config.toml")
        .with_context(|| "failed to read config.toml")?;
    println!("{content}");
    Ok(())
}
```

## 23. Word frequency counter
Count the frequency of each word in a sentence using a HashMap.
?
**Answer:**
```rust
use std::collections::HashMap;

let text = "the cat and the dog";
let mut counts: HashMap<&str, usize> = HashMap::new();
for word in text.split_whitespace() {
    *counts.entry(word).or_insert(0) += 1;
}
```

## 24. Parse JSON with serde
Parse a JSON string into a typed struct with serde.
?
**Answer:**
```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct Config { name: String, port: u16 }

let cfg: Config = serde_json::from_str(r#"{"name":"app","port":8080}"#)?;
```

## 25. Iterator chain
Given `Vec<i32>`, compute the sum of squares of the even elements using iterators.
?
**Answer:**
```rust
let nums = vec![1, 2, 3, 4, 5];
let total: i32 = nums.iter()
    .filter(|&&x| x % 2 == 0)
    .map(|&x| x * x)
    .sum();
```

## 26. Shared counter across threads
Increment a counter from 10 threads safely using Arc and Mutex.
?
**Answer:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];
for _ in 0..10 {
    let c = Arc::clone(&counter);
    handles.push(thread::spawn(move || {
        *c.lock().unwrap() += 1;
    }));
}
for h in handles { h.join().unwrap(); }
println!("{}", *counter.lock().unwrap());   // 10
```

## 27. Channels for parallelism
Spawn two threads that send values over a channel, then receive both.
?
**Answer:**
```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();
let tx2 = tx.clone();
thread::spawn(move || tx.send(42).unwrap());
thread::spawn(move || tx2.send(7).unwrap());
let a = rx.recv().unwrap();
let b = rx.recv().unwrap();
```

## 28. Recursive data structure
Define a linked-list style enum using Box. Why is Box needed?
?
**Answer:**
```rust
enum List { Cons(i32, Box<List>), Nil }
```
`Box` gives the enum a fixed, known size by moving the recursive part to the heap; without it the size would be infinite.

## 29. Trait objects
Store heterogeneous types implementing a common trait in one Vec and dispatch.
?
**Answer:**
```rust
trait Draw { fn draw(&self); }
struct Circle; impl Draw for Circle { fn draw(&self) {} }
struct Square; impl Draw for Square { fn draw(&self) {} }

let shapes: Vec<Box<dyn Draw>> = vec![Box::new(Circle), Box::new(Square)];
for s in &shapes { s.draw(); }
```

## 30. Generic function with trait bound
Write a generic function returning the largest element of a slice.
?
**Answer:**
```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut max = &list[0];
    for item in list {
        if item > max { max = item; }
    }
    max
}
```

## 31. Struct holding a reference
Define a struct that borrows a string slice, and explain the lifetime.
?
**Answer:**
```rust
struct Excerpt<'a> {
    part: &'a str,
}
```
`'a` ties the struct to the lifetime of the borrowed data so it can never outlive it.

## 32. Enum with data and match
Model a message type and write a handler that extracts each variant.
?
**Answer:**
```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}

fn handle(m: Message) -> String {
    match m {
        Message::Quit => "quit".into(),
        Message::Move { x, y } => format!("move to {x},{y}"),
        Message::Write(s) => s,
    }
}
```

## 33. Return impl Iterator
Write a function returning an iterator without naming its exact type.
?
**Answer:**
```rust
fn evens() -> impl Iterator<Item = i32> {
    (0..).map(|x| x * 2)
}
```

## 34. Build a small CLI with clap
Sketch a minimal `main` parsing a required `--name` argument with clap.
?
**Answer:**
```rust
use clap::Parser;

#[derive(Parser)]
struct Args {
    #[arg(short, long)]
    name: String,
}

fn main() {
    let args = Args::parse();
    println!("Hello, {}!", args.name);
}
```

## 35. Interior mutability with RefCell
Why use `RefCell`, and what check does it move to runtime?
?
**Answer:**
`RefCell` allows mutating data behind an immutable reference (interior mutability). Borrow checking happens at runtime via `borrow()`/`borrow_mut()`, panicking on double mutable borrow instead of failing at compile time.
