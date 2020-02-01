from Main import *

class Ticket:

    # Instance attributes
    def __init__(self):

        global CURRENT_ID

        CURRENT_ID += 1

        # expensive route:
        self.t_id = CURRENT_ID
        TICKET_LIST.append(self.t_id)

    #iniitialize to estimated time start at t=end of queue
        global AVG_TIME
        self.est_update()

    # gives an updated eta for patient to be served
    # TICKET_LIST.getIndex(self.id) is new position of this ticket
    def est_update(self):
        global AVG_TIME
        self.t_est_time = TICKET_LIST.index(self.t_id) * AVG_TIME
    
    def quit(self):
        TICKET_LIST.remove(self.t_id)


if __name__ == "__main__":
    a = Ticket()
    b = Ticket()
    print(a.t_id)
    print(b.t_est_time)
    #a.quit()
    #b.quit()
    c = Ticket()
    print(TICKET_LIST)
    a.quit()
    #print(a.t_id)
    print(b.t_est_time)
    print(c.t_est_time)