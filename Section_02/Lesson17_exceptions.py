try:
    a = float("ancd")
except ValueError:
    print("Value casting error")
except:
    print("Generic error")

tries = 0
while True:
    a = input("Enter positive number: ")
    tries += 1

    try:
        a = float(a)
        # custom exception
        if float(a) <= 0:
            raise  Exception("You entered negative number")
    except ValueError:
        print("Value casting error")
    except Exception as exp:  # custom exception
        print(exp)
    except:
        print("Generic user error")
    else:
        print("Thanks!!!!")
    finally:
        print("Program exits")
        #  exit(1)

    if tries > 2:
        break

print("--- Exersise ---")
z = input("Enter positive number: ")
try:
    print(3.62 / float(z))
except ZeroDivisionError:
    print("Zero Division Error determined")





