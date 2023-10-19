def find_substring(main_string, sub_string):
    list_main_string = main_string.split(",")
    count = 0
    for i in list_main_string:
        count += 1
    num = count - 1
    p = len(sub_string) + 2
    position = []
    for i in range(0, num):
        position.append(p)
        p += p
    return (num, position)
main_string = 'Let,let,let'
sub_string = 'let'

print(find_substring(main_string,sub_string))