# UVM AutoTB Python Generator

Automatically generate UVM testbench skeleton files using Python and a YAML configuration.

## Project Structure

| File/Folder      | Description |
|------------------|-------------|
| `code.py`        | Generates UVM SystemVerilog code based on parsed config |
| `func.py`        | Helper functions used across the project |
| `uvm_gen.py`     | Main script to drive generation |
| `uvm_input.yml`  | Configuration file defining components and naming |
| `uvm_files/`     | Output directory containing all generated UVM files |

## How to Use

```bash
git clone git@github.com:Sidshx/uvm_autotb_py.git
cd uvm_autotb_py
//Change the configurations as required in YAML file\
cd Code
python uvm_gen.py
```
## Features

- YAML-driven generation
- Supports all essential UVM components:
  - Sequence Item
  - Sequence
  - Sequencer
  - Driver
  - Monitor
  - Agent
  - Scoreboard
  - Environment
  - Test
  - Top-level testbench
- Modular and extendable design

## Reference

Based on the UVM Testbench Architecture from:  
[Verification Guide – UVM Testbench Architecture](https://verificationguide.com/uvm/uvm-testbench-architecture/)
