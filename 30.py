h1,n1=map(int,raw_input().split())
h2,n2=map(int,raw_input().split())
x1=h1*60+n1
x2=h2*60+n2
diff=abs(x1-x2)
time=diff%60
time1=(diff-time)//60
print time1,time
