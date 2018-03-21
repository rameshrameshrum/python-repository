n=int(input("enter the no:"))
temp=0
for i in range (2,n+1):
  if(n%i==0):
   temp=temp+1
if(temp==1):
  print "prime no"
else:
  print "not prime no"
