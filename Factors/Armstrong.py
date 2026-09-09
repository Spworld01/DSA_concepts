def Armstrong(num):
    n=num
    nod=len(str(num))
    result=0

    while num>0:
        id=num%10
        result=result+(id**nod)
        num=num//10

    if n==result:
        print("Armstrong")
    else:
        print("NOt Armstrong")

print(Armstrong(1536789))