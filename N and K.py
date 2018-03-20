N=int(input("N="))
K=int(input("K="))
a=[input("element in N") for i in range (N)]
sum=0
for i in range (K):
  sum=sum+a[i]
print sum
