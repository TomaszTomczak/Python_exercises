def checkIfAnagram(first, second):
    return sorted(first.lower()) == sorted(second.lower())

if __name__ == "__main__":
    print checkIfAnagram("Mary", "army")