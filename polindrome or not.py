n=int(input("enter the no:"))
temp=n
new=0
while(n>0):
  rem=n%10
  new=new*10+rem
  n=n/10
if temp==new:
  print "polindrome"
else:
  print "not polindrome"
