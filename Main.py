import datetime

TICKET_LIST = []

# Average time in minutes
AVG_TIME = 1

NUM_SERVED = 0

CURRENT_ID = 0


# calculates the average wait time, increments the number of patients served
# cur_time: time at the moment of the call minus the elapsed time of the session
def avg_wait():
    global AVG_TIME
    global NUM_SERVED
    cur_time = datetime.datetime.now() - datetime.timedelta(
        minutes=(NUM_SERVED * AVG_TIME))
    AVG_TIME = (NUM_SERVED * AVG_TIME + cur_time) / (NUM_SERVED + 1)
    NUM_SERVED += 1


def serve():
    avg_wait()
    TICKET_LIST.remove(TICKET_LIST[0])
