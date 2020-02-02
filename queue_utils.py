import datetime

#updates all tickets.t_est_time in ticket_list relative to new position
def update_queue(ticket_list):
	tmp = ticket_list
	return [est_update() for ticket in tmp]

# calculates the average wait time, increments the number of patients served
# cur_time: time at the moment of the call minus the elapsed time of the session
def avg_wait(avg_service_time, n_served):
    cur_time = datetime.datetime.now() - datetime.timedelta(
        minutes=(n_served * avg_service_time))
    avg_service_time = (n_served * avg_service_time +
                        cur_time.minute) / (n_served + 1)
    return avg_service_time


def serve(avg_service_time, n_served, ticket_list):
    avg_service_time = avg_wait(avg_service_time, n_served)
    ticket_list.remove(ticket_list[0])
    n_served += 1
    return n_served, avg_service_time