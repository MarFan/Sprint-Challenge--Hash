#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trip = {}
    route = []

    # cache all tickets
    for t in tickets:
        if t.source not in trip:
            trip[t.source] = t.destination
            if t.source is 'NONE':
                route.append(t.destination)
    
    for i in range(0, length):       
        if len(route) == length:
            return route

        route.append(trip[route[i]])