import yaml
from func import *

files = ["uvm_seq_item.sv", "uvm_sequence.sv", "uvm_sequencer.sv", "uvm_driver.sv", "uvm_monitor.sv", "uvm_agent.sv", "uvm_scoreboard.sv", "uvm_env.sv", "uvm_test.sv", "tbench_top.sv"]

with open('uvm_input.yml', 'r') as f:
    data = yaml.safe_load(f)

#print(data)
directory = "uvm_files"
os.makedirs(directory, exist_ok=True)

file_check(directory, files)

for name in files:
    path = os.path.join(directory, name)
    f = open(path, "x")
    f.write(f"//File Name: {name}\n")
    print(f"Created: {path}")
