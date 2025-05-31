// Sequencer: uart_sequencer_e1_a1_0
class uart_sequencer_e1_a1_0 extends uvm_sequencer#(uart_seq_item_e1_a1_i0);
    `uvm_object_utils(uart_sequencer_e1_a1_0)

// Constructor
function new(string name = "uart_sequencer_e1_a1_0", uvm_component parent = null);
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

endclass : uart_sequencer_e1_a1_0
