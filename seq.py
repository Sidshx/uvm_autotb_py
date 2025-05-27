import os

def seq_gen(config, directory, seq_item, seq, seqr):

    item_path =  os.path.join(directory, seq_item)
    seq_path = os.path.join(directory, seq)
    seqr_path = os.path.join(directory, seqr)

    with open(item_path, "w") as f:
        f.write(f"""// Sequence Item: {seq_item}
class {config['File_Name']}_seq_item extends uvm_sequence_item;
    `uvm_object_utils({config['File_Name']}_seq_item)

endclass : {config['File_Name']}_seq_item) 
""")
        print(f"Generated: {config['File_Name']}_seq_item.sv")

    with open(seq_path, "w") as f:
        f.write(f"""// Sequence: {seq}
class {config['File_Name']}_sequence extends uvm_sequence;
    `uvm_object_utils({config['File_Name']}_sequence)

endclass : {config['File_Name']}_sequence)
""")
        print(f"Generated: {config['File_Name']}_sequence.sv")

    with open(seqr_path, "w") as f:
        f.write(f"""// Sequencer: {seqr}
class {config['File_Name']}_sequencer extends uvm_sequencer#({config['File_Name']}_seq_item);
    `uvm_object_utils({config['File_Name']}_sequencer)

endclass : {config['File_Name']}_sequencer)
""")
        print(f"Generated: {config['File_Name']}_sequencer.sv")

def driver(config, directory, f_name):

    drv_path = os.path.join(directory, f_name)

    with open(drv_path, "w") as f:
        f.write(f"""// Driver: {f_name})
class {config['File_Name']}_driver extends uvm_driver#({config['File_Name']}_seq_item);
    `uvm_object_utils({config['File_Name']}_driver)

endclass : {config['File_Name']}_driver
""")
        print(f"Generated: {config['File_Name']}_driver.sv")

def monitor(config, directory, f_name):

    mon_path = os.path.join(directory, f_name)

    with open(mon_path, "w") as f:
        f.write(f"""// Monitor: {f_name})
class {config['File_Name']}_monitor extends uvm_monitor;
    `uvm_object_utils({config['File_Name']}_monitor)

endclass : {config['File_Name']}_monitor
""")
        print(f"Generated: {config['File_Name']}_monitor.sv")

def agent(config, directory, f_name):

    agent_path = os.path.join(directory, f_name)

    with open(agent_path, "w") as f:
        f.write(f"""// Agent: {f_name})
class {config['File_Name']}_agent extends uvm_agent;
    `uvm_component_utils({config['File_Name']}_agent)

endclass : {config['File_Name']}_agent
""")
        print(f"Generated: {config['File_Name']}_agent.sv")

def scoreboard(config, directory, f_name):

    scb_path = os.path.join(directory, f_name)

    with open(scb_path, "w") as f:
        f.write(f"""// Scoreboard: {f_name})
class {config['File_Name']}_scoreboard extends uvm_scoreboard;
    `uvm_component_utils({config['File_Name']}_scoreboard)

endclass : {config['File_Name']}_agent
""")
        print(f"Generated: {config['File_Name']}_scoreboard.sv")

def env(config, directory, f_name):

    env_path = os.path.join(directory, f_name)

    with open(env_path, "w") as f:
        f.write(f"""// Environment: {f_name})
class {config['File_Name']}_env extends uvm_env;
    `uvm_component_utils({config['File_Name']}_env)

endclass : {config['File_Name']}_env
""")
        print(f"Generated: {config['File_Name']}_env.sv")

def test(config, directory, f_name):

    test_path = os.path.join(directory, f_name)

    with open(test_path, "w") as f:
        f.write(f"""// Test: {f_name})
class {config['File_Name']}_test extends uvm_test;
    `uvm_object_utils({config['File_Name']}_test)

endclass : {config['File_Name']}_test
""")
        print(f"Generated: {config['File_Name']}_test.sv")

def top(config, directory, f_name):

    top_path = os.path.join(directory, f_name)

    with open(top_path, "w") as f:
        f.write(f"""// TBench Top: {f_name})
module tbench_top;
   
endmodule : tbench_top
""")
        print(f"Generated: tbench_top.sv")

