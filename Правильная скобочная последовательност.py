a = []
s = input()

for i in s:
    if i == '(' or i == '[' or i == '{':
        a.append(i)
        continue
    elif len(a) > 0:
        if (i == ')' and a[-1] == '(') or (i == ']' and a[-1] == '[') or (i == '}' and a[-1] == '{'):
            del a[-1]
            continue
    print("no")
    break
else:
    print("yes" if len(a) == 0 else "no")
