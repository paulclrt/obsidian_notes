
To make this very simple at first, lets make an OR gate:
We need two files:
- the component (to code the behavior)
- a test bench (to simulate the component and test it)

### Write the component logic
`orgate.vhd`:
```VHDL
-- Import libraries
library IEEE;
use IEEE.std_logic_1164.ALL;
use IEEE.numeric_std.ALL;

-- create the entity (inputs/outputs): kinda function definition
entity OR_gate is
	Port(
		a: in std_logic;
		b: in std_logic;
		q: out std_logic
	);
end entity OR_gate;

-- architecture (code the behavior): kinda function body
architecture rtl of OR_gate is
begin
	process(a, b) is
	begin
		q <= a or b; 
	end process;
end architecture rtl;

```

### Write the test bench for the component
Now you need the testbench
`tb_orgate.vhd`:
```VHDL
-- Import libraries
library IEEE;
use IEEE.std_logic_1164.ALL;
use IEEE.numeric_std.ALL;

-- define the entity (the function definition kinda like .h file but empty)
entity tb_orggate is
end entity;

-- DUT component (Design under test)
architecture rtl of tb_orgate is
--define the component again here (just the definition)
component OR_gate is
port(
	a: in std_logic;
	b: in std_logic;
	q: out std_logic
);
end component;

-- "variables " used to drive input and check outputs
signal a_in, b_in, o_out: std_logic;

-- write the driver logic (control the inputs and then simulation will show the outputs)
begin
	-- connect your signals ("variables") to the component under test
	DUT: OR_gate port map(a_in, b_in, o_out);
	
	--write your test
	process
	begin
		a_in <= '0';
		b_in <= '0';
		wait for 1 ns;
		assert(o_out='0') report "Fail 0/0" severity error;
		
		a_in <= '0';
	    b_in <= '1';
	    wait for 1 ns;
	    assert(q_out='1') report "Fail 0/1" severity error;
	
	    a_in <= '1';
	    b_in <= 'X';
	    wait for 1 ns;
	    assert(q_out='1') report "Fail 1/X" severity error;
	
	    a_in <= '1';
	    b_in <= '1';
	    wait for 1 ns;
	    assert(q_out='1') report "Fail 1/1" severity error;
		
		-- clear inputs
		a_in <= '0';
		b_in <= '0';
		
		assert false report "Test done." severity note;
		wait;
	end process;
end rtl;

```

## Compiling & simulating
You now need to compile the entity and then the testbench. Use [GHDL](http://ghdl.free.fr/) (Gnu compiler & simulator).

```
sudo apt/dnf install ghdl gtkwave
```

```bash
# 1. Analyze (compile) the VHDL source files
ghdl -a orgate.vhd
ghdl -a tb_orgate.vhd
```

```bash
# 2. Elaborate the testbench top-level entity
ghdl -e tb_orgate
```

```bash
# 3. Run the simulation and export waveforms to a VCD file 
ghdl -r orgate_tb --vcd=waveform.vcd
```

This last command should run the simulation; print the asserts results and create a `waveform.vcd` file that you can open with gtk wave.
## View the simulation results graphicaly with GTKwave

```bash
gtkwave waveform.vcd
```

![[gtkwave_screenshot.png]]

> Asserts are the way to test the design you wrote, the waveform is practical for debugging.

## Bonus: Writing code snipets and sharing them
[EdaPlayground](https://www.edaplayground.com/s/example/615) has a nice interface that allows you to write simple and complex hdl code and share them with other as well as to run them. 
This is practical when you don't have a toolchain setup and no rights on the machine.

![[edaplayground.png]]