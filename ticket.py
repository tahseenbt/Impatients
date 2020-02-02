from Main import *
import datetime

class Ticket:
    current_id = 1
    avg_time = 1
    num_served = 0

    # Instance attributes
    def __init__(self):
        self.t_id = Ticket.current_id
        Ticket.current_id += 1
        self.t_est_time = 3

    # gives an updated eta for patient to be served
    # TICKET_LIST.getIndex(self.id) is new position of this ticket
    def est_update(self, i):
        self.t_est_time = (i+1) * avg_time
    
    def quit(self):
        TICKET_LIST.remove(self.t_id)


if __name__ == "__main__":
    a = Ticket()
    b = Ticket()
    #a.quit()
    #b.quit()
    c = Ticket()
    print(c.t_id)
    #a.quit()
    #print(b.t_id)