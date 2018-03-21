f=int(input("f="))
l=int(input("l="))
temp=0
for i in range (f,l+1):
  for n in range (2,i+1):
    if(i%n==0):
      temp=temp+1
  if(temp==1):
    print i
    temp=0
