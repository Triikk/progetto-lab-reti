from router import Router

def create_link(r1 : Router , r2 : Router, d : int = 1):
    """
    Creates a link between router r1 and r2 with distance d.
    """
    r1.add_neighbor(r2,d)
    r2.add_neighbor(r1,d)

if __name__ == "__main__":
    # r1 = Router("r1", "192.168.0.1")
    # r2 = Router("r2", "192.168.0.2")
    # r3 = Router("r3", "192.168.0.3")
    # r4 = Router("r4", "192.168.0.4")
    # r5 = Router("r5", "192.168.0.5")
    # routers = [r1,r2,r3,r4,r5]
    # create_link(r1,r2)
    # create_link(r1,r3)
    # create_link(r2,r4)
    # create_link(r3,r4)
    # create_link(r4,r5)

    # a = Router("a", "192.168.0.1")
    # b = Router("b", "192.168.0.2")
    # c = Router("c", "192.168.0.3")
    # d = Router("d", "192.168.0.4")
    # e = Router("e", "192.168.0.5")
    # routers = [a,b,c,d,e]
    # create_link(e,c,7)
    # create_link(e,d,2)
    # create_link(c,d,3)
    # create_link(c,a,6)
    # create_link(c,b,2)
    # create_link(d,b,1)
    # create_link(a,b,1)

    # a = Router("a", "192.168.0.1")
    # b = Router("b", "192.168.0.2")
    # c = Router("c", "192.168.0.3")
    # d = Router("d", "192.168.0.4")
    # e = Router("e", "192.168.0.5")
    # f = Router("f", "192.168.0.6")
    # routers = [a,b,c,d,e,f]
    # create_link(a,b,1)
    # create_link(a,f,3)
    # create_link(b,c,3)
    # create_link(b,e,5)
    # create_link(b,f,1)
    # create_link(c,d,2)
    # create_link(d,e,1)
    # create_link(d,f,6)
    # create_link(e,f,2)

    for i in range(len(routers)):
        print("="*50)
        print("Round",i+1)
        print("="*50)
        for router in routers:
            print("Routing table of router",router.name)
            print("-"*50)
            print("{:15s}{:15s}{:5s}".format("Destination","Gateway","Distance"))
            for destination,route in sorted(router.paths.items(), key = lambda x : x[0].name): # sort on destination's alphanumerical order
                gateway,distance = route
                print("{:15s}{:15s}{:5d}".format(destination.name,gateway.name,distance))
            print("-"*50)

        for router in routers:
            router.send()
        for router in routers:
            router.update()