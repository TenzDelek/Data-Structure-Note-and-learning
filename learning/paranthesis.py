def checking(string):
    stack=[]
    openin="({["
    for i in string:
        if i in openin:
            stack.append(i)
        else:
            if(not stack or (i=="}" and stack[-1]!="{") or (i=="]" and stack[-1]!="[")or (i==")" and stack[-1]!="(")):
                return "NOT EQUAL"
            stack.pop()
    if not stack:
        return "equal"
string="[()]]"
ans=checking(string)
print(ans)

