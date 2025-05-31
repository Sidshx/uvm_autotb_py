// Environment: uart_env_e1)
class uart_env_e1 extends uvm_env;
    `uvm_component_utils(uart_env_e1)

// Constructor
function new(string name = "uart_env", uvm_component parent = null);
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

endclass : uart_env_e1