def main():
    #Framework for demo functionality including all menu options
    #display upon entry and entry only:
    print("_________________ Welcome to Eatup! _________________")
    print("To exit type exit,")
    #Recieve user input and trasfer to correct menu, at this point this menu will be the only one displayed until exit
    command = "init"
    while command != "exit":
        print("_______________________ Menu ________________________\n")

        print("1. Buisness")
        print("2. Customer\n")

        command = input()
        if command == "Buisness":
            buisnessMenu()
            while command != "back":
                command = input()
                if command == "Setup":
                    setupBuisness()
                if command == "Manage":
                    print("Enter Buisness ID:")
                    command = input()
                    login_success = 0
                    login_success = loginBuisness()
                    while login_success != 1 or command != "back":
                        print("Enter Buisness ID:")
                        command = input()
                        login_success = loginBuisness()
                    manageMenu()

        if command == "Customer":
            while command != "back":
                customerMenu()
                command = input()
                if command == "New user":
                    setupUser()

                if command == "Login":
                    print("Enter Customer ID:")
                    command = input()
                    login_success = 0
                    login_success = loginCustomer()
                    while login_success != 1 or command != "back":
                        print("Enter Customer ID:")
                        command = input()
                        login_success = loginCustomer()
                    customerRewardsMenu()

    return



#Print menu definitions
def buisnessMenu():
    print("___________________  Buisness Menu ____________________\n")
    print("1. Setup")
    print("2. Manage\n")
    return

#manageMenu handling
def manageMenu():
    inp = "init"
    while inp != "back":
        inp = input()
        print("____________________  Manage Menu _____________________\n")
        print("1. Add rewards")
        print("2. Remove rewards")
        print("3. View rewards")
        print("4. Edit rewards\n")

        if inp == "Add rewards":
            addRewards()
        if inp == "Remove rewards":
            removeRewards()
        if inp == "View rewards":
            displayRewards()
        if inp == "Edit rewards":
            editRewards()
    return

#customer menu function
def customerMenu():
    print("___________________  Customer Menu _______________________\n")
    print("1. New user")
    print("2. Login\n")
    return

#Main customer functionality
def customerRewardsMenu():
    inp = "start"
    while inp != "back":
        inp = input()
        print("____________________  Customer Menu _____________________\n")
        print("1. Rewards progress")
        print("2. Input rewards")
        print("3. Redeem rewards")

        if inp == "Rewards progress":
            rewardsProgress()
        if inp == "inputRewards":
            inputRewards()
        if inp == "redeemRewards":
            redeemRewards()
    return

#placeholder
def rewardsProgress():
    return

#placeholder
def inputRewards():
    return

#placeholder
def redeemRewards():
    return

#placeholder
def loginCustomer():
    return 1

#placeholder
def addRewards():
    return

#placeholder
def removeRewards():
    return

#placeholder
def displayRewards():
    return

#placeholder
def editRewards():
    return

def setupUser():
    return

#placeholder for buisness Setup
def setupBuisness():
    return

#placeholder for buisness login
def loginBuisness():
    return 1

if __name__ == "__main__":
    main()
