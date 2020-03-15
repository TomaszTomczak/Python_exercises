def main():
    print("Witaj swiecie!")

def checkLetters(letters):
    return (sum([1 for b in letters.replace(" ", "") if not b.isupper()]) ,sum([1 for b in letters if b.isupper()]))

def checkIfTextIsPangram(tekst):
    setOfLetters = set(tekst.lower().replace(" ",""))
    if len(setOfLetters) == 26:
        return True
    else:
        print setOfLetters
        return False

if __name__ == "__main__":
   # znaki = checkLetters(raw_input("Podaj jakies slowo: "))
   # print "ilosc wielkich znakow:", znaki[1]
   # print "ilosc malych znakow:", znaki[0] 
   t = raw_input("daj tekst: ");
   print "tekst jest panagramem: ",checkIfTextIsPangram(t)