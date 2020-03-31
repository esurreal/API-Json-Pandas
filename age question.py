user_input = input("how old are you?: ")
#if intAge!= int():
    #print("try again")
#else:
    #pass
#if intAge > 40:
    #print("you are old")
#else:
    #print("you are still young")

try:
    age = int(user_input)
    if age > 41:
        print("Damn, you are old. HAHAHA")
    else:
        print("you are still young")
except ValueError:
    try:
        age = float(user_input)
        if age > 41:
            print("Damn, you are old. HAHAHA")
        else:
            print("You're still young")
    except ValueError:
        print("Please enter a number")
