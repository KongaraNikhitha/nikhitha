n=int(input())
list=[int(z) for z in raw_input().split()]
list.sort()
print " ".join(map(str,list))
