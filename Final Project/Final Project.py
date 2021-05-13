# This program will read data from w3schools.com,
# and build parallel array for catalog items, as well as
# display the menu items.


import os


def get_title(title, line):    
    if line.find("TITLE") == True:
        line = line.replace("<TITLE>", "")
        line = line.replace("</TITLE>", "")
        title.append(line)
    else:
        pass


def get_artist(artist, line):    
    if line.find("ARTIST") == True:
        line = line.replace("<ARTIST>", "")
        line = line.replace("</ARTIST>", "")
        artist.append(line)
    else:
        pass


def get_country(country, line):    
    if line.find("COUNTRY") == True:
        line = line.replace("<COUNTRY>", "")
        line = line.replace("</COUNTRY>", "")
        country.append(line)
    else:
        pass
    

def get_company(company, line):    
    if line.find("COMPANY") == True:
        line = line.replace("<COMPANY>", "")
        line = line.replace("</COMPANY>", "")
        company.append(line)
    else:
        pass
    
    
def get_price(price, line):    
    if line.find("PRICE") == True:
        line = line.replace("<PRICE>", "")
        line = line.replace("</PRICE>", "")
        price.append(line)
    else:
        pass


def get_year(year, line):    
    if line.find("YEAR") == True:
        line = line.replace("<YEAR>", "")
        line = line.replace("</YEAR>", "")
        year.append(line)
    else:
        pass
    

def display_results(title, artist, country, company, price, price1, year, average):
    for index in range(len(title)):
        print(title[index], "-", artist[index], "-", country[index], "-",
              price1[index], "-", year[index])
    print(len(title), "items", "-", "$", average, "average price")



def calculate_average(price):
    price1 = [None] * len(price)
    for index in range(0, len(price)):
        price1[index] = price[index]
    total = 0
    average = 0
    for index in range(0, len(price)):
        price[index] = float(price[index])
    for index in range(len(price)):
        total += price[index]
        average = sum(price) / len(price)
        average = str(round(average, 2))

    return average, price1


def read_data(filename):
    title = []
    artist = []
    country = []
    company = []
    price = []
    year = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            get_title(title, line)
            get_artist(artist, line)
            get_country(country, line)           
            get_company(company, line)            
            get_price(price, line)
            get_year(year, line)

    return (title, artist, country, company, price, year)


def main():
    filename = "cd_catalog.xml"
    try:
        if os.stat(filename).st_size > 0:
            title, artist, country, company, price, year = read_data(filename)
            average, price1 = calculate_average(price)
            display_results(title, artist, country,
                        company, price, price1, year, average)
        else:
            print("File is empty")
    except TypeError:
       print("Error: Missing or bad data")
    except ValueError:
        print("Error: Missing or bad data")
    except IndexError:
        print("File is empty")
    except FileNotFoundError:
        print("File is missing")


main()