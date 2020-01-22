# program to check if a string is a palindrome
string = input()

string_split = []
for i in string:
    string_split.append(i)

str_len = len(string)

middle = str_len//2

if str_len%2 == 0:
    p1 = string_split[:middle]
else:
    p1 = string_split[:middle+1]
p2 = string_split[middle:]
p2.reverse()

if p1 == p2:
    print('True')
else:
    print('False')
