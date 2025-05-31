// Agent: uart_agent_e0_a0)
class uart_agent_e0_a0 extends uvm_agent;
    `uvm_component_utils(uart_agent_e0_a0)

// Constructor
function new(string name = "uart_agent_e0_a0", uvm_component parent = null);
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

endclass : uart_agent_e0_a0
