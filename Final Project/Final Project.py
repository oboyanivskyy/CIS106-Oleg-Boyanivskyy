# This program will read data from w3schools.com,
# and build parallel array for catalog items, as well as
# display the menu items.


def get_title(title, line):
    
    if line.find("TITLE") == True:
        line.replace("<TITLE>", "")
        line.replace("</TITLE>", "")
        title.append(line)
    else:
        pass
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
#            get_artist(artist, line)
#            get_country(country, line)           
#            get_company(company, line)            
#            get_price(price, line)
#            get_year(year, line)
        print(title)
            
def main():
    filename = "cd_catalog.xml"
#    try:
    read_data(filename)
#    except TypeError:
#        print("Error: Missing or bad data")
#    except ValueError:
#        print("Error: Missing or bad data")
#    except IndexError:
#        print("File is empty")
#    except FileNotFoundError:
#        print("File is missing")


main()