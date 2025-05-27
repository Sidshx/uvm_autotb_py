import yaml
from func import *
from seq import *


#print(data)
os.makedirs(directory, exist_ok=True)

file_check(directory, files)

for name in files:
    path = os.path.join(directory, f"{config['File_Name']}_{name}")
    f = open(path, "x")
    f.write(f"//File Name: {config['File_Name']}_{name}\n")
    print(f"Created: {path}")

seq_gen(config, directory, f"{config['File_Name']}_seq_item.sv", f"{config['File_Name']}_seq.sv", f"{config['File_Name']}_seqr.sv")
driver(config, directory, f"{config['File_Name']}_driver.sv")
monitor(config, directory, f"{config['File_Name']}_monitor.sv")
agent(config, directory, f"{config['File_Name']}_agent.sv")
scoreboard(config, directory, f"{config['File_Name']}_scoreboard.sv")
env(config, directory, f"{config['File_Name']}_env.sv")
test(config, directory, f"{config['File_Name']}_test.sv")
top(config, directory, f"tbench_top.sv")





