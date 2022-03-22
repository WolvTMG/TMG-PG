import random
import sys
import time
import asyncio
import os
import json
from _thread import *


health = 10
attack = 10
xp = 0
cash = 100
rounds = 5
subscribe_to_dream = 0
dev = 0

randomizedquests = ["You are encountered by a wild wolf, ", "A group of angry bears surround you, ",
"You wake up in the back of a van and you don't remember much, ",
"A large group of anti vax moms surround you because you're wearing a mask, "]
randomizedquests2 = ["You run into a cult hideout, ", "A notorious murderer is 5 feet away staring at you, ",
"Someone named Michael Myers is a few feet away from you with a knife in his hand, ",
"Jason the killer is running towards you in the forest, ",
"You wake up in a nightmare and Freddy Kruger is breathing down your spine, ",
"You wake up in an abandoned building and hear foot steps, ",
"You wake up to the sounds of strange noises, and your home alone, ",
"A bunch of twitter users saw you having an opinion and are canceling you, "]
randomizedquests3 = ["You wake up tied up with a bunch of mafia bosses above you talking about a deal, ",
"You run into a cult hideout, ", "A zombie apocolypse breaks out and you and a few civilizations are left alive, "]
randomizedquests4 = ["A furry thinks you're cute, ", "James Charles sent you (a minor) some questionable images, ",
"Your mom saw your report card, ", "You see a minecraft youtuber walking in front of you, "]
randomizedquests5 = ["You see a cringe fortnite kid dancing for a tik tok, "]
randomizedquests6 = ["I ran out of questions, "]
randomizedluck = ["attack", "attack", "run"]
randomizednumbers = [1, 2, 3, 4, 5, 6]
randomizeddamages = [1, 2, 3, 4, 5, 6]
randomizedcash = [50, 150, 200, 250]
randomizedxp = [1, 2, 3, 4, 5, 6]
randomizedattack = [1, 2, 3, 4]


def loops():
    while True:
        if health <= 0:
            print("You died!\n")
            time.sleep(6)
            os._exit(3)

def loops2():
    global cash
    global xp
    global health
    global attack
    i = 1
    while i == 1:
        if dev == 1:
            cash = cash + 999999999
            xp = xp + 999999999
            health = health + 999999999
            attack = attack + 999999999
            i = i + 1

start_new_thread(loops, ())
start_new_thread(loops2, ())


async def arc7():
    print("arc 7 coming soon")
    time.sleep(2)
    print(f"Health: {health}")
    print(f"Attack: {attack}")
    print(f"Experience: {xp}")
    print(f"Cash: {cash}")
    sys.exit()

async def arc6():
    global health
    global attack
    global xp
    global rounds
    global cash
    global damage
    print("(Arc 6)")
    print("You will now recieve randomized cash")
    time.sleep(2)
    clear()
    for i in range(rounds):
        print(f"Health {health}\nAttack: {attack}\nExpperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests6)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        rcash = random.choice(randomizedcash)
        time.sleep(1)
        ui = input(quest + "what do you do, attack or run away? ").lower()
        if ui == 'attack' and luck == 'attack' and attack > 0:
            clear()
            print("You sucsesfully defend against the attacker and gained 3 xp\n")
            xp = xp + 6
            attack = attack - 3
            cash = cash + rcash
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'attack' and attack <= 0:
            clear()
            print(f"You have no more attacks and you loose {damage} hp")
            health = health - damage
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'run':
            clear()
            print(f"You lost the fight and lose {damage} hp")
            health = health - damage
            attack = attack - 3
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 3 xp!\n")
            xp = xp + 6
            cash = cash + rcash
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            clear()
            print(f"The attacker outran you and you lost {damage} hp\n")
            health = health - damage
            time.sleep(2)
            clear()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await arc7()

async def arc5():
    global health
    global attack
    global xp
    global rounds
    global cash
    global damage
    print("(Arc 5)")
    print("WARNING, from now on attacks will be randomized from 1 - 6 damage, this will be the last warning and will continue for future arcs")
    time.sleep(2)
    clear()
    for i in range(rounds):
        print(f"Health: {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests5)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        time.sleep(1)
        ui = input(quest + "what do you do, attack or run away? ").lower()
        if ui == 'attack' and luck == 'attack' and attack > 0:
            clear()
            print("You sucsesfully defend against the attacker and gained 3 xp\n")
            xp = xp + 5
            attack = attack - 3
            cash = cash + 100
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'attack' and attack <= 0:
            clear()
            print(f"You have no more attacks and you loose {damage} hp")
            health = health - 2
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'run':
            clear()
            print(f"You lost the fight and lose {damage} hp")
            health = health - damage
            attack = attack - 3
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 3 xp!\n")
            xp = xp + 5
            cash = cash + 100
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            clear()
            print(f"The attacker outran you and you lost {damage} hp\n")
            health = health - damage
            time.sleep(2)
            clear()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice5()

async def arc4():
    global health
    global attack
    global xp
    global rounds
    global cash
    global damage
    print("(Arc 4)")
    print("WARNING, game saves once process is terminated, always wait after the process has stopped before closing")
    print("WARNING, in arc 4, attacks will now be randomized from 1 - 6 damage to you and you are required 2 attacks to kill enemies")
    time.sleep(2)
    clear()
    for i in range(rounds):
        print(f"Health {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests4)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        time.sleep(1)
        ui = input(quest + "what do you do, attack or run away? ").lower()
        if ui == 'attack' and luck == 'attack' and attack > 0:
            clear()
            print("You sucsesfully defend against the attacker and gained 3 xp\n")
            xp = xp + 4
            attack = attack - 2
            cash = cash + 80
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'attack' and attack <= 0:
            clear()
            print(f"You have no more attacks and you loose {damage} hp")
            health = health - damage
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'run':
            clear()
            print(f"You lost the fight and lose {damage} hp")
            health = health - damage
            attack = attack - 2
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 3 xp!\n")
            xp = xp + 4
            cash = cash + 80
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            clear()
            print(f"The attacker outran you and you lost {damage} hp\n")
            health = health - damage
            time.sleep(2)
            clear()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice4()


async def arc3():
    global health
    global attack
    global xp
    global rounds
    global cash
    global subscribe_to_dream
    print("(Arc 3)")
    print("WARNING, game saves once process is terminated, always wait after the process has stopped before closing")
    print("WARNING, (danger ahead), attacks now deal 4 damage to you and you are required 2 attacks to kill enemies")
    time.sleep(2)
    clear()
    for i in range(rounds):
        print(f"Health {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests3)
        luck = random.choice(randomizedluck)
        time.sleep(1)
        ui = input(quest + "attack or run away? ").lower()
        if ui == 'attack' and luck == 'attack' and attack > 0:
            clear()
            print("You sucsesfully defend against the attacker and gained 3 xp\n")
            xp = xp + 3
            attack = attack - 2
            cash = cash + 60
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'attack' and attack <= 0:
            clear()
            print("You have no more attacks and you loose 4 hp")
            health = health - 4
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'run':
            clear()
            print("You lost the fight and lose 4 hp")
            health = health - 4
            attack = attack - 2
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 3 xp!\n")
            xp = xp + 3
            cash = cash + 60
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + 60
                xp = xp + 3
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print("The attacker outran you and you lost 4 hp\n")
                health = health - 4
                time.sleep(2)
            clear()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice3()
        

async def arc2():
    global health
    global attack
    global xp
    global rounds
    global cash
    print("(Arc 2)")
    print("WARNING, game saves once process is terminated, always wait after the process has stopped before closing")
    print("WARNING, in arc 2 rewards are doubled but so is damage to your health")
    time.sleep(2)
    clear()
    for i in range(rounds):
        print(f"Health: {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests2)
        luck = random.choice(randomizedluck)
        time.sleep(1)
        ui = input(quest + "attack or run away? ").lower()
        if ui == 'attack' and luck == "attack" and attack > 0:
            clear()
            print("You sucsesfully defended against the attacker and gained 2 xp\n")
            xp = xp + 2
            attack = attack - 1
            cash = cash + 40
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'attack' and attack <= 0:
            clear()
            print("You have no more attacks and you loose 2 hp")
            health = health - 2
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == "run":
            clear()
            print("You lost the fight and lose 2 hp\n")
            health = health - 2
            attack = attack - 1
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 2 xp!\n")
            xp = xp + 2
            cash = cash + 40
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            clear()
            print("The attacker outran you and you lost 2 hp\n")
            health = health - 2
            time.sleep(2)
            clear()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice2()


async def arc1():
    global health
    global attack
    global xp
    global rounds
    global cash
    print("(Arc 1)")
    print("WARNING, game saves once process is terminated, always wait after the process has stopped before closing\n")
    time.sleep(2)
    clear()
    for i in range(rounds):
        print(f"Health: {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests)
        luck = random.choice(randomizedluck)
        time.sleep(1)
        ui = input(quest + "attack or run away? ").lower()
        if ui == 'attack' and luck == "attack" and attack > 0:
            clear()
            print("You sucsesfully defended against the attacker and gained 1 xp\n")
            cash = cash + 20
            xp = xp + 1
            attack = attack - 1
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == 'attack' and attack <= 0:
            clear()
            print("You have no more attacks and you loose 1 hp")
            health = health - 1
            time.sleep(2)
            clear()
        elif ui == 'attack' and luck == "run":
            clear()
            print("You lost the fight and lose 1 hp\n")
            health = health - 1
            attack = attack - 1
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 1 xp!\n")
            cash = cash + 20
            xp = xp + 1
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            clear()
            print("The attacker outran you and you lost 1 hp\n")
            health = health - 1
            time.sleep(2)
            clear()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice()


async def choice5():
    y = input("Would you like to visit the shop? ").lower()
    if y == 'yes':
        await shop5()
    elif y == 'no':
        await arc6()
    else:
        await choice5()

async def choice4():
    y = input("Would you like to visit the shop? ").lower()
    if y == 'yes':
        await shop4()
    elif y == 'no':
        await arc5()
    else:
        await choice4()
        
async def choice3():
    y = input("Would you like to visit the shop? ").lower()
    if y == 'yes':
        await shop3()
    elif y == 'no':
        await arc4()
    else:
        await choice3()

async def choice2():
    y = input("Would you like to visit the shop? ").lower()
    if y == 'yes':
        await shop2()
    elif y == 'no':
        await arc3()
    else:
        await choice2()

async def choice():
    y = input("Would you like to visit the shop? ").lower()
    if y == 'yes':
        await shop()
    elif y == 'no':
        await arc2()
    else:
        await choice()


async def shop6():
    global cash
    global health
    global attack
    print(f"Balance: {cash}\n")
    time.sleep(3)
    print("no shop for arc 6 yet")
    await arc7()

async def shop5():
    global cash
    global health
    global attack
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (15 hp): 150$ (1)\n\nMega Attack Boost (Rare, +25 attacks): 300$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 150:
        health = health + 15
        cash = cash - 150
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop4()
    elif choice == '1' and cash <= 150:
        clear()
        print("Insufficient Funds")
        await shop4()
    elif choice == '2' and cash >= 300:
        attack = attack + 25
        cash = cash - 300
        clear()
        print(f"Sucsesfully boosted your attacks, your attack is now {attack} ")
        await shop4()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop4()
    elif choice == '3' and cash >= 500:
        cash = cash - 500
        subscribe_to_dream = subscribe_to_dream + 5
        print(f"Sucsesfully subscribed to Dream")
        await shop4()
    elif choice == '3' and cash <=500:
        print("Insufficient Funds")
        await shop4()
    elif choice == 'exit':
        clear()
        await arc6()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop4()

async def shop4():
    global cash
    global health
    global attack
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (15 hp): 150$ (1)\n\nMega Attack Boost (Rare, +25 attacks): 300$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 150:
        health = health + 15
        cash = cash - 150
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop4()
    elif choice == '1' and cash <= 150:
        clear()
        print("Insufficient Funds")
        await shop4()
    elif choice == '2' and cash >= 300:
        attack = attack + 25
        cash = cash - 300
        clear()
        print(f"Sucsesfully boosted your attacks, your attack is now {attack} ")
        await shop4()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop4()
    elif choice == '3' and cash >= 500:
        cash = cash - 500
        subscribe_to_dream = subscribe_to_dream + 5
        print(f"Sucsesfully subscribed to Dream")
        await shop4()
    elif choice == '3' and cash <=500:
        print("Insufficient Funds")
        await shop4()
    elif choice == 'exit':
        clear()
        await arc5()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop4()

async def shop3():
    global cash
    global health
    global attack
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (15 hp): 150$ (1)\n\nMega Attack Boost (Rare, +25 attacks): 300$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 150:
        health = health + 15
        cash = cash - 150
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop3()
    elif choice == '1' and cash <= 150:
        clear()
        print("Insufficient Funds")
        await shop3()
    elif choice == '2' and cash >= 300:
        attack = attack + 25
        cash = cash - 300
        clear()
        print(f"Sucsesfully boosted your attacks, your attack is now {attack} ")
        await shop3()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop3()
    elif choice == '3' and cash >= 500:
        cash = cash - 500
        subscribe_to_dream = subscribe_to_dream + 5
        print(f"Sucsesfully subscribed to Dream")
        await shop3()
    elif choice == '3' and cash <=500:
        print("Insufficient Funds")
        await shop3()
    elif choice == 'exit':
        clear()
        await arc4()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop3()

async def shop2():
    global cash
    global health
    global attack
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Heal (5 hp): 50$ (1)\n\nAttack Boost (5 attacks): 80$ (2)\n\nMega Heal (15 hp): 120$ (3)\n\nExit Shop: free, or is it? (exit)\n\n").lower()
    if choice == '1' and cash >= 50:
        health = health + 5
        cash = cash - 50
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop2()
    elif choice == '1' and cash <= 50:
        clear()
        print("Insufficient Funds")
        await shop2()
    elif choice == '2' and cash >= 80:
        attack = attack + 5
        cash = cash - 80
        clear()
        print(f"Sucsesfully boosted your attacks, your attack is now {attack} ")
        await shop2()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop2()
    elif choice == '3' and cash >= 120:
        health = health + 15
        cash = cash - 120
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop2()
    elif choice == '3' and cash <= 120:
        clear()
        print("Insufficient Funds")
        await shop2()
    elif choice == 'exit':
        clear()
        await arc3()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop2()

async def shop():
    global cash
    global health
    global attack
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Heal (5 hp): 50$ (1)\n\nAttack Boost (5 attacks): 80$ (2)\n\nMega Heal (15 hp): 120$ (3)\n\nExit Shop: free, or is it? (exit)\n\n").lower()
    if choice == '1' and cash >= 50:
        health = health + 5
        cash = cash - 50
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop()
    elif choice == '1' and cash <= 50:
        clear()
        print("Insufficient Funds")
        await shop()
    elif choice == '2' and cash >= 80:
        attack = attack + 5
        cash = cash - 80
        clear()
        print(f"Sucsesfully boosted your attacks, your attack is now {attack} ")
        await shop()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop()
    elif choice == '3' and cash >= 120:
        health = health + 15
        cash = cash - 120
        clear()
        print(f"Sucsesfully healed, your health is now {health} ")
        await shop()
    elif choice == '3' and cash <= 120:
        clear()
        print("Insufficient Funds")
        await shop()
    elif choice == 'exit':
        clear()
        await arc2()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop()


# async def enchants():
#     global enchantments
#     global cash
#     enchant_1 = 0
#     while enchant_1 == 0:
#         enchant1 = input("Enchantment 1 = 500$, would you like to purchase? ").lower()
#         if enchant1 == 'yes' and cash >= 500:
#             cash = cash - 500
#             enchant1 = enchant1 + 1
#         else:
#             enchants()
#     enchant_2 = 0
#     while enchant_2 == 0:
#         enchant2 = input("Enchantment 2 = 750$, would you like to purchase? ").lower()
#         if enchant2 == 'yes' and cash >= 750:
#             cash = cash - 750
#             enchant2 = enchant2 + 1
#         else:
#             enchants()
    

async def devchoice():
    choice = input("Which arc would you like to explore? ")
    if choice == '1':
        await arc1()
    elif choice == '2':
        await arc2()
    elif choice == '3':
        await arc3()
    elif choice == '4':
        await arc4()
    elif choice == '5':
        await arc5()
    elif choice == '6':
        await arc6()
    elif choice == '7':
        await arc7()
    else:
        await devchoice()


ui = int(input("Age: "))

if ui < 13:
    print("Age requirement not met [error code 1]")
    sys.exit()
elif ui > 100:
    print("Age requirement not met [error code 2]")
    sys.exit()
else:
    user = input("Username: ")

names = ["James", "Jack", "Will", "Jonathon", "Max", "Michael"]
begin = random.choice(names)


def clear():
    system = os.name
    if system == 'nt':
        #if its windows
        os.system('cls')
    elif system == 'posix':
        #if its linux
        os.system('clear')
    else:
        print('\n'*120)
    return


async def start():
    global begin
    global dev
    con1 = input("Welcome to camp, this is your first time so make sure to figure out the ropes by the end of the day, got it, " + begin +"? ").lower()
    if con1 == 'yes':
        print("Prepare for war " + begin +"!\n")
        clear()
        await arc1()
    elif con1 == 'no':
        print("Come back when you're ready")
        sys.exit()
    elif con1 == 'devmode':
        dev = dev + 1
        await devchoice()
    else:
        print("Yes or no")
        await start()
asyncio.run(start())


