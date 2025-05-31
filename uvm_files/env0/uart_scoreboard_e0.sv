// Scoreboard: uart_scoreboard_e0)
class uart_scoreboard_e0 extends uvm_scoreboard;
    `uvm_component_utils(uart_scoreboard_e0)

// Constructor
function new(string name = "uart_scoreboard_e0", uvm_component parent = null);
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

endclass : uart_scoreboard_e0
