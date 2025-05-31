// Test: uart_test.sv)
class uart_test extends uvm_test;
    `uvm_object_utils(uart_test)

// Constructor
function new(string name = "uart_test", uvm_component parent = null);
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

endclass : uart_test
