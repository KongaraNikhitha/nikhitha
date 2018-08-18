size=int(input())
list2=[int(z) for z in raw_input().split()]
list2.sort()
print " ".join(map(str,list2))
