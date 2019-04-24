from collections import Counter
shoe=int(input())
shoe_size=input().split()
shoe_list=map(int,shoe_size)
flist=list(shoe_list)
cust=int(input())
total=0
var=Counter(flist)


def available(size):
    check=var[size]
    if check>0:
        check-=1
        var[size]=check
        return True
    else:
        return False
for x in range(cust):
    val=input().split()
    size=int(val[0])
    price=int(val[1])
    if available(size):
        total+=price
print(total)