// Driver: uart_driver_e1_a0_3)
class uart_driver_e1_a0_3 extends uvm_driver#(uart_seq_item_3);
    `uvm_object_utils(uart_driver_e1_a0_3)

// Constructor
function new(string name = "uart_driver_e1_a0_3", uvm_component parent = null);
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

endclass : uart_driver_e1_a0_3
