#flashcards/languages/lua

## 1. local vs global
What is the difference between `local x = 5` and `x = 5` in Lua?
?
**Answer:**
`x = 5` creates a global (visible everywhere); `local x = 5` scopes it to the current block. Always use `local` to avoid pollution and get faster access.

## 2. Truthiness
Which values are falsy in Lua?
?
**Answer:**
Only `nil` and `false`. Everything else — including `0` and `""` — is truthy.

## 3. Types
List Lua's eight basic types.
?
**Answer:**
`nil`, `boolean`, `number`, `string`, `function`, `table`, `userdata`, `thread`. Check with `type(x)`.

## 4. String concatenation
How do you concatenate strings, and what is `#s`?
?
**Answer:**
`..` concatenates; `#s` gives the length:
```lua
local s = "hello" .. " " .. "world"   -- "hello world"
local n = #s                           -- 11
```

## 5. Tables as arrays
How are Lua tables indexed when used as arrays, and how do you get the length?
?
**Answer:**
Arrays are 1-indexed (not 0). `#t` returns the length of the array part:
```lua
local a = {10, 20, 30}
print(a[1])   -- 10
print(#a)     -- 3
```

## 6. Tables as dictionaries
Create a table with string keys and access its fields two ways.
?
**Answer:**
```lua
local p = { name = "Alice", age = 30 }
print(p.name)      -- Alice
print(p["name"])   -- Alice
```

## 7. ipairs vs pairs
When do you use `ipairs` vs `pairs`?
?
**Answer:**
`ipairs` iterates the array part in order (stops at first `nil`); `pairs` iterates all key/value pairs in arbitrary order.

## 8. Multiple return values
How do functions return multiple values, and how do you capture them?
?
**Answer:**
```lua
local function divmod(a, b) return a // b, a % b end
local q, r = divmod(7, 3)   -- q=2, r=1
```

## 9. Variadic functions
How do you accept a variable number of arguments in Lua?
?
**Answer:**
Use `...`, packed into a table with `{...}`:
```lua
local function sum(...)
    local t = 0
    for _, v in ipairs({...}) do t = t + v end
    return t
end
```

## 10. and/or as defaults
How does `local x = input or "default"` work?
?
**Answer:**
`or` returns its operands (not just booleans): if `input` is truthy it's returned, otherwise the default. `and`/`or` are used for defaults and ternary-like expressions.

## 11. Numeric for loop
Write the three forms of the numeric `for` loop.
?
**Answer:**
```lua
for i = 1, 10 do end          -- 1..10
for i = 1, 10, 2 do end       -- step 2
for i = 10, 1, -1 do end      -- count down
```

## 12. Integer division
How do you do integer (floor) division and modulus in Lua?
?
**Answer:**
`a // b` is floor division, `a % b` is modulus (result follows Lua's floor convention).

## 13. Metatables
What is a metatable and what does `setmetatable` do?
?
**Answer:**
A table that changes how another table behaves (via metamethods like `__index`, `__add`, `__call`). `setmetatable(t, mt)` attaches it.

## 14. __index
What does `__index` do and how is it used to build "classes"?
?
**Answer:**
`__index` provides a fallback for missing keys. Pointing it at a method table simulates inheritance: instances look up methods on the metatable.

## 15. Colon syntax
What is the difference between `obj:method(x)` and `obj.method(x)`?
?
**Answer:**
The colon passes `self` implicitly: `obj:method(x)` == `obj.method(obj, x)`. Use `:` to define/call methods.

## 16. require
How do modules work with `require`, and what does it return?
?
**Answer:**
A module is a table returned by a file; `require("name")` loads it once, caches it, and returns the table.

## 17. pcall
How do you call a function that may raise an error without crashing?
?
**Answer:**
```lua
local ok, result = pcall(function() error("boom") end)
if not ok then print("caught: " .. result) end
```

## 18. error and assert
What do `error(msg)` and `assert(v, msg)` do?
?
**Answer:**
`error(msg)` raises an error. `assert(v, msg)` raises with `msg` if `v` is falsy, otherwise returns `v`.

## 19. Operator metamethods
How do you overload `+` for a vector type?
?
**Answer:**
```lua
function Vector.__add(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end
-- now v1 + v2 works
```

## 20. Build a simple class
Write a minimal "class" with a constructor and a method using metatables.
?
**Answer:**
```lua
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable({x = x, y = y}, Vector)
end

function Vector:length()
    return math.sqrt(self.x^2 + self.y^2)
end

local v = Vector.new(3, 4)
print(v:length())   -- 5
```

## 21. Word count with a table
Count word frequencies in a string using a table.
?
**Answer:**
```lua
local counts = {}
for w in (text .. " "):gmatch("(%S+)") do
    counts[w] = (counts[w] or 0) + 1
end
```

## 22. String pattern matching
Extract all numbers from a string using `string.gmatch`.
?
**Answer:**
```lua
for n in s:gmatch("%d+") do
    print(tonumber(n))
end
```

## 23. Sort a list
Sort an array of strings by length using `table.sort`.
?
**Answer:**
```lua
table.sort(words, function(a, b) return #a < #b end)
```

## 24. Config module
Write a small module that loads and returns a config table.
?
**Answer:**
```lua
-- config.lua
local M = { host = "localhost", port = 8080 }
function M.get() return M end
return M
```
```lua
-- main.lua
local cfg = require("config")
print(cfg.host, cfg.port)
```

## 25. Callable table
Make a table callable like a function using `__call`.
?
**Answer:**
```lua
local doubler = setmetatable({}, {
    __call = function(self, x) return x * 2 end
})
print(doubler(21))   -- 42
```

## 26. Guarded table writes
Intercept writes to a table with `__newindex`.
?
**Answer:**
```lua
local t = setmetatable({}, {
    __newindex = function(tbl, k, v)
        print("set " .. k .. " = " .. v)
        rawset(tbl, k, v)
    end
})
```

## 27. Coroutine basics
Write a producer/consumer coroutine that yields values.
?
**Answer:**
```lua
local co = coroutine.create(function()
    for i = 1, 3 do coroutine.yield(i) end
end)
print(coroutine.resume(co))   -- true, 1
print(coroutine.resume(co))   -- true, 2
```

## 28. C API: run a Lua string
Write a minimal C program that runs a Lua chunk.
?
**Answer:**
```c
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>
int main(void) {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    luaL_dostring(L, "print('hello')");
    lua_close(L);
    return 0;
}
```

## 29. C API: register a function
Expose a C function `add(a,b)` to Lua.
?
**Answer:**
```c
static int l_add(lua_State *L) {
    double a = luaL_checknumber(L, 1);
    double b = luaL_checknumber(L, 2);
    lua_pushnumber(L, a + b);
    return 1;                    // one return value
}
// in init: lua_register(L, "add", l_add);
```

## 30. Read-only table
Build a table whose keys can be read but not written.
?
**Answer:**
```lua
local readonly = setmetatable({x = 1}, {
    __newindex = function() error("read-only") end
})
```

## 31. Deep default values
Use `__index` as a function to return a computed default for missing keys.
?
**Answer:**
```lua
local t = setmetatable({}, {
    __index = function(tbl, key) return "missing: " .. key end
})
print(t.foo)   -- missing: foo
```
