resource={
    "Water":300,
    "Milk": 200,
    "Coffee": 100,
    "Money":0,

}

loop= True

penny=0.01
dime=0.10
nickel=0.05
quarter=0.25



while loop:
    total_inserted_value=0

    user_choice=input("What would you like? 1.espresso 2.latte 3.cappuccino-Type 'report' for resources: ".title()).lower()

    if user_choice=="report":
        print(f"Water is {resource['Water']}ml".title())
        print(f"Milk is {resource['Milk']}ml".title())
        print(f"Coffee is {resource['Coffee']}g".title())
        print(f"Money is ${resource['Money']}".title())
        print("----------------------------------------")

    elif user_choice == "1": #espresso
        if resource["Water"]>=50 and resource["Coffee"] >=18:
            print("Your total bill is 1.50$".title())
            print("please insert coins".title())
            quarter_input=int(input("How many quarters:"))
            dime_input=int(input("How many dime:"))
            nickel_input=int(input("How many nickel:"))
            penny_input=int(input("How many penny:"))
            
            total_inserted_value=round((quarter_input*quarter)+(dime_input*dime)+(nickel_input*nickel)+(penny_input*penny),2)
            print(f"total inserted amount is {total_inserted_value} $")
            if total_inserted_value <1.50:
                print("insufficient amount entered")
            elif total_inserted_value >1.50:
                change=round(total_inserted_value-1.50,2)
                print(f"{change} is your change")
                print("Enjoy our coffee!!!")

                resource["Water"] -= 50
                resource["Coffee"] -= 18
                resource["Money"] += 1.50

            elif total_inserted_value == 1.50:
                print("Money deposit successfull!!")
                print("Enjoy our coffee!!!")
            
                resource["Water"] -= 50
                resource["Coffee"] -= 18
                resource["Money"] += 1.50

        else:
            print("Not much resources available!")

    elif user_choice == "2": #lattee
        if resource["Water"]>=200 and resource["Coffee"] >=24 and resource["Milk"]>=150:
            print("Your total bill is 2.50$".title())
            print("please insert coins".title())
            quarter_input=int(input("How many quarters:"))
            dime_input=int(input("How many dime:"))
            nickel_input=int(input("How many nickel:"))
            penny_input=int(input("How many penny:"))
                        
            total_inserted_value=round((quarter_input*quarter)+(dime_input*dime)+(nickel_input*nickel)+(penny_input*penny),2)
            print(f"total inserted amount is {total_inserted_value} $")
            if total_inserted_value <2.50:
                print("insufficient amount entered")
            elif total_inserted_value >2.50:
                change=round(total_inserted_value-2.50,2)
                print(f"{change} is your change")
                print("Enjoy our coffee!!!")

                resource["Water"] -= 200
                resource["Milk"] -= 150
                resource["Coffee"] -= 24
                resource["Money"] += 2.50

            elif total_inserted_value == 2.50:
                print("Money deposit successfull!!")
                print("Enjoy our coffee!!!")

                resource["Water"] -= 200
                resource["Milk"] -= 150
                resource["Coffee"] -= 24
                resource["Money"] += 2.50


        else:
                    print("Not much resources available!")

    elif user_choice =="3": #cappuccino
        if resource["Water"]>=250 and resource["Coffee"] >=24 and resource["Milk"]>=100:
            print("Your total bill is 3.00$".title())
            print("please insert coins".title())
            quarter_input=int(input("How many quarters:"))
            dime_input=int(input("How many dime:"))
            nickel_input=int(input("How many nickel:"))
            penny_input=int(input("How many penny:"))
                                
            total_inserted_value=round((quarter_input*quarter)+(dime_input*dime)+(nickel_input*nickel)+(penny_input*penny),2)
            print(f"total inserted amount is {total_inserted_value} $")
            if total_inserted_value <3.00:
                print("insufficient amount entered")
            elif total_inserted_value >3.00:
                change=round(total_inserted_value-3.00,2)
                print(f"{change} is your change")
                print("Enjoy our coffee!!!")

                resource["Water"] -= 250
                resource["Milk"] -= 100
                resource["Coffee"] -= 24
                resource["Money"] += 3.00
            elif total_inserted_value == 3.00:
                print("Money deposit successfull!!")
                print("Enjoy our coffee!!!")

                resource["Water"] -= 250
                resource["Milk"] -= 100
                resource["Coffee"] -= 24
                resource["Money"] += 3.00
        else:
            print("Not much resources available!")

    elif user_choice =="off":
        loop=False