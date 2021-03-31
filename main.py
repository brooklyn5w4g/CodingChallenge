import sys

numeralValues = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def numeralToDecimal(numeral):
    total = 0
    lastValue = 0

    for symbol in reversed(numeral):
        currentValue = numeralValues[symbol]

        if lastValue > currentValue:
            total -= currentValue
        else:
            total += currentValue

        lastValue = currentValue

    return total

descendingNumerals = ['M','D','C','L','X','V','I']

validPrecedingCharacters = {
    'I': [],
    'V': ['I'],
    'X': ['I'],
    'L': ['V','X'],         #I'm going to assume V is a valid preceding character of L
    'C': ['X'],             #it wasn't clear in the spec
    'D': ['L','C'],
    'M': ['C']
}

def decimalToNumeral(decimal):
    finalString = ''
    i = 0

    while decimal > 0:
        currentNumeral = descendingNumerals[i]

        #First try subtracting the whole value of the current numeral
        if decimal - numeralValues[currentNumeral] >= 0:
            finalString += currentNumeral
            decimal -= numeralValues[currentNumeral]
        else:
            #Try subtracting partial values of the current numeral. For example IX or XC
            addedToString = False
            for character in validPrecedingCharacters[currentNumeral]:
                if decimal - (numeralValues[currentNumeral] - numeralValues[character]) >= 0:
                    finalString += character + currentNumeral
                    decimal -= (numeralValues[currentNumeral] - numeralValues[character])
                    addedToString = True

            #if we did not add to the string, move on to the next smallest numeral
            if not addedToString:
                i += 1

    return finalString

def testFunctions():
    for i in range(10000):
        if i != numeralToDecimal(decimalToNumeral(i)):
            print("Conversion did not work with number " + str(i) + "!")

def isRomanNumeral(testString):
    for character in testString:
        if character not in descendingNumerals:
            return False

    return True

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Please enter a valid positive integer or Roman numeral as an argument")
        exit(0)

    if sys.argv[1].isnumeric():
        number = int(sys.argv[1])
        print("Roman Numeral- ")
        print(decimalToNumeral(number))

    elif isRomanNumeral(sys.argv[1]):
        print("Decimal- ")
        print(numeralToDecimal(sys.argv[1]))

    else:
        print("Please enter a valid positive integer or a Roman numeral (MDCLXVI)")







