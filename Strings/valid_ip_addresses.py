def validIPAddress(string):
    ipAddressesFound = []
    
    for i in range(1, min(len(string), 4)):
        currentIpAddressesFound = ["", "", "", ""]
        currentIpAddressesFound[0] = string[:i]
        if not isValidIpAddress(currentIpAddressesFound[0]):
            continue
        
        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIpAddressesFound[1] = string[i:j]
            if not isValidIpAddress(currentIpAddressesFound[1]):
                continue
            
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIpAddressesFound[2] = string[j:k]
                currentIpAddressesFound[3] = string[k:]
                
                if isValidIpAddress(currentIpAddressesFound[2]) and isValidIpAddress(currentIpAddressesFound[3]):
                    ipAddressesFound.append(".".join(currentIpAddressesFound))
    return ipAddressesFound

def isValidIpAddress(string):
    stringToInt = int(string)
    if stringToInt > 255:
        return False
    
    return len(string) == len(str(stringToInt))
        


print(validIPAddress("1921680"))
