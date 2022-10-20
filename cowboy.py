# cowboy adventure story
name = input("Enter your name: ")
print(f"Hello {name}, welcome to Cowboy Adventure!")
cowboy = 1;
farmer = 2;
role = int(input("What role do you wanna be? Press 1 for cowboy or 2 for farmer: "))
if role == 1:
    print("You have chosen the cowboy role!")
else:
    print("You have chosen the farmer role!")

if role == 2:
    print("You are a farmer. When you run a desolate land in northern Texas and grow cotton, one day: ")
    event1 = "1. You get robbed by a bandit who kills your family."
    event2 = "2. Your crops dry out and all die and you become a bandit."
    inputEvent1 = int(input(f"Which event would you choose \n {event1} \n {event2} \n Choose 1 or 2 for each event. "))
    if inputEvent1 == 1:
        print("You become a bounty hunter in order to look for the bandit who killed your family.")
        print("You are ordered to kill a 2 different corrupt politician choose which one: ")
        bountevent1 = int(input("Do you wanna kill politician 1 or 2? "))
        if bountevent1 == 1:
            print("You have died!")
            quit()
        else:
            print("You have killed politician 2!")
    else:
        print("You head towards the band in order to rob it.")