import os

# Testbench parameters
def seq_gen(config, directory, seq_item, seq, seqr, e,a,i):

    item_path =  os.path.join(directory, f"{seq_item}.sv")
    seq_path = os.path.join(directory, f"{seq}.sv")
    seqr_path = os.path.join(directory, f"{seqr}.sv")

    with open(item_path, "w") as f:
        f.write(f"""// Sequence Item: {seq_item}
class {seq_item} extends uvm_sequence_item;

    `uvm_object_utils({seq_item})

// Constructor
function new(string name = "{seq_item}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
endfunction

// Run phase
task run_phase(uvm_phase phase);
    super.run_phase(phase);
endtask

endclass : {seq_item}
""")
        print(f"Generated {seq_item}")

    with open(seq_path, "w") as f:
        f.write(f"""// Sequence: {seq}
class {seq} extends uvm_sequence;
    `uvm_object_utils({seq})

// Constructor
function new(string name = "{seq}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
endfunction

// Run phase
task run_phase(uvm_phase phase);
    super.run_phase(phase);
endtask

endclass : {seq}
""")
        print(f"Generated {seq}")

    with open(seqr_path, "w") as f:
        f.write(f"""// Sequencer: {seqr}
class {seqr} extends uvm_sequencer#({config['File_Name']}_seq_item_e{e}_a{a}_i{i});
    `uvm_object_utils({seqr})

// Constructor
function new(string name = "{seqr}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
endfunction

endclass : {seqr}
""")
        print(f"Generated {seqr}")

def driver(config, directory, f_name, n):

    drv_path = os.path.join(directory, f"{f_name}.sv")

    with open(drv_path, "w") as f:
        f.write(f"""// Driver: {f_name})
class {f_name} extends uvm_driver#({config['File_Name']}_seq_item_{n});
    `uvm_object_utils({f_name})

// Constructor
function new(string name = "{f_name}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
endfunction

// Run phase
task run_phase(uvm_phase phase);
    super.run_phase(phase);
endtask

endclass : {f_name}
""")
        print(f"Generated {f_name}")

def monitor(config, directory, f_name, n):

    mon_path = os.path.join(directory, f"{f_name}.sv")

    with open(mon_path, "w") as f:
        f.write(f"""// Monitor: {f_name})
class {f_name} extends uvm_monitor;
    `uvm_object_utils({f_name})

// Constructor
function new(string name = "{f_name}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
endfunction

// Run phase
task run_phase(uvm_phase phase);
    super.run_phase(phase);
endtask

endclass : {f_name}
""")
        print(f"Generated {f_name}")

def agent(config, directory, f_name):

    agent_path = os.path.join(directory, f"{f_name}.sv")

    with open(agent_path, "w") as f:
        f.write(f"""// Agent: {f_name})
class {f_name} extends uvm_agent;
    `uvm_component_utils({f_name})

// Constructor
function new(string name = "{f_name}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // TODO: create driver, monitor, sequencer
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    // TODO: connect analysis and sequencer ports
endfunction

endclass : {f_name}
""")
        print(f"Generated {f_name}")

def scoreboard(config, directory, f_name, n):

    scb_path = os.path.join(directory, f"{f_name}.sv")

    with open(scb_path, "w") as f:
        f.write(f"""// Scoreboard: {f_name})
class {f_name} extends uvm_scoreboard;
    `uvm_component_utils({f_name})

// Constructor
function new(string name = "{f_name}", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // TODO: create analysis ports
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    // TODO: connect inputs to analysis ports
endfunction

endclass : {f_name}
""")
        print(f"Generated {f_name}")

def env(config, directory, f_name, n):

    env_path = os.path.join(directory, f"{f_name}.sv")

    with open(env_path, "w") as f:
        f.write(f"""// Environment: {f_name})
class {f_name} extends uvm_env;
    `uvm_component_utils({f_name})

// Constructor
function new(string name = "{config['File_Name']}_env", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // TODO: create agents and scoreboard
endfunction

// Connect phase
function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    // TODO: connect agents to scoreboard
endfunction

endclass : {f_name}""")
        print(f"Generated a {config['File_Name']}_env")

def test(config, directory, f_name):

    test_path = os.path.join(directory, f_name)

    with open(test_path, "w") as f:
        f.write(f"""// Test: {f_name})
class {config['File_Name']}_test extends uvm_test;
    `uvm_object_utils({config['File_Name']}_test)

// Constructor
function new(string name = "{config['File_Name']}_test", uvm_component parent = null);
    super.new(name, parent);
endfunction

// Build phase
function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // TODO: set up default sequencer and start sequence
endfunction

// Run phase
task run_phase(uvm_phase phase);
    super.run_phase(phase);
    // TODO: start sequence
endtask

endclass : {config['File_Name']}_test
""")
        print(f"Generated a {config['File_Name']}_test.sv")

def top(config, directory, f_name):

    top_path = os.path.join(directory, f_name)

    with open(top_path, "w") as f:
        f.write(f"""// TBench Top: {f_name})
module tbench_top;
    import uvm_pkg::*;

    initial begin
        run_test();


    end

endmodule : tbench_top
""")
        print(f"Generated a tbench_top")

