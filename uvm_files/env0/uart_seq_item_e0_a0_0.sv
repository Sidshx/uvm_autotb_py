// Sequence Item: uart_seq_item_e0_a0_0
class uart_seq_item_e0_a0_0 extends uvm_sequence_item;

    `uvm_object_utils(uart_seq_item_e0_a0_0)

// Constructor
function new(string name = "uart_seq_item_e0_a0_0", uvm_component parent = null);
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

endclass : uart_seq_item_e0_a0_0
