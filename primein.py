m,n=map(int,raw_input().split())
for num in range(m,n):
  c=0
  for i in range(m,n+1):
    if(num%i==0):
      if(c==2):
        print num


