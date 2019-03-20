bid=0
print("Welcome to the Auction House!!!!!!!")
print("How many items are in this auction?")
nomitems=int(input())

while nomitems <0:
    print("There needs to be atleast 10 items")
    nomitems=int(input())


#ARRAYS
ItemNo = []
Bids = []
Desc = []
Reserve = []
NomBids=[]
Highest_bid=[]
Highest_bidder=[]


#--------------------------TASK 1---------------------------------------------------------------


for i in range (0,nomitems):
    print("Here are the ID numbers \n",i+1)
    newitemno = i
    ItemNo.append(newitemno)

    
for i in range (0,nomitems):
    print("Enter the description",i+1,":")
    description = input()
    Desc.append(description)

for i in range (0,nomitems):
    print("Enter the reserve prices",i+1,":")
    rprice = int(input())
    Reserve.append(rprice)



#GMN Added this
for i in range (0,nomitems):
    NomBids.append(0)
    

#take this out - you dont need this when on task 2
for i in range (0,nomitems):
    print("\nItem",i+1)
    print("Item Number",ItemNo[i])
    print("Description",Desc[i])
    print("Reserve price",Reserve[i])
    print("Number of bids",NomBids)
    

#---------------------------TASK 2 ------------------------------------------------------------

print("First of all what would you like your buyer id to be?")
buyerid = input()
print("Your buyer id is,",buyerid)
print("Welcome to the auction house,\nwould you like to buy any items?")
answer1 = input()
answer1 = "yes"


#GMN Added this- as all highest bids are set to 0, because no one has bidded yet!!
for i in range (0,nomitems):
    Highest_bid.append(0)



while answer1 == "yes":
    print("Here are the list of the items up for sale")
    for i in range (0,nomitems):
        print("\nItem",i+1)
        print("Item Number",ItemNo[i])
        print("Description",Desc[i])
        print("Reserve price",Reserve[i])
        print("Number of bids",NomBids[i])
        print("Highest bid",Highest_bid[i])
    print("What item would you like to buy? Enter the item number")
    item = int(input())
    indexID = ItemNo.index(item)
    print("This is your item,",Desc[indexID])
    print("What is your bid?")
    currentbid = int(input())
    if currentbid > Highest_bid[indexID]:
        print("You are now the highest bidder")
        Highest_bid[indexID] = currentbid
        NomBids[indexID] = + 1
    else:
        print("This bid is not high enough")
        NomBids[indexID] = + 1
        print("Would you like to bid again")
        answer1 = input()
    print("Would you like to bid for another item?")
    answer1 = input()



#--------------------------------------Task 3-----------------------------------------
unsold = []
Totalfee = []
Solditems = []
newreserve = []
for i in range (0,nomitems):
    if Highest_bid[i] >= Reserve[i]:
        Solditems.append(Desc[i])
    else:
        unsold.append(Desc[i])
   

print("These are all of the sold items,",Solditems)
print("These are all of the unsold items,",unsold)

for i in range (0,nomitems):
    if NomBids[i] >= 1:
        print("These are all of the sold items and their prices + the 10% fee",Solditems[i],Reserve[i]*1.1)

for i in range (0,nomitems):
    if Highest_bid[i] < Reserve[i]:
        print("Here is the item number and bid for the items that have not reached the reserve price and are not sold,",ItemNo[i],Highest_bid[i])


print("Thankyou for for your visit!")

    

    
    
              
