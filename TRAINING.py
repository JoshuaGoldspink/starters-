#show current food
with open('DATABASE1', 'r') as file:
    f = file.read()
print("The current food list is: " + "\n" + f)
file.close()
with open("Calories", "r") as calories_before:
    c = int(calories_before.read())
print("Total current calories is " + str(c))



#add foods
while input("anything else? (yes/no)") == "yes":
    with open("DATABASE1", "a") as myfile:
        myfile.write( "\n" + input("what did you buy ten you fat punk: "))
    c = c + int(input("How many calories was that? "))
with open("Calories", "w") as cfinal:
    cfinal.write(str(c))


# show final list
with open("DATABASE1", "r") as myfinal:
    final = myfinal.read()
    myfinal.close()



print("The final list is: " + "\n" + final)
print("TOTAL CALORIES= " + str(c))












