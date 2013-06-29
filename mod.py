class mod:
    
    def __init__(self):
        self.__sys_clk = False;
        self.__counter = 0;
        
        self.input_valid;
        self.output_valid;
        
    def clk_toggle(self):
        self.__sys_clk = not self.__sys_clk;
        
        if self.__sys_clk:
            self.__do_proc();
            
    def __do_proc(self):
        self.__counter = self.__counter + 1;
        print self.__counter;
        
        

