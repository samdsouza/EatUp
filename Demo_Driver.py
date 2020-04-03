import xlsxwriter
from openpyxl import load_workbook
import pandas

import xlrd




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
        command.strip()
        print("Command = ", command)
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

        elif command == "Customer":
            while command != "back":
                customerMenu()
                command = input()
                if command == "New user":
                    setupUser()

                if command == "Login":
                    print("Enter Customer ID:")
                    command = input()
                    login_success = 0
                    login_success, customerFirstName, customerLastName = loginCustomer(command)
                    while login_success != 1:
                        print("Customer ID not found in database, Please try again")
                        command = input()
                        login_success, customerFirstName, customerLastName = loginCustomer(command)
                    print('Welcome Back' , customerFirstName.strip(), customerLastName.strip(), "!")
                    #print('Before Customer Rewards Call')
                    customerRewardsMenu(customerFirstName.strip(),customerLastName.strip())
                    #print('After Customer Rewards Call')

        else:
            print("Invaild Command")

    return











def fileLocation(fileName):
    baseDirectory = "/Users/samdsouza/Documents/EatUp/EatUp"
    fileLocation = baseDirectory + "/" + fileName
    return fileLocation

def openWorkbook(fileLocation):
    wb = xlrd.open_workbook(fileLocation)
    return wb


def returnCustomerID(workbook):
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0,0)
    return sheet.cell_value(0,1)

def returnCustomerName(workbook):
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0,0)
    return sheet.cell_value(1,1)

def extractInfo(workbook):
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0,0)
    lengthSheet = sheet.nrows

    dates = []
    restaurants = []
    prices = []
    rewards = []

    for i in range(4,lengthSheet):
        #print(sheet.cell_value(i,0))
        dates.append(sheet.cell_value(i,0))
        restaurants.append(sheet.cell_value(i,1))
        prices.append(sheet.cell_value(i,2))
        rewards.append(sheet.cell_value(i,3))

    return dates, restaurants, prices, rewards


def searchRestaurant(workbook,searchRestaurant):
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0,0)
    lengthSheet = sheet.nrows

    for i in range(4,lengthSheet):
        currentRestaurant = sheet.cell_value(i,1)
        if(searchRestaurant == currentRestaurant):
            return currentRestaurant
        else:
            print('Did Not Find Resteraunt')

def determineRewards(workbook,searchRestaurant):
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0,0)
    lengthSheet = sheet.nrows

    for i in range(4,lengthSheet):
        currentRestaurant = sheet.cell_value(i,1)
        if(searchRestaurant == currentRestaurant):
            totalRewards =  sheet.cell_value(i,3)
            return totalRewards

def addNewVisit(fileDestination,restaurantName,date,totalSpent):
    # Before adding total spent, need to lookup resteraunt reward policy in resteraunt index
    # Determine the rewards earned and input into the individual resteraunt and customer excell sheet
    wb = load_workbook(filename = dest)
    worksheet = wb["Sheet1"]


    currentRow = worksheet.max_row
    dateCell = worksheet.cell(row = currentRow, column = 1)
    restaurantCell = worksheet.cell(row = currentRow, column = 2)
    spentCell = worksheet.cell(row = currentRow, column = 3)
    rewardsEarnedCell = worksheet.cell(row = currentRow, column = 4)
    rewardsClaimedCell = worksheet.cell(row = currentRow, column = 5)

    dateCell.value = date + "'"
    restaurantCell.value = restaurantName
    spentCell.value = totalSpent
    wb.save(dest)







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
def customerRewardsMenu(customerFirstName, customerLastName):
    #print('Made it in customer Rewards ')
    inp = "start"
    while inp != "back":
        print("\n")
        print("____________________ ", customerFirstName, customerLastName,"'s", "Rewards_________________")
        print("1. Rewards progress")
        print("2. Input rewards")
        print("3. Redeem rewards")

        inp = input()

        if inp == "Rewards progress":
            rewardsProgress()
        if inp == "inputRewards":
            inputRewards()
        if inp == "redeemRewards":
            redeemRewards()
    return

#placeholder
def loginCustomer(command):
    signal = 1
    filename = 'customerIndex.xlsx'
    fileLocationOutput = fileLocation(filename)
    customerIndexBook = openWorkbook(fileLocationOutput)
    sheet = customerIndexBook.sheet_by_index(0)
    sheet.cell_value(0,0)
    lengthSheet = sheet.nrows
    #print('Length of Sheet =' , lengthSheet)

    for i in range(2,lengthSheet):
        #('Starting Loop')
        currentID = sheet.cell_value(i,0)
        #print('Current ID = ', currentID)
        if(command == str(int(currentID))):
            customerFirstName =  sheet.cell_value(i,1)
            customerLastName = sheet.cell_value(i,2)
            return signal, customerFirstName, customerLastName

    signal = 0
    customerFirstName = 'NA'
    customerLastName = 'NA'
    return signal, customerFirstName, customerLastName



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
