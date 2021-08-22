def uncompress(string):
    numbers = '0123456789'
    result = []
    i = 0
    j = 0
    while j < len(string):
        if string[j] in numbers:
            j += 1
        else:
            number = int(string[i:j])
            result.append(string[j] * number)
            j += 1
            i = j
    return ''.join(result)
            


print(uncompress('5y'))
print(uncompress("2c3a1t"))
