print("welcome to mini banking app".title())

basic_info={
    "name":"soban",
    "age":21,
    "city":"Lahore",
    "acc_no": 2021,
    "branch":"main",
    "account_type":"premium",
    "bank_pin_code" :8431,
}

initial_balance=0
password=int(input("enter your password to log in\n".title()))
if password ==1234:
    loop=True
    while loop:
        choice=int(input("---Welcome which feture you want to access---\n1.Show info\n2.add balance\n3.show balance\n".title()))
        if choice==1:
            print(basic_info)

        elif choice==2:
            deposited_amount =int(input("Enter amount you want to deposit".title()))
            initial_balance+=deposited_amount
            print(f"{deposited_amount} is deposited successfully".title())

        elif choice ==3:
            if initial_balance >0:
                print(f"{initial_balance} is your current balance")

        else:
            print("Invalid choice".title())
        last_choice=input("Do you want to perform another request y for yes?").lower()
        if last_choice=="n":
            loop=False

    print("Thank you for using mini banking app".title())
else:
    print("Wrong passsword Try again later".title())