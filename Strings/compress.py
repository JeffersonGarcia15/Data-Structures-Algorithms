# O(n) time | O(n) Space
def compress(s):
    # s += '!'
    # i = 0
    # j = 0
    # result = []
    
    # while j < len(s):
    #     if s[i] == s[j]:
    #         j += 1
    #     else:
    #         num = j - i
    #         if num == 1:
    #             result.append(s[i])
    #         else:
    #             result.append(str(num))
    #             result.append(s[i])
    #         i = j
    # return ''.join(result)
    # def compress(s):
  s += '!'
  left = 0
  right = 1
  count = 1
  string = []
  while right < len(s):
    if s[left] == s[right]:
      right += 1
      count += 1
    else:
      if count == 1:
        string.append(s[left])
      else:
        string.append(str(count))
        string.append(s[left])
      left = right
      right += 1
      count = 1
  return ''.join(string)

print(compress('ccaaatsss'))
    
