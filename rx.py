from mod import *   

class rx:
    
    __sys_clk = 0;
    def __init__(self):
        self.__sys_clk = False;
        self.mod_ = mod();
        
    def do_proc(self):
        for k in range(10):
            self.mod_.clk_toggle()

rx_ = rx();
rx_.do_proc();
