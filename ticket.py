from Main import *

class Ticket:
    current_id = 1

    # Instance attributes
    def __init__(self):
        self.t_id = Ticket.current_id
        Ticket.current_id += 1

    """#iniitialize to estimated time start at t=end of queue
        global AVG_TIME
        self.est_update()

    # gives an updated eta for patient to be served
    # TICKET_LIST.getIndex(self.id) is new position of this ticket
    # TODO move to queue_utils? will decide
    def est_update(self):
        global AVG_TIME
        self.t_est_time = TICKET_LIST.index(self.t_id) * AVG_TIME
    
    # TODO move to queue_utils? will decide
    def quit(self):
        TICKET_LIST.remove(self.t_id)"""


if __name__ == "__main__":
    a = Ticket()
    b = Ticket()
    #a.quit()
    #b.quit()
    c = Ticket()
    print(a.t_id)
    #a.quit()
    print(b.t_id)