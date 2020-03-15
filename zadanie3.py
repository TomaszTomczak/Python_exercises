def sumDigitsFromString(string):
    suma = 0
    for digit in string:
        suma += int(digit)
    return suma

if __name__ == "__main__":
   print sumDigitsFromString("123")