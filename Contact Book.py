print("   _____            _             _     ____              _    ")
print("  / ____|          | |           | |   |  _ \            | |   ")
print(" | |     ___  _ __ | |_ __ _  ___| |_  | |_| | ___   ___ | | __")
print(" | |    / _ \| '_ \| __/ _` |/ __| __| |  _ < / _ \ / _ \| |/ /")
print(" | |___| |_| | | | | || |_| | |__| |_  | |_| | |_| | |_| |   < ")
print("  \_____\___/|_| |_|\__\__,_|\___|\__| |____/ \___/ \___/|_|\_\)")
print("________________________________________________________________________")

# Contact book storing information
contact_list = []
# Number of contacts in the book
number_of_contacts = 0
# Flag to indicate if the user has completed using the contact book
completed = False

# Function to print the contact list
def print_list():
    print("")
    print("Your Contact Book")
    print("_____________________________")
    for i in range(number_of_contacts):
        # Printing each contact's details
        print(str(i+1) + "|  Name: " + str(contact_list[i][1]) + ",  Address: " + str(contact_list[i][2]) + ",  Phone: " + str(contact_list[i][3]) + ",  Email: " + str(contact_list[i][4]))
    print("")

# Function to add a contact to the contact book
def add_contact():
    global number_of_contacts
    global contact_list
    # Getting contact details from the user
    add_name = input("  What is their name?: ")
    add_address = input("  What is their address?: ")
    add_phone = input("  What is their phone number?: ")
    add_email = input("  What is their email?: ")
    # Creating a contact tuple and adding it to the contact list
    contact = (number_of_contacts + 1, add_name, add_address, add_phone, add_email)
    contact_list.append(contact)
    number_of_contacts += 1
    print("Successfully added the contact to your book!")
    print("")

# Function to edit a contact in the contact book
def edit_contact():
    global number_of_contacts
    global contact_list
    print_list()
    # Getting the contact number to edit from the user
    try:
        edit_contact_number = int(input("What contact would you like to edit? (Put the number of the contact): "))
    except ValueError:
        print("Invalid input! Please enter a valid contact number.")
        return

    # Validating the contact number
    while edit_contact_number < 1 or edit_contact_number > number_of_contacts:
        print("That is not a valid contact number!")
        try:
            edit_contact_number = int(input("What contact would you like to edit? (Put the number of the contact): "))
        except ValueError:
            print("Invalid input! Please enter a valid contact number.")
            return

    # Getting the field to edit from the user
    option = input("What would you like to change? (name, address, phone, email, all): ")
    # Validating the field option
    while option != "name" and option != "address" and option != "phone" and option != "email" and option != "all":
        print("That is not a valid option!")
        option = input("What would you like to change? (name, address, phone, email, all): ")

    # Performing the corresponding action based on the field option
    if option == "name":
        # Getting the new name from the user
        new_name = input("  What is the edited name?: ")
        old_contact = contact_list[edit_contact_number - 1]
        # Creating a new contact tuple with the updated name
        new_contact = (old_contact[0], new_name, old_contact[2], old_contact[3], old_contact[4])
        contact_list[edit_contact_number - 1] = new_contact
        print("Contact number " + str(edit_contact_number) + "'s name was changed to '" + new_name + "'")
    elif option == "address":
        # Getting the new address from the user
        new_address = input("  What is the edited address?: ")
        old_contact = contact_list[edit_contact_number - 1]
        # Creating a new contact tuple with the updated address
        new_contact = (old_contact[0], old_contact[1], new_address, old_contact[3], old_contact[4])
        contact_list[edit_contact_number - 1] = new_contact
        print("Contact number " + str(edit_contact_number) + "'s address was changed to '" + new_address + "'")
    elif option == "phone":
        # Getting the new phone number from the user
        new_phone = input("  What is the edited phone number?: ")
        old_contact = contact_list[edit_contact_number - 1]
        # Creating a new contact tuple with the updated phone number
        new_contact = (old_contact[0], old_contact[1], old_contact[2], new_phone, old_contact[4])
        contact_list[edit_contact_number - 1] = new_contact
        print("Contact number " + str(edit_contact_number) + "'s phone number was changed to '" + new_phone + "'")
    elif option == "email":
        # Getting the new email from the user
        new_email = input("  What is the edited email?: ")
        old_contact = contact_list[edit_contact_number - 1]
        # Creating a new contact tuple with the updated email
        new_contact = (old_contact[0], old_contact[1], old_contact[2], old_contact[3], new_email)
        contact_list[edit_contact_number - 1] = new_contact
        print("Contact number " + str(edit_contact_number) + "'s email was changed to '" + new_email + "'")
    else:
        # Editing all fields of the contact
        old_contact = contact_list[edit_contact_number - 1]
        new_name = input("  What is their name?: ")
        new_address = input("  What is their address?: ")
        new_phone = input("  What is their phone number?: ")
        new_email = input("  What is their email?: ")
        new_contact = (old_contact[0], new_name, new_address, new_phone, new_email)
        contact_list[edit_contact_number - 1] = new_contact
        print("Successfully applied all changes")

    print("")

# Function to delete a contact from the contact book
def delete_contact():
    global number_of_contacts
    global contact_list
    print_list()
    # Getting the contact number to delete from the user
    delete_contact_number = int(input("What contact would you like to delete? (Put the number of the contact): "))
    # Validating the contact number
    while delete_contact_number < 1 or delete_contact_number > number_of_contacts:
        print("That is not a valid contact number!")
        delete_contact_number = int(input("What contact would you like to delete? (Put the number of the contact): "))
    
    # Deleting the contact from the contact list
    deleted_contact = contact_list.pop(delete_contact_number - 1)
    number_of_contacts -= 1
    print("Contact number " + str(delete_contact_number) + " was deleted from your book")
    print("")

# Main function to run the contact book
def main():
    global completed
    # Running the contact book until the user indicates completion
    while not completed:
        # Getting the user's choice from the menu
        menu = input("Would you like to view, add, edit, or delete a contact?: ")
        # Validating the menu choice
        while menu != "add" and menu != "edit" and menu != "delete" and menu != "view":
            print("That is not a valid option!")
            menu = input("Would you like to view, add, edit, or delete a contact?: ")
        
        # Performing the corresponding action based on the menu choice
        if menu == "add":
            add_contact()
        elif menu == "edit":
            edit_contact()
        elif menu == "view":
            print_list()
        else:
            delete_contact()

# Running the main function to start the contact book
main()