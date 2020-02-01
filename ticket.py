from Main import *

class Ticket:

    # Instance attributes
    def __init__(self):

        global CURRENT_ID

        CURRENT_ID += 1

        # expensive route:
        self.t_id = CURRENT_ID
        TICKET_LIST.append(self.t_id)

        
    
    def quit(self):
        TICKET_LIST.remove(self.t_id)


if __name__ == "__main__":
    a = Ticket()
    b = Ticket()
    print(a.t_id)
    print(b.t_id)
    a.quit()
    b.quit()
    c = Ticket()
    print(TICKET_LIST)
    print(a.t_id)
    print(b.t_id)
    print(c.t_id)