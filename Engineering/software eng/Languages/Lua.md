# Lua

Lightweight, embeddable scripting language. Single small interpreter, trivial to embed in C/C++ (games, Neovim, Redis, nginx...). One data structure — the **table** — does everything (arrays, maps, objects, modules).

## Running Lua

```bash
lua script.lua      # run a script
luajit script.lua   # JIT interpreter (much faster, optional)
```

Or the REPL: `lua` then type code.

## Values and types

Types: `nil`, `boolean`, `number` (double by default), `string`, `function`, `table`, `userdata`, `thread`.

Only `nil` and `false` are falsy (even `0` and `""` are truthy).

```lua
local a = 10          -- number
local b = 3.14
local s = "hello"
local s2 = 'world'
local multiline = [[
multiple
lines
]]
local n = nil         -- "no value"
```

Variables are **global by default**; `local` makes them scoped (always use `local`).

```lua
x = 5          -- global (bad practice)
local y = 5    -- local
```

## Strings

Concatenation is `..`, length is `#`.

```lua
local s = "hello" .. " " .. "world"   -- "hello world"
local len = #s                        -- 11
local up = string.upper(s)            -- "HELLO WORLD"
local sub = string.sub(s, 1, 5)       -- "hello"
local found = string.find(s, "world") -- start index or nil
```

Numbers auto-coerce in arithmetic, but not in `..`:

```lua
print("10" + 1)     -- 11
print(10 .. 20)     -- "1020" (numbers coerced to string by ..)
```

## Tables (the one structure)

Tables are both **arrays** (1-indexed) and **dictionaries** at once.

```lua
-- as array (1-indexed!)
local arr = {10, 20, 30}
print(arr[1])        -- 10   (NOT 0-indexed)
print(#arr)          -- 3    (length)

-- as dictionary
local person = { name = "Alice", age = 30 }
print(person.name)   -- Alice
print(person["name"]) -- Alice

-- mixed
local t = {1, 2, x = 5, y = 6}

-- add / remove
table.insert(arr, 40)         -- append
table.insert(arr, 2, 15)      -- insert at index 2
table.remove(arr)             -- pop last
table.remove(arr, 1)          -- remove at index 1
```

Iterating:

```lua
-- ipairs: array part, in order
for i, v in ipairs(arr) do
    print(i, v)
end

-- pairs: ALL key/value pairs, unordered
for k, v in pairs(t) do
    print(k, v)
end
```

## Functions

Functions are first-class values. Can return multiple values.

```lua
local function add(a, b)
    return a + b
end

-- multiple returns
local function divmod(a, b)
    return a // b, a % b
end
local q, r = divmod(7, 3)    -- q=2, r=1

-- variadic functions use ...
local function sum(...)
    local total = 0
    for _, v in ipairs({...}) do total = total + v end
    return total
end

-- functions as values
local f = add
print(f(1, 2))
```

## Control flow

```lua
if x > 0 then
    print("positive")
elseif x < 0 then
    print("negative")
else
    print("zero")
end

-- while
local i = 0
while i < 5 do
    i = i + 1
end

-- repeat ... until
repeat
    i = i - 1
until i == 0

-- numeric for (inclusive, optional step)
for i = 1, 10 do print(i) end
for i = 10, 1, -1 do print(i) end

-- logical operators: and, or, not
local x = a and b or c
```

`and`/`or` return their operands (not just booleans), enabling defaults:

```lua
local name = input or "default"
```

## Metatables (object system)

A metatable changes how a table behaves: `__index`, `__newindex`, operator overloads, etc.

```lua
-- __index: fallback lookup (basis for "classes")
local meta = {}
meta.__index = function(tbl, key)
    return key .. " not found"
end
setmetatable(t, meta)

-- operator overloads
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable({x = x, y = y}, Vector)
end

function Vector:add(other)     -- ':' passes self implicitly
    return Vector.new(self.x + other.x, self.y + other.y)
end

function Vector.__add(a, b)    -- overload '+'
    return Vector.new(a.x + b.x, a.y + b.y)
end

local v1 = Vector.new(1, 2)
local v2 = Vector.new(3, 4)
local v3 = v1 + v2             -- uses __add
```

## Modules (`require`)

A module is a table returned by a file.

```lua
-- mymodule.lua
local M = {}
function M.greet(name) return "Hello " .. name end
return M
```

```lua
-- main.lua
local mod = require("mymodule")
print(mod.greet("Alice"))
```

`require` caches modules — each is loaded only once.

## Error handling

```lua
error("something went wrong")     -- raise an error

-- pcall: protected call, returns (ok, result)
local ok, result = pcall(function()
    error("boom")
end)
if not ok then
    print("caught: " .. result)   -- result holds the error message
end

-- assert
local v = assert(tonumber("42"), "not a number")
```

## Advanced (still everyday-relevant)

### C API (embedding/extending)

Lua communicates with C through a **stack** (`lua_State`).

```c
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

int main(void) {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);                       // load std libs

    luaL_dostring(L, "print('hello from lua')");

    // push a value and run a chunk
    luaL_loadfile(L, "script.lua");
    lua_pcall(L, 0, 0, 0);

    lua_close(L);
    return 0;
}
```

Registering a C function to Lua:

```c
static int l_add(lua_State *L) {
    double a = luaL_checknumber(L, 1);
    double b = luaL_checknumber(L, 2);
    lua_pushnumber(L, a + b);
    return 1;                               // number of return values
}

lua_register(L, "add", l_add);              // now callable from Lua as add(a, b)
```

Compile/link: `cc -o app app.c -llua -lm` (or `-llua5.4`).

### `__newindex` and `__call`

```lua
-- __newindex: intercept writes
local guarded = setmetatable({}, {
    __newindex = function(t, k, v)
        print("write to " .. k .. " = " .. v)
        rawset(t, k, v)
    end
})

-- __call: make a table callable like a function
local callable = setmetatable({}, {
    __call = function(self, x) return x * 2 end
})
print(callable(21))   -- 42
```

### Coroutines (cooperative multitasking)

```lua
local co = coroutine.create(function(a)
    local b = coroutine.yield(a + 1)   -- pause, return a+1
    return a + b
end)

local status, val = coroutine.resume(co, 10)  -- val = 11
coroutine.resume(co, 20)                      -- b = 20, function returns 30
```

### Gotchas

- Arrays are **1-indexed** (not 0).
- Variables are global unless `local`.
- `#` on a table with holes is unreliable; only use it on proper arrays.
- `..` does not coerce numbers automatically when mixed with strings on the left? It does coerce numbers — but prefer `tostring` for clarity.
- Default integer division: `//` (floor), remainder `%`.

## Links

[[C_ANSI]]
[[C_GNU]]
