
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
BP=0
if size == "S":
  BP += 15
elif size == "M":
  BP += 20
else:
  BP += 25

if add_pepperoni == "Y":
  if size == "S":
    BP+=2   
  else:
    BP+=3
  
if extra_cheese =="Y":
    BP+=1
    
print(f"Your final bill is: ${BP}")



