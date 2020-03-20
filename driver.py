# Eat Up Driver File

import xlsxwriter
import openpyxl
import pandas

import xlrd





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
        print(sheet.cell_value(i,0))
        dates.append(sheet.cell_value(i,0))
        restaurants.append(sheet.cell_value(i,1))
        prices.append(sheet.cell_value(i,2))
        rewards.append(sheet.cell_value(i,3))

    return dates, restaurants, prices, rewards





# def writeNewRestaurant(filename, )





if __name__ == '__main__':
    print('Welcome to EatUp!')

    restaurantIndex = xlsxwriter.Workbook('restaurantIndex.xlsx')
    restaurantListings = restaurantIndex.add_worksheet()


    restaurantListings.set_column('A:A', 20)
    bold = restaurantIndex.add_format({'bold': True})

    restaurantListings.write(1, 1, 'Resteraunt Name', bold)
    restaurantListings.write(1,0,'Resteraunt ID', bold)

    restaurantListings.write(2,0,1)
    restaurantListings.write(2,1,'Chick Fil A')

    restaurantListings.write(3,0,2)
    restaurantListings.write(3,1, 'AeroTek Cafe')

    restaurantIndex.close()


    fileLocation = fileLocation('customer2.xlsx')
    customer2 = openWorkbook(fileLocation)
    customerID = returnCustomerID(customer2)
    customerName = returnCustomerName(customer2)
    results = extractInfo(customer2)
    customer2Dates = results[0]
    customer2Restaurants = results[1]
    customer2Prices = results[2]
    customer2Rewards = results[3]

    print(customer2Dates)
    print(customer2Prices)





    #ref_workbook= openpyxl.load_workbook('resterauntIndex.xlsx')

    #customer2 = pandas.read_excel('customer2.xlsx')
    #print(customer2)

    #loc = ("/Users/samdsouza/Documents/EatUp/EatUp/customer2.xlsx")

    #wb = xlrd.open_workbook(loc)
    #sheet = wb.sheet_by_index(0)

    #sheet.cell_value(0,0)

    #for i in range(sheet.nrows):
    #    print(sheet.cell_value(i,0))
