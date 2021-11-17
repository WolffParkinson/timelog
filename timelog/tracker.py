import time

class Tracker():
    def __init__(self,title) -> None:
        self.logs:list[dict] = []
        self.title = title

        self.start_time = time.time()
        self.time_check = self.start_time

    def add_stop(self,name:str)->None:
        self.logs.append({"name":name,"delta":self.reset_clock()})

    def reset_clock(self)->float:
        stop = time.time() - self.time_check
        self.time_check = time.time()
        return stop

    def humanize(self,delta:float)->str:
        ms = delta * float(1000)

        if ms < 1:return "<1ms"
        else:return str(f"{round(ms)}ms")

    def print(self)->str:
        lb = "\n------------------------------------"
    
        output = lb + '\n' + 'EXECUTION LOG ::: {}'.format(self.title) + lb

        for log in self.logs:
            output+='\n• ' + log.get('name') + " ------ " + self.humanize(log.get('delta'))

        output += lb + '\nTOTAL\t:\t' + self.humanize(time.time()-self.start_time) + lb

        return output