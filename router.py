from math import inf

class Router:

    def __init__(self, name, ip_address):
        self.name = name
        self.address = ip_address
        self.neighbors : dict = {}
        self.paths : dict = {} # paths[router] = [gateway,distance]
        self.received_paths = {}

    def add_neighbor(self, r : 'Router', d : int = 1):
        """
        Adds router r as neighbor with distance d.
        """
        assert(r != self)
        self.neighbors[r] = [r,d]
        self.paths[r] = [r,d]

    def send(self):
        """
        Sends the path to all neighbors
        """
        for neighbor in self.neighbors:
            neighbor.recv(self, {destination : route for destination,route in self.paths.items() if route[0] != neighbor and destination != neighbor})

    def recv(self, sender : 'Router', paths : dict):
        """
        Receives paths from neighbor `sender`.
        """
        assert(sender in self.neighbors)
        self.received_paths[sender] = paths

    def update(self):
        """
        Updates the routing informations based on the stored received paths.
        """
        for sender,paths in self.received_paths.items():
            for destination,route in paths.items():
                gateway,distance = route
                distance_from_sender = self.paths[sender][1]
                if destination not in self.paths: # unknown destination
                    self.paths[destination] = [sender,distance_from_sender+distance]
                else:
                    current_distance = self.paths[destination][1] # current distance to destination
                    new_distance = distance_from_sender + distance # possible new distance
                    if current_distance > new_distance:
                        gateway = self.paths[sender][0] # the gateway is not the actual sender (a neighbor) but the neighbor which allows me to reach the sender as fast as possible
                        self.paths[destination] = [gateway,new_distance]
        self.received_paths = {}

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "<name=" + self.name + ",address=" + self.address + ">"

    def __ne__(self, x):
        return self.name != x.name