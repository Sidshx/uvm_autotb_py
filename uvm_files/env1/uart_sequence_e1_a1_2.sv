// Sequence: uart_sequence_e1_a1_2
class uart_sequence_e1_a1_2 extends uvm_sequence;
    `uvm_object_utils(uart_sequence_e1_a1_2)

// Constructor
function new(string name = "uart_sequence_e1_a1_2", uvm_component parent = null);
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

endclass : uart_sequence_e1_a1_2
