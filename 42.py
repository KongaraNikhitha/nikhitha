r1,r2=map(str,raw_input().split())
d1=len(r1)
d2=len(r2)
if d1==d2:
  print r1 or r2
elif d1>d2:
  print r1
else:
  print r2
