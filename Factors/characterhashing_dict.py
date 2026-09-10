s="azyxyyzaaaa"

q=["a","a","y","x"]

def hashing_dict(num1,num2):

    hash_dict={}

    for ch in num1:
        hash_dict[ch]=hash_dict.get(ch,0)+1

    for ch in num2:
        if ch<"a" or ch>"z":
            print(0)
        else:
            print(hash_dict.get(ch,0))

print(hashing_dict(s,q))
        