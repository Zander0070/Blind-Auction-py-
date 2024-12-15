Buyers = {}


#print(art.logo) # displaying art work
print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
bflag = False

while bflag == False:
    key_name = input("Please enter your name") # step 1
    bid_value = int(input('Please enter your bid')) # step 2

    Buyers[key_name] = bid_value

    print("\n" * 20 )

    Choice = input("Are there any other bidders? yes/no")
    if Choice.lower() == "yes":
        bflag = False
    elif Choice.lower() == "no":
        bflag = True
    else:
        print("stop taking my program for a joke")



#for I in Buyers:
 #   Bid = max(Buyers[I])
    Highest_num = max(Buyers, key=Buyers.get)


#Highest_value = max(Buyers, key=Buyers.get)

print(f"The highest bidder is {Highest_num} with a bid of {Buyers[Highest_num]}")
