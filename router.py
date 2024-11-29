from math import inf

class Router:

    def __init__(self, name, ip_address):
        self.name = name
        self.address = ip_address
        self.neighbors = []
        self.paths : dict = {} # paths[router] = [gateway,distance]
        self.received_paths = {} # buffer which stores the unprocessed paths received from other neighbors

    def add_neighbor(self, r : 'Router', d : int = 1):
        """
        Adds router r as neighbor with distance d.
        """
        assert(r != self)
        self.neighbors.append(r)
        self.paths[r] = [r,d]

    def send(self):
        """
        Sends the path to all neighbors
        """
        for neighbor in self.neighbors:
            neighbor.recv(self, {destination : route for destination,route in self.paths.items() if route[0] != neighbor and destination != neighbor}) # split horizon

    def recv(self, sender : 'Router', paths : dict):
        """
        Receives paths from neighbor sender.
        """
        assert(sender in self.neighbors)
        self.received_paths[sender] = paths

    def update(self):
        """
        Updates the routing informations based on the stored received paths.
        """
        for sender,paths in self.received_paths.items():
            for destination,route in paths.items():
                assert(destination != self)
                neighbor_gateway,distance = route
                distance_from_sender = self.paths[sender][1]
                gateway = self.paths[sender][0] # the gateway is not necessarily the sender, but the neighbor which has the shortest path to the sender
                new_distance = distance_from_sender + distance # possible new distance to destination
                if destination not in self.paths: # unknown destination
                    self.paths[destination] = [gateway,new_distance]
                else:
                    current_distance = self.paths[destination][1] # current distance to destination
                    if current_distance > new_distance:
                        self.paths[destination] = [gateway,new_distance]
        self.received_paths = {} # clear the buffer

    def __str__(self):
        return self.name + " (" + self.address + ")"
    
    def __repr__(self):
        return "<name=" + self.name + ",address=" + self.address + ">"

    def __ne__(self, x):
        return self.name != x.name