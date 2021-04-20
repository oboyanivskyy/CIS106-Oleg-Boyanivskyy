# This program will ask for you to write
# a sentance, and then it will print it
# backwards.


def get_text():
    print("Please enter your line of text.")
    text = input()
    
    return text


def fix_text(text):
    newtext = text
    newtext = newtext.strip()
    newtext = " ".join(newtext.split())
    newtext = newtext[::-1]
    
    return newtext


def display_text(newtext):
    print(newtext)
    
    
def main():
    text = get_text()
    newtext = fix_text(text)
    display_text(newtext)
    
    
main()