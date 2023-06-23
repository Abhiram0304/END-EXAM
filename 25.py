def palindrome(s,start,end):
    if(start>=end):
        return True
    
    if(s[start]!=s[end]):
        return False
    
    return palindrome(s,start+1,end-1)

f=open("str.txt","r")
data=f.read()
l=data.split(" ")

print(l)
count=0
for i in l:
    if(palindrome(i,0,len(l)-1)):
        count=count+1
print(count)

