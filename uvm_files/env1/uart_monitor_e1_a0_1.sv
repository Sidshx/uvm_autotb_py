// Monitor: uart_monitor_e1_a0_1)
class uart_monitor_e1_a0_1 extends uvm_monitor;
    `uvm_object_utils(uart_monitor_e1_a0_1)

// Constructor
function new(string name = "uart_monitor_e1_a0_1", uvm_component parent = null);
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

endclass : uart_monitor_e1_a0_1
