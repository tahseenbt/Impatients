from Main import *

class Ticket:

    # Instance attributes
    def __init__(self):
        
        # expensive route:
        if len(TICKET_LIST) == 0:
            self.t_id = 1
        else:
            self.t_id = TICKET_LIST[-1]+1


if __name__ == "__main__":
    a = Ticket()
    print(a.t_id)
