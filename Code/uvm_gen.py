import yaml
import shutil
from code import *

files = ["seq_item.sv", "sequence.sv", "sequencer.sv", "driver.sv", "monitor.sv", "agent.sv", "scoreboard.sv", "env.sv", "test.sv", "tbench_top.sv"]

directory = "uvm_files"

inp_yml = os.path.join("..", "uvm_input.yml")
with open(inp_yml, 'r') as f:
    config = yaml.safe_load(f)

tb        = config["Testbench"]
n_envs    = tb.get("Envs", 1)
n_agents  = tb.get("Agents", 1)
defaults  = tb.get("default_per_agent", {})
overrides = tb.get("overrides", {})

dir_path= os.path.join("..", directory)
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
    print(f"{dir_path} is deleted.")

#print(data)
os.makedirs(dir_path, exist_ok=True)

for e in range(n_envs):
    env_dir = os.path.join(dir_path, f"env{e}")
    os.makedirs(env_dir, exist_ok=True)
    env(config, env_dir, f"{config['File_Name']}_env_e{e}", e)

    for a in range(n_agents):
        ov = overrides.get(f"agent{a}", {})
        nd = ov.get("Drivers",    defaults.get("Drivers", 1))
        nm = ov.get("Monitors",   defaults.get("Monitors", 1))
        ns = ov.get("Sequencers", defaults.get("Sequencers", 1))

        #driver
        for i in range(nd):
            driver(config, env_dir, f"{config['File_Name']}_driver_e{e}_a{a}_{i}", i)

        #monitor
        for i in range(nm):
            monitor(config, env_dir, f"{config['File_Name']}_monitor_e{e}_a{a}_{i}", i)

        #sequence items, sequences, sequencers
        for i in range(ns):
            seq_gen(
                config, env_dir,
                f"{config['File_Name']}_seq_item_e{e}_a{a}_{i}",
                f"{config['File_Name']}_sequence_e{e}_a{a}_{i}",
                f"{config['File_Name']}_sequencer_e{e}_a{a}_{i}",e,a,i
            )

        agent(config, env_dir, f"{config['File_Name']}_agent_e{e}_a{a}")

    scoreboard(config, env_dir, f"{config['File_Name']}_scoreboard_e{e}", e)

test(config, dir_path, f"{config['File_Name']}_test.sv")
top(config, dir_path,  f"{config['File_Name']}_top.sv")




