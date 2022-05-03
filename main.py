"""
This is a list app, to create lists
"""

__author__ = "Fedmichard Francois"

checklists = {}


def addtochecklist():
    """
    function that allows you to add your newly created list
    :return:
    """
    numberinlist = int(input("-------------------------\nEnter how many items do you want in your checklist: "))
    list = []

    for i in range(numberinlist):  # creates a loop i many times and prompts the user to make their list
        item = input(f"-------------------------\nEnter item #{i + 1}: ")
        list.append(item)  # adds input to the list
    return list


def createchecklist():
    """
    function to create a checklist
    """
    print("\nLIST CREATION\n-------------------------")
    print("Select a tag for your checklist:\n-------------------------")
    checklisttagchoice = ['To do', 'Shopping', 'Inventory', 'Best of', 'Bucket']  # A tag for your checklist

    for i in range(len(checklisttagchoice)):
        print(f"{i + 1}. {checklisttagchoice[i]}")
    print('6. Main menu')
    checklisttag = input("-------------------------\nSelect an option: ")

    try:  # Added to prevent user from typing anything that's not a number
        if 1 <= int(checklisttag) <= 5:  # as long as the user input is between 1 and 5
            checklistname = input("-------------------------\nEnter a name for your list: ")
            checklistnamelist = addtochecklist()
            for i in range(len(checklisttagchoice)):
                if i + 1 == int(checklisttag):
                    uniquelistname = str(checklistname) + ':' + str(checklisttagchoice[i])
                    checklists[uniquelistname] = checklistnamelist
                    print("-------------------------\nList Created Successfully!\n-------------------------")

            goback = str(input("Type anything to create another list or 'q' to go to the main menu: "))

            if goback == 'q':  # sends back to main menu
                selectchecklist()
            else:
                createchecklist()

        elif checklisttag == '6':
            selectchecklist()

        else:
            print("Error... try again!")
            createchecklist()

    except ValueError:  # if the user inputs anything but a number, restart the function
        print("Error... try again!")
        createchecklist()


def selectchecklist():
    """
    allows you to select a checklist
    """
    while True:
        print(
            f"MAIN MENU\n-------------------------\nYou currently have {len(checklists)} checklists..."
            f"\n-------------------------\nSelect an option:\n-------------------------")
        print("1. Create list")
        print("2. Show check list")
        print("3. Delete a checklist")
        print("4. Add to a checklist")
        print("5. Exit")
        selectlist = input("\nSelect an option: ")

        if selectlist == '1':
            createchecklist()

        elif selectlist == '2':
            print('\nYour checklists:\n-------------------------')
            for i in checklists:
                print(
                    # split function divides string to list
                    f"{i.split(':')[0]} / {i.split(':')[1]} / {checklists[i]}")
            print('-------------------------')

        elif selectlist == '3':
            deletechecklist()

        elif selectlist == '4':
            editchecklist()

        elif selectlist == '5':
            print("Good bye!")
            exit()

        else:
            print("Error... try again!")


def deletechecklist():
    """
    deletes a already created checklist
    """
    print("Deletion\n-------------------------")
    print("1. Clear all")  # Option 1 will be to erase everything in check list
    print("2. Main Menu")
    option = 3

    for i in checklists:  # Prints all checklists formatted
        print(
            # split function divides string to list
            f"{option}. {i.split(':')[0]} / {i.split(':')[1]} / {checklists[i]}")
        option += 1

    selection = input("Which checklist would you like to delete: ")
    keys = list(checklists.keys())

    try:
        if selection == '1':
            checklists.clear()
            selectchecklist()

        if selection == '2':
            selectchecklist()

        elif 2 < int(selection) <= (len(keys) + 1):
            del checklists[keys[int(selection) - 2]]
            selectchecklist()

        else:
            print("Error... Try Again!")
            deletechecklist()

    except ValueError:
        print("Error... Try Again!")
        deletechecklist()

    deletechecklist()

    print(selection + " has been deleted!")


def editchecklist():
    """
    allows you to add more to an already created checklist
    """
    print("\nChecklist Add\n-------------------------")
    print("1. Return to Main Menu")
    print("2. Add to checklist")
    option = 1

    editchecklistoption = (input('-------------------------\nSelect an option: '))
    keys = list(checklists.keys())

    try:
        if editchecklistoption == '1':
            main()

        elif editchecklistoption == '2':
            for i in checklists:
                print(
                    # split function divides string to list
                    f"{option}. {i.split(':')[0]} / {i.split(':')[1]} / {checklists[i]}")
                option += 1

            checklisttoedit = (input('-------------------------\nWhich checklist would you like to add to?: '))

            if 1 <= int(checklisttoedit) <= (len(keys)):
                try:
                    newchecklistvalue = input('Type what you would like to add: ')
                    checklists[keys[int(editchecklistoption) - 2]].append(newchecklistvalue)
                    editchecklist()
                except ValueError:
                    print('Error... Try Again!')
                    editchecklist()

            else:
                print('Error... Try Again!')
                editchecklist()

        else:
            print('Error... Try Again!')
            editchecklist()

    except ValueError:
        print('Error... Try Again!')
        editchecklist()


def main():
    """
    The main function
    """
    selectchecklist()


main()
