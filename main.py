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
gameround = 1
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

rounds1 = 5
rounds2 = 5
rounds3 = 5
rounds4 = 5
rounds5 = 5
rounds6 = 5
rounds7 = 5
rounds8 = 5


hpotion1 = 0
hpotion2 = 0
hpotion3 = 0
hpotion4 = 0
apotion1 = 0


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


async def arc8():
    print("arc 8 coming soon")
    time.sleep(2)
    print(f"Health: {health}")
    print(f"Attack: {attack}")
    print(f"Experience: {xp}")
    print(f"Cash: {cash}")
    sys.exit()

async def arc7():
    global health
    global attack
    global xp
    global rounds7
    global cash
    global damage
    global gameround
    global subscribe_to_dream
    gameround = gameround + 1
    print("(Arc 7)")
    print("WARNING, damage, cash, xp and attacks will now be randomized from now on")
    time.sleep(4)
    clear()
    for i in range(rounds7):
        print(f"Health {health}\nAttack: {attack}\nExpperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests6)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        rcash = random.choice(randomizedcash)
        rxp = random.choice(randomizedxp)
        rattack = random.choice(randomizedattack)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
        if ui == 'attack' and luck == 'attack' and attack > 0:
            clear()
            print("You sucsesfully defend against the attacker and gained 3 xp\n")
            xp = xp + rxp
            attack = attack - rattack
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
            attack = attack - rattack
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'run':
            clear()
            print("You sucsesfully ran away and gained 3 xp!\n")
            xp = xp + rxp
            cash = cash + rcash
            time.sleep(2)
            clear()
        elif ui == 'run' and luck == 'attack':
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + rcash
                xp = xp + rxp
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print(f"The attacker outran you and you lost {damage} hp\n")
                health = health - damage
                time.sleep(2)
            clear() 
        elif ui == 'bag':
            rounds7 = rounds7 + 1
            clear()
            await bag()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await arc8()

async def arc6():
    global health
    global attack
    global xp
    global rounds6
    global cash
    global damage
    global gameround
    global subscribe_to_dream
    gameround = gameround + 1
    print("(Arc 6)")
    print("You will now recieve randomized cash")
    time.sleep(4)
    clear()
    for i in range(rounds6):
        print(f"Health {health}\nAttack: {attack}\nExpperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests6)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        rcash = random.choice(randomizedcash)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
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
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + rcash
                xp = xp + 6
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print(f"The attacker outran you and you lost {damage} hp\n")
                health = health - damage
                time.sleep(2)
            clear()
        elif ui == 'bag':
            rounds6 = rounds6 + 1
            clear()
            await bag()
        else:
            clear()
            print("Answer must be attack or run")
            rounds = rounds + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice6()

async def arc5():
    global health
    global attack
    global xp
    global rounds5
    global cash
    global damage
    global gameround
    global subscribe_to_dream
    gameround = gameround + 1
    print("(Arc 5)")
    time.sleep(4)
    clear()
    for i in range(rounds5):
        print(f"Health: {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests5)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
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
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + 100
                xp = xp + 5
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print(f"The attacker outran you and you lost {damage} hp\n")
                health = health - damage
                time.sleep(2)
            clear()
        elif ui == 'bag':
            rounds5 = rounds5 + 1
            clear()
            await bag()
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
    global rounds4
    global cash
    global damage
    global gameround
    global subscribe_to_dream
    gameround = gameround + 1
    print("(Arc 4)")
    print("WARNING, attacks will now be randomized from 1 - 6 damage")
    time.sleep(4)
    clear()
    for i in range(rounds4):
        print(f"Health {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests4)
        luck = random.choice(randomizedluck)
        damage = random.choice(randomizeddamages)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
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
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + 80
                xp = xp + 4
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print(f"The attacker outran you and you lost {damage} hp\n")
                health = health - damage
                time.sleep(2)
            clear()
        elif ui == 'bag':
            rounds4 = rounds4 + 1
            clear()
            await bag()
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
    global rounds3
    global cash
    global subscribe_to_dream
    global gameround
    gameround = gameround + 1
    print("(Arc 3)")
    print("WARNING, (danger ahead), attacks now deal 4 damage to you and you are required 2 attacks to kill enemies")
    time.sleep(4)
    clear()
    for i in range(rounds3):
        print(f"Health {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests3)
        luck = random.choice(randomizedluck)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
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
        elif ui == 'bag':
            rounds3 = rounds3 + 1
            clear()
            await bag()
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
    global rounds2
    global cash
    global gameround
    global subscribe_to_dream
    gameround = gameround + 1
    print("(Arc 2)")
    print("WARNING, in arc 2 rewards are doubled but so is damage to your health")
    time.sleep(4)
    clear()
    for i in range(rounds2):
        print(f"Health: {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests2)
        luck = random.choice(randomizedluck)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
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
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + 40
                xp = xp + 2
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print("The attacker outran you and you lost 2 hp\n")
                health = health - 2
                time.sleep(2)
            clear()
        elif ui == 'bag':
            rounds2 = rounds2 + 1
            clear()
            await bag()
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
    global rounds1
    global cash
    global gameround
    global subscribe_to_dream
    gameround = gameround + 1
    print("(Arc 1)")
    print("WARNING, game saves once process is terminated, always wait after the process has stopped before closing\n")
    time.sleep(4)
    clear()
    for i in range(rounds1):
        print(f"Health: {health}\nAttack: {attack}\nExperience: {xp}\nCash: {cash}\n")
        quest = random.choice(randomizedquests)
        luck = random.choice(randomizedluck)
        time.sleep(1)
        ui = input(quest + "\nAttack / Run / Bag \n\nChoice: ").lower()
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
            if subscribe_to_dream > 0:
                print("The attacker was too disgusted to run after you because you were subscribed to Dream you fat fuck ")
                cash = cash + 20
                xp = xp + 1
                subscribe_to_dream = subscribe_to_dream - 1
                time.sleep(2)
                clear()
            else:
                clear()
                print("The attacker outran you and you lost 1 hp\n")
                health = health - 1
                time.sleep(2)
            clear()
        elif ui == 'bag':
            rounds1 = rounds1 + 1
            clear()
            await bag()
        else:
            clear()
            print("Answer must be attack or run")
            rounds1 = rounds1 + 1
            time.sleep(2)
            clear()
    time.sleep(2)
    await choice()


async def choice6():
    y = input("Would you like to visit the shop? ").lower()
    if y == 'yes':
        await shop6()
    elif y == 'no':
        await arc7()
    else:
        await choice6()


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


async def shop7():
    global cash
    global health
    global attack
    print(f"Balance: {cash}\n")
    time.sleep(3)
    print("no shop for arc 7 yet")
    await arc8()

async def shop6():
    global cash
    global health
    global attack
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (25 hp): 120$ (1)\n\nAttack Boost (5 Attacks): 80$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 120:
        cash = cash - 120
        hpotion2 = hpotion2 + 1
        clear()
        print(f"Sucsesfully bought Healing Potion (10hp)")
        await shop6()
    elif choice == '1' and cash <= 120:
        clear()
        print("Insufficient Funds")
        await shop6()
    elif choice == '2' and cash >= 80:
        apotion1 = apotion1 + 1
        cash = cash - 80
        clear()
        print(f"Sucsesfully bought Attack Potion (5 atk)")
        await shop6()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop6()
    elif choice == '3' and cash >= 500:
        cash = cash - 500
        subscribe_to_dream = subscribe_to_dream + 5
        print(f"Sucsesfully subscribed to Dream")
        await shop6()
    elif choice == '3' and cash <=500:
        print("Insufficient Funds")
        await shop6()
    elif choice == 'exit':
        clear()
        await arc7()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop6()

async def shop5():
    global cash
    global health
    global attack
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (25 hp): 120$ (1)\n\nAttack Boost (5 Attacks): 80$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 120:
        cash = cash - 120
        hpotion2 = hpotion2 + 1
        clear()
        print(f"Sucsesfully bought Healing Potion (25hp)")
        await shop5()
    elif choice == '1' and cash <= 120:
        clear()
        print("Insufficient Funds")
        await shop5()
    elif choice == '2' and cash >= 80:
        apotion1 = apotion1 + 1
        cash = cash - 80
        clear()
        print(f"Sucsesfully bought Attack Potion (5 atk)")
        await shop5()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop5()
    elif choice == '3' and cash >= 500:
        cash = cash - 500
        subscribe_to_dream = subscribe_to_dream + 5
        print(f"Sucsesfully subscribed to Dream")
        await shop5()
    elif choice == '3' and cash <=500:
        print("Insufficient Funds")
        await shop5()
    elif choice == 'exit':
        clear()
        await arc6()
    else:
        clear()
        print("Please make sure you enter a valid item number (1, 2, 3, exit)\n")
        await shop5()

async def shop4():
    global cash
    global health
    global attack
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (25 hp): 120$ (1)\n\nAttack Boost (5 Attacks): 80$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 120:
        cash = cash - 120
        hpotion2 = hpotion2 + 1
        clear()
        print(f"Sucsesfully bought Healing Potion (25hp)")
        await shop4()
    elif choice == '1' and cash <= 120:
        clear()
        print("Insufficient Funds")
        await shop4()
    elif choice == '2' and cash >= 80:
        apotion1 = apotion1 + 1
        cash = cash - 80
        clear()
        print(f"Sucsesfully bought Attack Potion (5 atk)")
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
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Mega Heal (25 hp): 120$ (1)\n\nAttack Boost (5 Attacks): 80$ (2)\n\nSubscribe to Dream: 500$ (3) \n\nLeave the store: (exit)\n\n").lower()
    if choice == '1' and cash >= 120:
        cash = cash - 120
        hpotion2 = hpotion2 + 1
        clear()
        print(f"Sucsesfully bought Healing Potion (25hp)")
        await shop3()
    elif choice == '1' and cash <= 120:
        clear()
        print("Insufficient Funds")
        await shop3()
    elif choice == '2' and cash >= 80:
        apotion1 = apotion1 + 1
        cash = cash - 80
        clear()
        print(f"Sucsesfully bought Attack Potion (5 atk)")
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
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global subscribe_to_dream
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Heal (10 hp): 50$ (1)\n\nAttack Boost (5 attacks): 80$ (2)\n\nMega Heal (25 hp): 120$ (3)\n\nExit Shop: free, or is it? (exit)\n\n").lower()
    if choice == '1' and cash >= 50:
        hpotion1 = hpotion1 + 1
        cash = cash - 50
        clear()
        print(f"Sucsesfully bought Healing Potion (10hp)")
        await shop2()
    elif choice == '1' and cash <= 50:
        clear()
        print("Insufficient Funds")
        await shop2()
    elif choice == '2' and cash >= 80:
        apotion1 = apotion1 + 1
        cash = cash - 80
        clear()
        print(f"Sucsesfully bought Attack Potion (5 atk)")
        await shop2()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop2()
    elif choice == '3' and cash >= 120:
        hpotion2 = hpotion2 + 1
        cash = cash - 120
        clear()
        print(f"Sucsesfully bought Healing Potion (25hp)")
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
    global health
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global cash
    global health
    global attack
    print(f"Balance: {cash}\n")
    print("WARNING, purchases are 1 time, 1 only, no refunds\n")
    time.sleep(3)
    choice = input("Heal (10 hp): 50$ (1)\n\nAttack Boost (5 attacks): 80$ (2)\n\nMega Heal (25 hp): 120$ (3)\n\nExit Shop: free, or is it? (exit)\n\n").lower()
    if choice == '1' and cash >= 50:
        hpotion1 = hpotion1 + 1
        cash = cash - 50
        clear()
        print(f"Sucsesfully bought Healing Potion (10hp)")
        await shop()
    elif choice == '1' and cash <= 50:
        clear()
        print("Insufficient Funds")
        await shop()
    elif choice == '2' and cash >= 80:
        apotion1 = apotion1 + 1
        cash = cash - 80
        clear()
        print(f"Sucsesfully bought Attack Potion (5 atk)")
        await shop()
    elif choice == '2' and cash <= 80:
        clear()
        print("Insufficient Funds")
        await shop()
    elif choice == '3' and cash >= 120:
        hpotion2 = hpotion2 + 1
        cash = cash - 120
        clear()
        print(f"Sucsesfully bought Healing Potion (25hp)")
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


async def bag():
    global health
    global attack
    global hpotion1
    global hpotion2
    global hpotion3
    global hpotion4
    global apotion1
    global cash
    ui = input(f"Healing Potion 1 (10hp): {hpotion1}\nHealing Potion 2 (25hp): {hpotion2}\nHealing Potion 3 (50hp): {hpotion3}\nHealing Potion 4 (100hp): {hpotion4}\nAttack Potion 5 (5 atk): {apotion1}\nExit Bag (exit)\n\n")
    if ui == '1' and hpotion1 >= 1:
        hpotion1 = hpotion1 - 1
        health = health + 10
        print("Sucsesfully used item heal")
        print(f"Health: {health}")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '1' and hpotion1 <= 1:
        print("Insufficent Items")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '2' and hpotion2 >= 1:
        hpotion2 = hpotion2 - 1
        health = health + 25
        print("Sucsesfully used item heal")
        print(f"Health: {health}")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '2' and hpotion2 <= 1:
        print("Insufficent Items")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '3' and hpotion3 >= 1:
        hpotion3 = hpotion3 - 1
        health = health + 50
        print("Sucsesfully used item heal")
        print(f"Health: {health}")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '3' and hpotion3 <= 1:
        print("Insufficent Items")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '4' and hpotion4 >= 1:
        hpotion4 = hpotion4 - 1
        health = health + 100
        print("Sucsesfully used item heal")
        print(f"Health: {health}")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '4' and hpotion4 <= 1:
        print("Insufficent Items")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '5' and apotion1 >= 1:
        apotion1 = apotion1 - 1
        attack = attack + 5
        print("Sucsesfully used attack boost")
        print(f"Attack: {attack}")
        time.sleep(2)
        clear()
        await bag()
    elif ui == '5' and apotion1 <= 1:
        print("Insufficent Items")
        time.sleep(2)
        clear()
        await bag()
    elif ui == 'exit':
        print("Alright")
        time.sleep(2)
        clear()
    else:
        print("Invalid Response")
        time.sleep(2)
        clear()
        await bag()


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
    con1 = input("Welcome to the game, are you ready to begin your adventure, " + begin +"? ").lower()
    if con1 == 'yes':
        clear()
        await arc1()
    elif con1 == 'no':
        print("Come back when you're ready")
        time.sleep(2)
        sys.exit()
    elif con1 == 'devmode':
        dev = dev + 1
        await devchoice()
    else:
        print("Yes or no")
        await start()
asyncio.run(start())


