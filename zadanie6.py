def calculateBMI(weight, height):
    return int(weight) / (float(height)/100)**2

if __name__ == "__main__":
    wzrost = raw_input("podaj wzrost")
    waga = raw_input("podaj wage")
    print "Twoje bmi to: ", calculateBMI(waga, wzrost)
