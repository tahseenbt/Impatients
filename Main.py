import datetime

TICKET_LIST = []

AVG_TIME = 0

NUM_SERVED = 0

#calculates the average wait time, increments the number of patients served
#cur_time: time at the moment of the call minus the elapsed time of the session
def AVG_WAIT()
    cur_time = datetime.datetime.now() - (NUM_SERVED + AVG_TIME) #note: convert to string?
    AVG_TIME = (NUM_SERVED* AVG_TIME + cur_time) / (NUM_SERVED + 1)
    NUM_SERVED+=1

def serve():
    avg_wait()
    TICKET_LIST.remove(0)
