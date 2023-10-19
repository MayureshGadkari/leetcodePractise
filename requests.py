# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for c in s:
#             if c in '([{':
#                 stack.append(c)
#             elif c == ')' and stack and stack[-1] == '(':
#                 stack.pop()
#             elif c == ']' and stack and stack[-1] == '[':
#                 stack.pop()
#             elif c == '}' and stack and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 return False
#         return not stack
#
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for c in s:
#             if c in '([{':
#                 stack.append(c)
#             elif stack and stack[-1] + c in '()[]{}':
#                 stack.pop()
#             else:
#                 return False
#         return not stack
#
# output = Solution()
# print(output.isValid('())'))
#
#
#str1 = 'xyz#'
str1 = 'xyzz##'

def compare(str1):
    # TODO: Write your code here
    str1_final = ""
    #str2_final = ""
    left = 0
    right = left + 1
    while right <= len(str1):
        if str1[left] != "#":
            str1_final = str1_final + str1[left]
        if right < len(str1) and str1[right] == "#":
            str1_final = str1_final[:-1]
        left += 1
        right += 1
    left = 0
    right = left + 1
    return str1_final
print(compare(str1))