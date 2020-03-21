if __name__ == "__main__":
    suma = 0
    ilosc = 0
    try:
       while True:
           suma += int(raw_input("podaj cyfre: "))
           ilosc+=1

    except EOFError as error:
        print "\nsuma cyfr to: ",suma
        