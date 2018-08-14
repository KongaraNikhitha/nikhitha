n=int(input())
list=[int(p) for p in raw_input().split()]
list.sort()
print " ".join(map(str,list))
