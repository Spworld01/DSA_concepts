n=[5,3,2,2,1,5,5,7,5,1]
m=[10,111,1,9,5,4,2]

def hashing_dict(num1,num2):
    hash_dict={}

    for i in num1:
        hash_dict[i]=hash_dict.get(i,0)+1

    for i in num2:
        if i<0 or i>10:
            print(0)
        else:
            print(hash_dict.get(i,0))

print(hashing_dict(n,m))