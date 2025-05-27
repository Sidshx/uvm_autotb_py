import os
import yaml

with open('uvm_input.yml', 'r') as f:
    config = yaml.safe_load(f)

directory = "uvm_files"

files = ["seq_item.sv", "sequence.sv", "sequencer.sv", "driver.sv", "monitor.sv", "agent.sv", "scoreboard.sv", "env.sv", "test.sv", "tbench_top.sv"]

def file_check(uvm_files, files):

    for name in files:
        path = os.path.join(uvm_files, f"{config['File_Name']}_{name}")
        print(path)
        if os.path.exists(path):
            os.remove(path)
            print(f"Deleted: {path}")
    print("Ready for generating files!")
         
   
