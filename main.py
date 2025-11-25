
hotel = "Sunrise Hotel"
print("\n", "="*55)
print("        WELCOME TO SUNRISE HOTEL - Feel at Home!       ".center(55))
print("="*55, "\n")


all_rooms = [101,102,103,104, 201,202,203,204, 301,302]
price = {101:1200,102:1200,103:1200,104:1200,
         201:2200,202:2200,203:2200,204:2200,
         301:4500,302:8000}

room_type = {101:"Standard Single",102:"Standard Single",103:"Standard Single",104:"Standard Single",
             201:"Family Double",202:"Family Double",203:"Family Double",204:"Family Double",
             301:"Deluxe",302:"Royal Suite"}

status = {}        
guests = []          
for r in all_rooms:
    status[r] = "Free"

def menu():
    print("\n   WHAT WOULD YOU LIKE TO DO?")
    print("   1. See all rooms")
    print("   2. Book a room")
    print("   3. Check-in")
    print("   4. Check-out & Pay bill")
    print("   5. See who is staying")
    print("   6. Exit")
    print("-"*40)

def see_rooms():
    print("\n   ROOM      TYPE                PRICE     STATUS")
    print("   ------------------------------------------------")
    for r in all_rooms:
        who = status[r]
        if who == "Free":
            print(f"   {r}     {room_type[r]:<20} {price[r]:<8}  Available")
        else:
            print(f"   {r}     {room_type[r]:<20} {price[r]:<8}  Occupied by {who}")
    print()

def book():
    print("\n   Hello! Happy to have you here")
    name = input("   Your name please: ").title().strip()
    phone = input("   Phone number: ").strip()

    print("\n   These rooms are free right now:")
    free = []
    for r in all_rooms:
        if status[r] == "Free":
            print(f"   → Room {r}  |  {room_type[r]}  |  ₹{price[r]}/night")
            free.append(r)
    
    if not free:
        print("   Sorry yaar, full house today! Come tomorrow")
        return

    try:
        chosen = int(input("\n   Which room number? "))
        nights = int(input("   How many nights? "))
    except:
        print("   Arre, numbers only please!")
        return

    if chosen not in free:
        print("   That room is taken, pick another one")
        return

    total = nights * price[chosen]

    print("\n   Booking Done!")
    print(f"   Name      : {name}")
    print(f"   Room      : {chosen} ({room_type[chosen]})")
    print(f"   Nights    : {nights}")
    print(f"   Total     : ₹{total}")
    print("   See you soon! Your room is waiting")

    # remember everything
    guests.append({"room":chosen, "name":name, "phone":phone, "nights":nights, "bill":total})
    status[chosen] = name

def checkin():
    print("\n   Welcome back!")
    try:
        room = int(input("   Your room number please: "))
    except:
        print("   Invalid room")
        return

    if status.get(room, "Free") != "Free":
        print(f"   Hello {status[room]}! Your key is ready. Enjoy your stay")
    else:
        print("   No booking found for this room. Talk to reception")

def checkout():
    print("\n   Hope you loved your stay")
    try:
        room = int(input("   Room number for checkout: "))
    except:
        return

    if status.get(room, "Free") == "Free":
        print("   This room is empty already")
        return

    guest_name = status[room]


    for g in guests:
        if g["room"] == room and g["name"] == guest_name:
            print("\n   FINAL BILL")
            print("   " + "═"*40)
            print(f"   Guest       : {g['name']}")
            print(f"   Phone       : {g['phone']}")
            print(f"   Room        : {room} ({room_type[room]})")
            print(f"   Stay        : {g['nights']} night(s)")
            print(f"   Rate        : ₹{price[room]}/night")
            print("   " + "─"*40)
            print(f"   TOTAL       : ₹{g['bill']}")
            print("   " + "═"*40)
            print("   Thank you so much! Come again")
            
            status[room] = "Free"    
            guests.remove(g)         
            return

    print("   No record found")

def current_guests():
    if not guests:
        print("\n   No one staying right now. So peaceful")
        return
    print("\n   CURRENT GUESTS")
    print("   " + "-"*70)
    for g in guests:
        print(f"   Room {g['room']} → {g['name']:<15} | {g['phone']:<12} | {g['nights']} nights | ₹{g['bill']}")
    print()

while True:
    menu()
    choice = input("   Choose (1-6): ").strip()

    if choice == "1":
        see_rooms()
    elif choice == "2":
        book()
    elif choice == "3":
        checkin()
    elif choice == "4":
        checkout()
    elif choice == "5":
        current_guests()
    elif choice == "6":
        print("\n   Thank you for visiting Sunrise Hotel!")
        print("   Take care and come back soon")
        break
    else:
        print("   Wrong option, try again")

    input("\n   Press Enter to continue...")