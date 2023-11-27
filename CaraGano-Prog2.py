#Cara Gano- Program 2 AIT

def loadData():
    tripList = [
        ("alice", 'chicago', 302),
        ("bruce", 'chicago', 309),
        ("david", 'chicago', 307),
        ("carol", 'columbus', 212),
        ("alice", 'chicago', 304),
        ("bruce", 'chicago', 301),
        ("david", 'columbus', 215),
        ("alice", 'chicago', 302),
        ("carol", 'chicago', 305),
        ("bruce", 'chicago', 304),
        ("carol", 'columbus', 218),
        ("alice", 'columbus', 217),
        ("carol", 'chicago', 309),
        ("david", 'columbus', 219)
        ]
    return tripList

def displayTrips(tripList):
    print("%-5s %10s %5s" % ("Name", "Destination", "Miles"))
    for record in tripList:
        n, c, m = record
        print("%-7s %8s %5s" % (n, c, m))

def addTrip():
    fn = input("Enter first name: ")
    city = input("Enter destination city: ")
    miles = input("Enter miles traveled: ")

    return fn, city, miles

def displayByName(tripList):
    name = input("Enter name (alice, bruce, carol or david): ")
    filter = []
    print("%-5s %8s %5s" % ("Name", "Destination", "Miles"))
    for n in tripList:
        if n[0] == name.lower():
            filter = 1
            print("%-5s %10s %5s" % (n[0], n[1], n[2]))
            #print(f'Name: {n[0]}, Destination: {n[1]}, Miles: {n[2]}')
        if filter == 0:
            print("No trip found with this name.")

def main():
    trips = loadData()

    while True:
        print("""
            Program options.
            1. Display all trips
            2. Input new trip
            3. Display trips by name
            4. Exit
            """)
        option = input("Enter your choice, 1, 2, 3 or 4: ")

        if option == "1":
            displayTrips(trips)
        elif option == "2":
            newTrip = addTrip()
            trips.append(newTrip)
        elif option == "3":
            displayByName(trips)
        elif option == "4":
            print("Goodbye")
            break
        else:
            print("Invalid entry.  Please enter 1, 2, 3 or 4.")
        
main()
