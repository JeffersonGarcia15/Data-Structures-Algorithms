def halvesAreAlike(string):
    vowel = 'aeiou'
    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]
    leftCounter = 0
    rightCounter = 0
    for letter in left:
        if letter in vowel:
            leftCounter += 1
        else:
            continue

    for letter in right:
        if letter in vowel:
            rightCounter += 1
        else:
            continue

    return leftCounter == rightCounter
