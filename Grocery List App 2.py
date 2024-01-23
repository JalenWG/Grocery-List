#Jalen Grimes  
# 01/23/2024
#Grocery List 2

#Functions 

def grocerylistapp(): 
    glist=[]
    print(" 1. Add an item to the grocery list \n 2. View current list \n 3. Check item off \n 4. Remove item from list \n 5. Remove all items \n 6. Sort list alphabetically \n 7. Print the number of items on list \n 8. Exit list ")
    while True:
        ans= int(input(" Insert the number corresponding to the option you choose"))
        
        if ans== 1:
            newitem= str(input("What item do you want to add to the list?"))
            glist.append(newitem)
        elif ans== 2: 
            print(glist)
        elif ans== 3: 
            checkitem= str(input("Which item do you want to check off?"))
            itemposition= (glist.index(checkitem))
            glist.pop(itemposition)
            glist.insert(itemposition, checkitem +"X")
        elif ans== 4: 
            olditem= str(input("Which item do you want to remove from the list?"))
            glist.remove(olditem)
        elif ans== 5: 
            glist.clear()
        elif ans== 6: 
                glist.sort() 
        elif ans== 7:
             print(len(glist))
        elif ans== 8:
            break
        else: 
            print("Not valid selection")
            grocerylistapp()





#Main
grocerylistapp()