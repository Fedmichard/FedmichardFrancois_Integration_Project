# Fedmichard Francois
# This is a list app, to create lists

checklists = {}

def addToChecklist(): # function that allows you to add to your newly created list
    numberInList = int(input("-------------------------\nEnter how many items do you want in your checklist: "))
    list = []

    for i in range(numberInList): # creates a loop i many times and prompts the user to make their list
        item = input(f"-------------------------\nEnter item #{i + 1}: ")
        list.append(item) # adds input to the list
    return list

def createChecklist(): # function to create a checklist
    print("\nLIST CREATION\n-------------------------")
    print("Select a tag for your checklist:\n-------------------------")
    checklistTagChoice = ['To do', 'Shopping', 'Inventory', 'Best of', 'Bucket'] # A tag for your checklist

    for i in range(len(checklistTagChoice)):
        print(f"{i + 1}. {checklistTagChoice[i]}")
    print('6. Main menu')
    checklistTag = input("-------------------------\nSelect an option: ")

    try: # Added to prevent user from typing anything that's not a number
        if int(checklistTag) >= 1 and int(checklistTag) <= 5: # as long as the user input is between 1 and 5
            checklistName = input("-------------------------\nEnter a name for your list: ")
            checklistNameList = addToChecklist()
            for i in range(len(checklistTagChoice)):
                if i + 1 == int(checklistTag):
                    uniqueListname = str(checklistName) + ':' + str(checklistTagChoice[i])
                    checklists[uniqueListname] = checklistNameList
                    print("-------------------------\nList Created Successfully!\n-------------------------")

            goBack = str(input("Type anything to create another list or 'q' to go to the main menu: "))

            if goBack == 'q': # sends back to main menu
                selectChecklist()
            else:
                createChecklist()

        elif checklistTag == '6':
            selectChecklist()

        else:
            print("Error... try again!")
            createChecklist()

    except ValueError: # if the user inputs anything but a number, restart the function
        print("Error... try again!")
        createChecklist()

def selectChecklist(): # allows you to select a checklist
    while True:
        print(f"\nMAIN MENU\n-------------------------\nYou currently have {len(checklists)} checklists...\n-------------------------\nSelect an option:")
        print("1. Create list")
        print("2. Show check list")
        print("3. Delete from checklist")
        print("4. Close app")
        selectList = input("\nSelect an option: ")

        if selectList == '1':
            createChecklist()

        elif selectList == '2':
            print('\nYour checklists:\n-------------------------\n')
            for i in checklists:
                print(f"{i.split(':')[0]} \t\ {i.split(':')[1]} \t\ {checklists[i]}") # split function divides string to list

        elif selectList == '3':
            deleteCheckList()

        elif selectList == '4':
            print("Good bye!")
            break

        else:
            print("Error... try again!")

def deleteCheckList():
    print("Deletion\n-------------------------")
    print("1. Clear all") # Option 1 will be to erase everything in check list
    option = 2

    for i in checklists: # Prints all checklists formatted
        print(f"{option}. {i.split(':')[0]} \t\ {i.split(':')[1]} \t\ {checklists[i]}") # split function divides string to list
        option += 1

    selection = input("Which checklist would you like to delete from?: ") #
    keys = list(checklists.keys())

    try:
        if selection == '1':
            checklists.clear()
            selectChecklist()

        elif int(selection) > 1 and int(selection) <= (len(keys) + 1):
            del checklists[keys[int(selection) - 2]]
            selectChecklist()

        else:
            print("Error... Try Again!")
            deleteCheckList()

    except ValueError:
        print("Error... Try Again!")
        deleteCheckList()

    deleteCheckList()

    print(selection + " has been deleted!")

def main(): # Main function
    selectChecklist()

main()