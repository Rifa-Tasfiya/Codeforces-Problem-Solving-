"""Codeforeces Round #769 (Div.2)
Problem A - ABC"""

"""If a binary string has palindrome substring, then print NO.. Otherwise print YES"""

def canReorder(string):
    if size == 1:
        print("YES")
    elif size == 2:
        if string == "00" or string == "11":
            print("NO")
        else:
            print("YES")
    else:
        print("NO")

#======================================= For User Input ===============================================================
t = int(input())
for i in range(t):
    size = int(input())
    string = input()
    canReorder(string)
