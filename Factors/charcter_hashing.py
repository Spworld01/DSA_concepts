s="azyxyyzaaaa"
q=["a","a","y","x","s"]

def charcter_hashing(num1,num2):
    hash_list=[0]*26

    for ch in num1:
        ascii_val=ord(ch)
        index=ascii_val-97
        hash_list[index]+=1

    for ch in num2:
        ascii_val=ord(ch)
        index=ascii_val-97
        print(hash_list[index])

print(charcter_hashing(s,q))
