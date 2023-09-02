strs=["flower","flow","flight"]


def longestCommonPrefix(strs):
    s = strs[0]
    for i in range(1, len(strs)):
        string = strs[i]
        cur = ""
        index = 0
        while index < len(s) and index < len(string):
            if s[index] == string[index]:
                cur += string[index]
                index += 1
            else:
                break
        s = cur
    return s
print(longestCommonPrefix(strs))