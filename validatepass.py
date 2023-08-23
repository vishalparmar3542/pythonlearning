def validate(password):
    a_set = set()
    min_length = 8
    if len(password) < min_length:
        print("Insufficient length")
        return False
    for char in password:
        # Checking alphabet: a-z A-Z is in password characters
        if(ord(char)>64 and ord(char)<91):
            a_set.add("big")
        if char.isalpha() == True:
            a_set.add("letter")
            continue
        # Check for numbers 0-9
        elif char.isdigit() == True:
            a_set.add("number")
            continue
        # Check for symbol (not alphanumeric)
        elif char.isalnum() == False:
            a_set.add("symbol")
            continue
        else:
            print("User may use a non ASCII keyboard!")
            return False
        
    # Check if all: letter, number and symbol in the set
    if "letter" not in a_set:
        print("No letter in password!")
        return False
    elif "number" not in a_set:
        print("No number in password!")
        return False
    elif "symbol" not in a_set:
        print("No symbol in password!")
        return False
    elif "big" not in a_set:
        print("No big char in password!")
        return False
    else:
        print("Password is good. Carry on.")
        return True
validate("qwqs2@")