#our input
s=input("write a text, and i remove all unnecessary whitespaces: ")
#our output
new=""
i=0
#find where first word start
while i < len(s):
    while i <len(s) and s[i]==" ":
        i+=1

    j=i
#find where first word ends
    if i < len(s):
        while j < len(s) and s[j]!=" ":
            j+=1
#build up the word
        new+=" "+s[i:j]
    i=j+1

print(new[1:])
