def compress(s):
    s += '!'
    i = 0
    j = 0
    result = []
    
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num))
                result.append(s[i])
            i = j
    return ''.join(result)

print(compress('ccaaatsss'))
    