# date : 31/03/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question - Q4

# * * An IPO Diagram for the following game is available on the word document * *

# * * * * * * * * * * question 4) * * * * * * * * * *


#This module will add pausing to the game
import time 

#Built-in mutable sequence.
#This is how the users will be able to respond
answer_1 = ["1"]
answer_2 = ["2"]
answer_3 = ["3"]
answer_4 = ["4"]
answer_5 = ["5"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Convert string to an integer
#objects
knife = 0
vaccine = 0

required = ("\n**Use only 1, 2, 3, 4, or 5**\n") #This shortens duplication

#The game is broken into sections, starting with intro.
def intro():
  print ("""The night after a high-profile party, you awaken the
  next morning in a hotel room. Head spinning and
  fighting the urge to vomit, you stand and marvel at your new,
  unfamiliar setting. The peace quickly fades when you hear a
  grotesque sound emitting from the bathroom. A slobbering zombie is
  coming towards you. You will:""")
  #Delays execution for 1 second
  time.sleep(1)
  print ("""  1. Grab the nearby lamp and throw it at the zombie
  2. Lie down on your bed and wait to be eaten
  3. Run out the hotel room""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_1:
    option_lamp()
  elif choice in answer_2:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_3:
    option_run()
  else:
    print (required)
    intro()


def option_lamp(): 
  print ("\nThe zombie is stunned, but regains control. She begins "
  "walking towards you again. Will you:")
  time.sleep(1)
  print ("""2. Throw another lamp
  3. Run towards the kitchen""")
  choice = input(">>> ")
  if choice in answer_1:
    print ("\nYou decided to throw another lamp, as if the first " 
    "lamp thrown did much damage. The lamp flew well over the "
    "zombie's head. You missed. \n\nYou died!")
  elif choice in answer_3:
    option_kitchen()
  else:
    print (required)
    option_lamp()


def option_kitchen():
  print ("\nYou were hesitant, since the kitchen was close to the zombie, "
  "Before you fully enter, you notice a shiny knife on "
  "the kitchen counter. Do you pick up a knife. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    knife = 1 #adds a knife
  else:
    knife = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  1. Hide in silence behind the kitchen counter
  2. Fight
  4. Walk into the pantry room and lock the door
  5. Open the kitchen cupboard and hide in it""")
  choice = input(">>> ")
  if choice in answer_1:
    print ("\nReally? You're going to hide in behind the counter? I think "
    "the zombie saw you, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_2:
   if knife > 0:
    print ("\nYou look at the zombie, The shimmering knife attracted "
    "the zombie, which thought you were no match. As she walked "
    "closer and closer, your heart beat rapidly. As the zombie "
    "reached out to eat you, you pierced the knife into "
    "its head, puncturing the brain. \n\nYou survived!")
   else: #If the user didn't grab the knife
     print ("\nYou should have picked up that knife. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_4:
    print ("You quickly run into the pantry room, "
    "you lock the door behind you.")
    option_pantry()
  elif choice in answer_5:
    print ("You quickly open and hide in the cupboard.")
    option_cupboard()
  else:
    print (required)
    option_kitchen()

# This is the child and leaf node which reverts back 2 nodes i,e to the beggining of the game.
def option_pantry(): 
  print ("\nYou turn around and see a time machine "
    "your vision starts to blur.")
  time.sleep(1)
  print ("""  1. You have only 1 choice. Close your eyes as you are 
  teleported back to the beginning. """)
  choice = input(">>> ")
  if choice in answer_1:
    intro()
  else:
    print (required)
    option_pantry()

# This is the 2nd child and leaf node which reverts back 2 nodes i,e to the beggining of the game.
def option_cupboard(): 
  print ("""\nWhile inside the cupboard, you notice a tiny mechanism, 
  It's a tiny time machine.
  You see two buttons on the mechanism, one says Beach
  and the other button says Past. You assume you will be teleported to 
  these locations, which button do you press?""")
  time.sleep(1)
  print (""" 1. Beach 
  2. Past """)
  choice = input(">>> ")
  if choice in answer_1:
    option_beach()
    if choice in answer_2:
      option_past()
    else:
        print (required)
        option_cupboard()

#this is a child node
def option_beach():
  print ("""\nYour vision starts to blur, you close your eyes as your 
  surrounding starts to quake,seconds later the quaking stops. 
  You open your eyes and open the cupboard, You squint as a bright light
  hits you in the eyes, as you adjust your eyes
  you see a vast ocean in the distance, a sandy beachside, you look down
  and you see you are sunbathing, what do you do next? """)
  time.sleep(1)
  print ("""  1. Relax, and take in the moment
  2. You look behind you and see the machine, it only has one button now,
  press it? """)
  choice = input(">>> ")
  if choice in answer_1:
    print ("\n\nYou Survived!")
  elif choice in answer_2:
    print ("""\nYour vision starts to blur as you are teleported inside 
    the elevator. """)
    option_fall2()
  else:
    print (required)
    option_beach()


def option_past():
  print ("""\nYou are teleported 1 year prior to the zombie incident, what 
  do you do next? """)
  time.sleep(1)
  print (""" 1. Relax, and take in the moment and
  2. You look behind you and see the machine, it only has one button now, press it? """)
  choice = input(">>> ")
  if choice in answer_1:
    print ("\n\nYou Survived!")
  elif choice in answer_2:
    print ("""\nYou press the button and are returned to the hotel room
    level. """)
    option_room()
  else:
    print (required)
    option_past()

#this is the easter egg node which repeats a previous node but now has an extra option
def option_fall2():
  print ("\nYour vision adjusts, and you are now back in the elevator")
  time.sleep(1)
  print ("""  1. Press the ground floor button
  2. Press the Roof button
  3. Sit down, contemplate life and get ready to die
  4. Interesting, there is a new button, it has nothing written on it, 
  press it? """)
  choice = input(">>> ")
  if choice in answer_1:
    print ("""\nYou press the ground floor button, the elevator shakes and 
    free falls. \n\nYou died!""")
  elif choice in answer_2:
    print ("""\nYou press the roof button, the elevator shakes and free 
    falls. \n\nYou died!""")
  elif choice in answer_3:
    print ("""\nYou close your eyes, relive your memories in a blink of a 
    second and suffer a painful death. \n\nYou died!""")
  elif choice in answer_4:
    print ("""\nYou press the new button, you instantly wake up! It was 
    all but a dream!. \n\nYou Survived!""")
  else:
    print (required)
    option_fall2()


def option_run():
  print ("\nYou run as quickly as possible, but the zombie's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  1. Hide behind the door
  2. Cornered, so you fight
  4. Run into the elevator
  5. Run into another hotel room""")
  choice = input(">>> ")
  if choice in answer_1:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_2:
    print ("\nYou're no match for the zombie. "
    "\n\nYou died!")
  elif choice in answer_4:
    option_fall()
  elif choice in answer_5:
    option_room()
  else:
    print (required)
    option_run()

#the following node has no alternatives other than death, this is also a child node
def option_fall(): 
  print ("""\nYou enter the elavator, the zombie is coming. What do you 
  do next?""")
  time.sleep(1)
  print ("""  1. Press the ground floor button
  2. Press the Roof button
  3. Sit down, contemplate life and get ready to die.""")
  choice = input(">>> ")
  if choice in answer_1:
    print ("""\nYou press the ground floor button, the elevator shakes 
    and free falls. \n\nYou died!""")
  elif choice in answer_2:
    print ("""\nYou press the roof button, the elevator shakes and free 
    falls. \n\nYou died!""")
  elif choice in answer_3:
    print ("""\nYou close your eyes, relive your memories in a blink of a 
    second and suffer a painful death. \n\nYou died!""")
  else:
    print (required)
    option_fall()

#this is a child node
def option_room(): 
  print ("""\nYou enter one of the hotel rooms in the corrdior and close 
  the door behind you. What do you do next?""")
  time.sleep(1)
  print ("""  1. Go into the bedroom
  2. Go into the bathroom 
  3. Open the front door again and run towards the elevator again""")
  choice = input(">>> ")
  if choice in answer_1:
    print ("""\nYou open the bedroom door and instantly get mauled to 
    death by a zombie. \n\nYou died!""")
  elif choice in answer_2:
    print ("""\nYou open the bathroom door and instantly get mauled to 
    death by a zombie. \n\nYou died!""")
  elif choice in answer_3:
    option_elevator()
  else:
    print (required)
    option_room()


def option_elevator():
  print ("\nWhile frantically running, you notice a rusted "
  "knife lying in the corrdior. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind baggage, waiting for the zombie to come "
  "charging around the corner. You notice a vial labelled vacine "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    vaccine = 1 #adds a vial of vaccine
  else:
    vaccine = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending zombie.")
  time.sleep(1)
  if vaccine > 0:
    print ("\nYou quickly inject the zombie with the vaccine, somehow "
    "hoping it will stop the zombie. It does! The zombie "
    "returned to human. "
    "\n\nYou survived!")
  else: #If the user did not grab the knife
     print ("\nMaybe you should have picked up the vaccine. "
     "\n\nYou died!")

intro()