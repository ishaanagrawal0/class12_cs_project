print("Welcome to \"The Vacation Connection\".")
a=input("Are you an old user, or a new user? Enter \"old\" for old user, and \"new\" for new user: ")

import sys

import csv
data=[]
with open("Database.csv","r") as f:
    csv_read=csv.reader(f)
    for row in csv_read:
        data.append(row)
data.pop(0)
#data now has all pre existing records.

f1=open("Custom.csv","a+",newline="")
check=[]  #has error, check once
csv_read1=csv.reader(f1)
for row in csv_read1:
    check.append(row)
print("check", check)
Fields=["Username","plan code","add ons"]
csv_writer=csv.writer(f1)
csv_writer.writerow(Fields)
custom=[]

def BOOKING():
    book = input("Do you want to book a new trip? Enter \"yes\" for new trip and \"no\" to exit: ")
    if book == "yes":
      cost = 0
      nostravels = 0
      while nostravels < 1 or nostravels > 20:
        print("Number of travelers must be less than 20")
        nostravels = int(input("Enter the number of travelers:"))
    new.append(nostravels)
    
    print("Press 1 for Mumbai.")
    print("Press 2 for Delhi.")
    start = input("Choose starting city: ")
    
    
    loc = input("Do you want to make an international or domestic booking? Enter \"int\" for International and \"dom\" for Domestic:  ")
    new.append(loc)
    
    if loc == "int":
      print("Select the destination you would like to travel to.")
      print("Press 1 for UAE.")
      print("Press 2 for Australia.")
      print("Press 3 for Singapore.")
      print("Press 4 for France & Germany.")
      I_dest = int(input("Enter destination code: "))
      new.append(I_dest)
      custom.append(I_dest)
    
      if I_dest == 1:
        print("You have decided to travel to The UAE.")
        print("The basic plan is 5D/4N.")
        print("The vanilla plan includes  Flight tickets, 2-night Hotel stay in Dubai with free breakfast.")
        cost = cost+40000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add dinner at the top of the Burj Khalifa ₹5000/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 5000
        AO_2 = input(
            "Press 102 to add show of Al Marmoon Camel Race. ₹3000/person")
        if AO_2 == "Y":
          cost += 3000
        AO_3 = input(
            "Press 103 to add an extra day (hotel included) ₹5000/person.")
        if AO_3 == "Y":
          cost += 5000
        AO_4 = input("Press 104 to add all meals. ₹5000/person")
        if AO_4 == "Y":
          cost += 5000
        AO_5 = input("Press 105 to add visit to Kite Beach. ₹1000/person")
        if AO_5 == "Y":
          cost += 1000
        AO_6 = input("Press 106 to add a visit to Ski Dubai. ₹3000/person")
        if AO_6 == "Y":
          cost += 3000
        AO_7 = input("Press 107 to add a visit to The Ethiad Museum. ₹2000/person")
        if AO_7 == "Y":
          cost += 2000
        cost = cost*nostravels
        print()
    
      elif I_dest == 2:
        print("You have decided to travel to Australia.")
        print("The basic plan is 6D/5N.")
        print("The vanilla plan includes  Flight tickets, 5-night Hotel stay in Sydney  with all meals covered.")
        cost = cost+90000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add 1 night cruise ₹7500/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 5000
        AO_2 = input(
            "Press 102 to add scuba diving in the Great Barrier Reef. ₹3000/person")
        if AO_2 == "Y":
          cost += 1500
        AO_3 = input(
            "Press 103 to add an extra day (hotel included) ₹5000/person.")
        if AO_3 == "Y":
          cost += 2000
        AO_4 = input("Visit to Ayers Rock (Uluru). ₹3000/person")
        if AO_4 == "Y":
          cost += 1000
        cost = cost*nostravels
        print()
    
      elif I_dest == 3:
        print("You have decided to travel to Singapore.")
        print("The basic plan is 5D/4N.")
        print("The vanilla plan includes  Flight tickets, hotel stay, and zoo visit.")
        cost = cost+45000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add Universal Studios visit ₹5000/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 1000
        AO_2 = input("Press Y to add cruise ₹15000/person or press N to skip.: ")
        if AO_2 == "Y":
          cost += 1000
        AO_3 = input(
            "Press Y to add an extra day (hotel included) ₹5000/person or press N to skip.: ")
        if AO_3 == "Y":
          cost += 3000
        AO_4 = input("Press Y to add all meals ₹1000/person or press N to skip.: ")
        if AO_4 == "Y":
          cost += 1000
        AO_5 = input(
            "Press Y to add Sentosa Island visit ₹2000/person or press N to skip")
        cost = cost*nostravels
        print()
    
      elif I_dest == 4:
        print("You have decided to travel to France.")
        print("The basic plan is 5D/4N.")
        print("The vanilla plan includes  Flight tickets, 2-night Hotel stay in Paris with free breakfast.")
        cost = cost+70000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add dinner at the top of the Eiffel Tower ₹5000/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 5000
        AO_2 = input("Press 102 to add Seine River Cruise in Paris. ₹3000/person")
        if AO_2 == "Y":
          cost += 3000
        AO_3 = input(
            "Press 103 to add an extra day (hotel included) ₹5000/person.")
        if AO_3 == "Y":
          cost += 5000
        AO_4 = input("Press 104 to add all meals. ₹10000/person")
        if AO_4 == "Y":
          cost += 10000
        AO_5 = input("Press 105 to add guided buss tour of Paris. ₹2000/person")
        if AO_5 == "Y":
          cost += 2000
        AO_6 = input("Press 106 to add a visit to The Notre Dame. ₹1000/person")
        if AO_6 == "Y":
          cost += 1000
        AO_7 = input("Press 107 to add a visit to The Louvre. ₹2000/person")
        if AO_7 == "Y":
          cost += 2000
        cost = cost*nostravels
        print()
    
    elif loc == "dom":
      print("Select the destination you would like to travel to.")
      print("Press 1 for Goa.")
      print("Press 2 for Meghalaya.")
      print("Press 3 for Andaman & Nicobar Islands.")
      print("Press 4 for Rajasthan.")
      D_dest = int(input("Enter destination code: "))
      new.append(D_dest)
      custom.append(D_dest)
    
      if D_dest == 1:
        print("You have decided to travel to Goa.")
        print("The basic plan is 3D/2N.")
        print("The vanilla plan includes  Flight tickets, 2-night Hotel stay in Panaji with free breakfast.")
        cost = cost+9000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add 1 night cruise ₹5000/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 5000
        AO_2 = input("Press 102 to add scuba diving. ₹1500/person")
        if AO_2 == "Y":
          cost += 1500
        AO_3 = input(
            "Press 103 to add an extra day (hotel included) ₹2000/person.")
        if AO_3 == "Y":
          cost += 2000
        AO_4 = input("Press 104 to add all meals. ₹1000/person")
        if AO_4 == "Y":
          cost += 1000
        cost = cost*nostravels
        print()
    
      elif D_dest == 2:
        print("You have decided to travel to Meghalaya.")
        print("The basic plan is 5D/4N.")
        print("The vanilla plan includes  Flight tickets, 2-night Hotel stay in Shillong, 2-night Hotel stay in Cherrapunji, and all meals (vegetarian).")
        cost = cost+20000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add tour guide(English/Hindi) ₹750/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 750
        AO_2 = input(
            "Press Y to add Mawlynnong visit (cleanest village) ₹1500/person or press N to skip.:")
        if AO_2 == "Y":
          cost += 1500
        AO_3 = input(
            "Press Y to add an extra day (hotel included) ₹3000/person or press N to skip.:")
        if AO_3 == "Y":
          cost += 3000
        AO_4 = input(
            "Press Y to add upgrade meals to non-veg ₹500/person or press N to skip.:")
        if AO_4 == "Y":
          cost += 500
        cost = cost*nostravels
        print()
    
      elif D_dest == 3:
        print("You have decided to travel to the Andman and Nicobar Islands.")
        print("The basic plan is 4D/3N.")
        print("The vanilla plan includes  Flight tickets, 3-night Hotel stay in Port Blair with all meals covered.")
        cost = cost+15000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add 1 night cruise ₹5000/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 5000
        AO_2 = input("Press Y to add scuba diving. ₹1500/person")
        if AO_2 == "Y":
          cost += 1500
        AO_3 = input("Press  to add an extra day (hotel included) ₹2000/person.")
        if AO_3 == "Y":
          cost += 2000
        AO_4 = input("Press Y Visit to Cellular Jail. ₹300/person")
        if AO_4 == "Y":
          cost += 1000
        cost = cost*nostravels
        print()
    
      elif D_dest == 4:
        print("You have decided to travel to Rajasthan.")
        print("The basic plan is 5D/4N.")
        print("The vanilla plan includes  Flight tickets, hotel stays in Jaipur, Ajmer, Bikaner, and Mount Abu respectively.")
        cost = cost+10000  # Flight + Hotel
    
        print("Now you will be prompted to choose the add-ons.")
        AO_1 = input(
            "Press Y to add choki dhani, Jaipur visit ₹1000/person or press N to skip.: ")
        if AO_1 == "Y":
          cost += 1000
        AO_2 = input(
            "Press Y to add camel safari ₹1000/person or press N to skip.: ")
        if AO_2 == "Y":
          cost += 1000
        AO_3 = input(
            "Press Y to add an extra day (hotel included) ₹2500/person or press N to skip.: ")
        if AO_3 == "Y":
          cost += 3000
        AO_4 = input("Press Y to add all meals ₹1000/person or press N to skip.: ")
        if AO_4 == "Y":
          cost += 1000
        AO_5 = input(
            "Press Y to add tour guide (English/Hindi) ₹750/person or press N to skip")
        cost = cost*nostravels
        print()
    
      else:
        print("Invalid")
    else:
      print("Invalid")

def check():
        username=input("Enter username: ")
        password=input("Enter password: ")
        verify=0
        for i in data[1::]:
            for j in i:
                if j[1]==username:
                    if j[2]==password:
                        print("You have successfully logged in.")
                    else:
                        print("incorrect password")
                        quit()
                else:
                    print("User does not exist. Make a new user.")
                    quit()
check()



if a=="old":
    username=input("Enter username: ")
    password=input("Enter password: ")
    verify=0
    
    for i in data:
        if i[1]==username:
            if i[2]==password:
                print("You have successfully logged in.")
                verify=1
            else:
                print("incorrect password, restart login.")
                sys.exit()
    if verify==0:
        print("User does not exist. Make a new user.")
        sys.exit()
    #MatchOldData
    #ChangesInData

elif a=="new":
    new=[]
    for i in data:
        x=int(i[0])
    x=x+1
    new.append(x)
    newusername =input("Create Your Username:  ")
    for i in data:
        if i[1]==newusername:
            print("User already exists, choose old user at the beginning.")
            print("One user can only do 1 booking per account, create a new one for second booking.")
            sys.exit()
    new.append(newusername)
    newpassword=""
    while len(newpassword)<4:
        print("Password must have atleast 4 characters")
        newpassword= input("Create a secure password (Minimum 4 characters) :   ")
    new.append(newpassword)
    newname = input("Enter Your Name: ")
    new.append(newname)
    newage  = int(input("Enter Your Age:  "))
    new.append(newage)
    newcontact=int(input("Enter Your Contact Number: "))
    new.append(newcontact)
    custom.append(newusername)