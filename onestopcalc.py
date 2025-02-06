def mainmenu():
    "prints the four options for the calc"
    print("MAIN MENU\n")
    print("1. standard")
    print("2. scientific")
    print("3. units")
    print("4. tips")
    print("5. currency\n\n")

def standard():
    print("STANDARD CALCULATOR: computes +,-,/,*")
    print("type 'menu' to return to main menu or 'clear' to reset previous result")

    previous = 0

    while True:
        entry = input()
        if entry.lower() == "menu":
            return  
        elif entry.lower() == "clear":
            previous = 0
            print("previous calculations have been cleared.")
            continue

        try: 
            if isvalidstandard(entry):
                if entry[0] in "+-/*":
                    newexpr = str(previous) + entry
                    result = eval(newexpr)
                    print(f"Result: {result}")
                    previous = result
                else:
                    result = eval(entry)
                    print(f"Result: {result}")
                    previous = result
            else:
                print("invalid entry. try again")
        except Exception as e:
            print(f"Error: {e}. Please try again.")
def isvalidstandard(entry):
    allowed = "0123456789/+-*(). "
    if not all(c in allowed for c in entry):
        return False
    if "**" in entry or "++" in entry or "--" in entry or "//" in entry:
        return False

def scientific():
    print("type 'menu' to return to main menu or 'clear' to reset previous result")

    previous = 0

    while True:
        entry = input()
        if entry.lower() == "menu":
            return  
        elif entry.lower() == "clear":
            previous = 0
            print("previous calculations have been cleared.")
            continue

def unitconverter():
    print("type menu to return to main menu")
    entry = input()
    if entry.lower == "menu":
        onestopcalc()
    
def tipcalc():
    print("type menu to return to main menu")
    entry = input()
    if entry.lower == "menu":
        onestopcalc()

def currencyconverter():
    print("type menu to return to main menu")
    entry = input()
    if entry.lower == "menu":
        onestopcalc()

def onestopcalc():
    print("welcome to the one stop calculator. your ultimate tool for everyday math and conversions. \
          \nFrom simple calculations to scientific equations, \
          unit conversions, tipping, and currency exchanges, everything you need \
          is just a click away!\n\n\n")
    
    while True:
        mainmenu()
        calc_choice = input("enter choice (number or name):")
        if calc_choice == "1" or calc_choice.lower() == "standard":
            standard()

        elif calc_choice == "2" or calc_choice.lower() == "scientific":
            scientific()
        
        elif calc_choice == "3" or calc_choice.lower() == "units":
            unitconverter()

        elif calc_choice == "4" or calc_choice.lower() == "tips":
            tipcalc()

        elif calc_choice == "5" or calc_choice.lower() == "currency":
            currencyconverter()
        else:
            print("invalid choice. try again")
        