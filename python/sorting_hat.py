# harry potter gang. you wasnt there reading the fourth book in a day

# Initialize points for each house
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Question 1
print("Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk")
answer1 = int(input("Your answer (1/2): "))
if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

# Question 2
print("When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")
answer2 = int(input("Your answer (1-4): "))
if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Question 3
print("Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum")
answer3 = int(input("Your answer (1-4): "))
if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4
elif answer3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Determine the house with the most points
max_points = max(gryffindor, hufflepuff, ravenclaw, slytherin)
if max_points == gryffindor:
    print("Gryffindor!")
elif max_points == hufflepuff:
    print("Hufflepuff!")
elif max_points == ravenclaw:
    print("Ravenclaw!")
elif max_points == slytherin:
    print("Slytherin!")
