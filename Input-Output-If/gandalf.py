"""
File : gandalf.py
Date : 02/13/2023
"""

race = input("Which race are you? (Human,dwarf,elf,maiar,hobbit) ")

if race.lower() == "human":
   king = input("Are you the King of Gondor? ")
   if king.lower() == "yes":
       print("You are Aragorn ! Son of Arathorn !")
   else:
       ring_take = input("Did you try to take the ring from Frodo? ")
       if ring_take.lower() == "yes":
           print("You are Boromir !! ")
       else:
           print("You are Theoden ! ....probably ")
elif race.lower() == "dwarf":
    print("You are Gimli ! Son of Gloin !")
elif race.lower() == "elf":
    matrix = input("Were you in the Matrix? ")
    if matrix.lower() == "yes":
        print("You are Elrond ! ")
    else:
        print("You are Legolas ! ")
elif race.lower() == "maiar":
    good_or_evil = input("Are you good or evil? ")
    if good_or_evil.lower() == "good":
        print("You are Gandalf !!!")
    else:
        forge_ring = input("Did you forge the One Ring?")
        if forge_ring.lower() == "yes":
            print("You are Sauron. Heh. ")
        else:
            print("You are the mighty ranger SARUMAN !!!")
elif race.lower() == "hobbit":
    carry_ring = input("Do you carry the One Ring? ")
    if carry_ring.lower() == "yes":
        print("You are Frodo Baggins.")
    else:
        gardener = input("Are you a gardener? ")
        if gardener.lower() == "yes":
            print("You are Samwise !")
        else:
            print("You're either Merry or Pippin !")
else:
    print("You are an Orc")
