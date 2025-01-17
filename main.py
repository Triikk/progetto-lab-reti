import argparse
from router import Router

def create_link(r1 : Router , r2 : Router, d : int = 1):
    """
    Creates a link between router r1 and r2 with distance d.
    """
    r1.add_neighbor(r2,d)
    r2.add_neighbor(r1,d)

def get_help_message():
    return "\n".join([
        "round - get the current round",
        "tables - print routing tables",
        "routers - print routers",
        "step - perform a simulation step",
        "help - print this message",
        "exit - stop the simulation",
    ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", help="perform simulation automatically", action="store_true", default=True)
    parser.add_argument("--manual", help="perform simulation manually", action="store_true")
    args = parser.parse_args()
    
    # configuration 1
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

    # configuration 2
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

    # configuration 3
    a = Router("a", "192.168.0.1")
    b = Router("b", "192.168.0.2")
    c = Router("c", "192.168.0.3")
    d = Router("d", "192.168.0.4")
    e = Router("e", "192.168.0.5")
    f = Router("f", "192.168.0.6")
    routers = [a,b,c,d,e,f]
    create_link(a,b,1)
    create_link(a,f,3)
    create_link(b,c,3)
    create_link(b,e,5)
    create_link(b,f,1)
    create_link(c,d,2)
    create_link(d,e,1)
    create_link(d,f,6)
    create_link(e,f,2)

    if args.manual:
        print("Welcome to the manual simulation of the Distance Vector routing protocol! These are the available commands:")
        print(get_help_message())
        
        round = 1
        while True:
            command = input("> ").strip()
            match command:
                case "round":
                    print("Round",round)
                case "tables":
                    for router in routers:
                        print("Routing table of router",router.name)
                        print("-"*50)
                        print("{:15s}{:15s}{:5s}".format("Destination","Gateway","Distance"))
                        for destination,route in sorted(router.paths.items(), key = lambda x : x[0].name): # sort on destination's alphanumerical order
                            gateway,distance = route
                            print("{:15s}{:15s}{:5d}".format(destination.name,gateway.name,distance))
                        print("-"*50)
                case "routers":
                    for router in routers:
                        print(router)
                case "step":
                    for router in routers:
                        router.send()
                    for router in routers:
                        router.update()
                    round += 1
                case "help":
                    print(get_help_message())
                case "exit":
                    exit()
                case _:
                    continue
    else:
        for round in range(len(routers)):
            print("="*50)
            print("Round",round+1)
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