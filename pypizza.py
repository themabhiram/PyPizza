program_name = "    Welcome to PyPizza    "
print("="*len(program_name))
print(program_name)
print("="*len(program_name))
print()
pizza_size = input("Pizza size?\nSmall:15rs (S)\nMedum:20rs (M)\nLarge:25rs (L)\nSelect : ")
bill = 0
if pizza_size == "S":
    bill+=15
elif pizza_size == "M":
    bill+=20
elif pizza_size == "L":
    bill+=25
else:
    print("entered invalid option")

if pizza_size == "S":
    pepperoni_small = input("Add pepperoni just 2rs?\nY or N : ")
    if pepperoni_small == "Y":
        bill+=2
elif pizza_size == "M" or pizza_size == "L":
    pepperoni = input("Add pepperoni just 3rs?\nY or N : ")
    if pepperoni == "Y":
        bill+=3
else:
    print("entered invalid option.")

chesse = input("Extra chesse just 1rs?\nY or N : ")
if chesse == "Y":
    bill+=1
print(f"Your final bill : {bill} rs")
