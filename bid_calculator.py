loop=True
bid={}
while loop is not False:
    name=input("Enter you name: ")
    bid_value=int(input("Enter your bid:$"))
    bid[name]=bid_value

    heighest_bid=0
    lucky_name=""
    check=input("Do you want another person for bid?").lower()
    if check=="no":
        loop= False

    for name in bid:
        if bid[name]>heighest_bid:
            heighest_bid=bid[name]
            lucky_name=name

print(f"{lucky_name} won the bid as he offered {heighest_bid} $")

