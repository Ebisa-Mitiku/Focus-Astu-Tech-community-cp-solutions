s=input()
if len(s)==8 and s[0].isupper() and s[len(s)-1].isupper() and s[1:-1].isdigit() and 100000<=int(s[1:-1])<=999999:
   print("Yes")
else:
    print("No")
