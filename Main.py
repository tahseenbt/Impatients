import ticket
from functools import partial
from tkinter import Tk, Button, Label


def create_ticket(ticket_list):
    new_ticket = ticket.Ticket()
    ticket_list.append(new_ticket)
    ticket_list[-1].est_update(len(ticket_list) - 1)
    return new_ticket


def digital_ticket(ticket_list):
    def refresh_time_label():
        est_time_label.config(
            text="Estimated time: {0} minutes".format(new_ticket.avg_time))
        est_time_label.after(1000, refresh_time_label)

    new_ticket = create_ticket(ticket_list)
    ticket_window = Tk()
    ticket_window.title("Ticket {0}".format(new_ticket.t_id))
    ticket_window.geometry("200x200")

    est_time_label = Label(ticket_window,
                           text="Estimated time: {0} minutes".format(
                               new_ticket.t_est_time))
    est_time_label.pack(side="top")
    refresh_time_label()
    leave_btn = Button(ticket_window,
                       text="Leave queue",
                       bd="5",
                       command=combine_funcs(
                           partial(queue_quit, ticket_list,
                                   len(ticket_list) - 1),
                           ticket_window.destroy))
    leave_btn.pack(side="top")
    ticket_window.mainloop()


def queue_quit(ticket_list, ticket_idx):
    # todo list comprehension for all tickets after ticket_idx
    ticket_list.pop(ticket_idx)


def print_ticket(ticket_list):
    create_ticket(ticket_list)
    pass


def next_ticket(ticket_list):
    ticket_list.remove(ticket_list[0])
    current_ticket_label.config(
        text="Serving: {0}".format(str(ticket_list[0].t_id)))
    pass


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


# if __name__ == '__main__':

ticket_list = []

# Reception window
reception = Tk()
reception.title("Reception")
reception.geometry('200x200')

# label gets refreshed when ticket is served
current_ticket_label = Label(reception, text="Serving: 1")
current_ticket_label.pack(side="top")
next_ticket_btn = Button(reception,
                         text="Next ticket",
                         bd="5",
                         command=partial(next_ticket, ticket_list))
next_ticket_btn.pack(side="top")

# Kiosk window
kiosk = Tk()
kiosk.title("Kiosk")
kiosk.geometry('200x200')
print_btn = Button(kiosk,
                   text="Print ticket",
                   bd="5",
                   command=partial(print_ticket, ticket_list))
print_btn.pack(side="top")
digital_ticket_btn = Button(kiosk,
                            text="Digital ticket",
                            bd="5",
                            command=partial(digital_ticket, ticket_list))
digital_ticket_btn.pack(side="top")

# All mainloops here
reception.mainloop()
kiosk.mainloop()
