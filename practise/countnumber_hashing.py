# Q1 — Count a Number
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 1]
q = [5, 2, 1, 10]
def countnumber_(num1,num2):
    list_hashing=[0]*11

    for ch in num1:
        list_hashing[ch]=list_hashing[ch]+1

    for ch in num2:
        if ch<0 or ch>10:
            print(0)
        else:
            print(list_hashing[ch])

print(countnumber_(n,q))

# Q2 — Count Multiple Queries
n = [1, 2, 3, 2, 1, 4, 2, 5, 3, 1]
q = [1, 2, 3, 4, 5, 6]
def countmultiples_(num1,num2):
    list_hashing=[0]*11

    for ch in num1:
        list_hashing[ch]=list_hashing[ch]+1

    for ch in num2:
        if  ch<0 or ch>10:
            print(0)
        else:
            print(list_hashing[ch])

print(countmultiples_(n,q))

# Q3 — Find the Most Frequent Number
n=[4, 2, 4, 3, 2, 4, 5, 2, 2]
def mostfrequent_(num1):
    list_hashing=[0]*11
    highest=0
    index=0

    for i in num1:
        list_hashing[i]=list_hashing[i]+1

    for i in range(len(list_hashing)):
        if list_hashing[i]>highest:
            highest=list_hashing[i]
            index=i

    return index
print(mostfrequent_(n))

# Q4 — Count Numbers With Frequency > 1

n = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
def countnumbers_frequency(num1):
    list_hashing=[0]*11
    count=0


    for i in num1:
        list_hashing[i]=list_hashing[i]+1

    for i in range(len(list_hashing)):
        if list_hashing[i]>1:
            count+=1

    return count

print(countnumbers_frequency(n))

# Q5 — Highest and Lowest Frequency
n = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
def highest_lowest(num1):
    list_hashing=[0]*11
    first=0
    second=0

    for i in num1:
        list_hashing[i]=list_hashing[i]+1
    
    for i in range(0,len(list_hashing)):
        if list_hashing[i]>first:
            second=first
            first=list_hashing[i]

        elif list_hashing[i]>second and list_hashing[i]<first:
            second=list_hashing[i]
            

    print(first,second)

print(highest_lowest(n))


# CHARACTER HASHING 
# Q1 — Count a Character
s = "azyxyyzaaaa"
q = ["a", "a", "y", "x"]
def count_character(char1,char2):
    list_hashing=[0]*26

    for ch in char1:
        ascii_val=ord(ch)
        index=ascii_val-97
        list_hashing[index]+=1

    for ch in char2:
        ascii_val=ord(ch)
        index=ascii_val-97
        print(list_hashing[index])

print(count_character(s,q))

# Q2 — Count All Characters

s = "banana"
def count_all(char):
    list_char=[0]*26

    for ch in char:
        ascii_val=ord(ch)
        index=ascii_val-97
        list_char[index]+=1

    for i in range(len(list_char)):
        if list_char[i]>0:
            print(chr(i+97),list_char[i])

print(count_all(s))

# Q3 — Most Frequent Character
s = "programming"

def mostfrequent_(char):
    highest=0
    index=0
    list_char=[0]*26

    for ch in char:
        ascii_val=ord(ch)
        index=ascii_val-97
        list_char[index]+=1

    for i in range(len(list_char)):
        if list_char[i]>highest:
            highest=list_char[i]
            index=i

    print(chr(index+97))
    

# print(mostfrequent_(s))

Q4 — Count Distinct Characters

s = "aabbccddeeffa"
def countdistinct_(char):
    list_char=[0]*26
    count=0

    for ch in char:
        ascii_val=ord(ch)
        index=ascii_val-97
        list_char[index]+=1

    for i in range(len(list_char)):
        if list_char[i]>0:
            print(chr(i+97))
            count+=1

    return count

print(countdistinct_(s))

# Q5 — Character Frequency Comparison

s1="listen"
s2="silent"

def charactercomparsion_(char1,char2):
    list_char1=[0]*26
    list_char2=[0]*26

    for ch in char1:
        ascii_val=ord(ch)
        index=ascii_val-97
        list_char1[index]+=1

    for ch in char2:
        ascii_val=ord(ch)
        index=ascii_val-97
        list_char2[index]+=1

    for i in range(26):
        if list_char1[i]!=list_char2[i]:
            return False

    return True

print(charactercomparsion_(s1,s2))

# Q1 — Count a Number

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 1]
q = [5, 2, 1, 10]

def count_dict(num1,num2):
    count_dict={}

    for i in num1:
        count_dict[i]=count_dict.get(i,0)+1
    for i in num2:
        if i<0 and i>10:
            print(0)
        else:
            print(count_dict.get(i,0))

print(count_dict(n,q))

# Q2 — Count Multiple Queries
n = [1, 2, 3, 2, 1, 4, 2, 5, 3, 1]
q = [1, 2, 3, 4, 5, 6]

def count_dict(num1,num2):
    count_dict={}

    for i in num1:
        count_dict[i]=count_dict.get(i,0)+1
    for i in num2:
        if i<0 and i>10:
            print(0)
        else:
            print(count_dict.get(i,0))

print(count_dict(n,q))

# Q3 — Most Frequent Number
n = [4, 2, 4, 3, 2, 4, 5, 2, 2]

def most_frequent(num1):
    highest=0
    key=0
    count_dict={}

    for i in num1:
        count_dict[i]=count_dict.get(i,0)+1

    for i in count_dict:
        if count_dict[i]>highest:
            highest=count_dict[i]
            key=i

    print(key)

print(most_frequent(n))
# Q4 — Count Numbers Appearing More Than Once
n = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

def countnumber_(num):
    count_dict={}
    highest=0

    for i in num:
        count_dict[i]=count_dict.get(i,0)+1

    for i in count_dict:
        if count_dict[i]>highest:
            highest=count_dict[i]

    return highest

print(countnumber_(n))

# Q5 — Highest and Lowest Frequency
n = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]

def highest_lowest(num1):
    dict={}
    highest=0
    second=0

    for i in num1:
        dict[i]=dict.get(i,0)+1

    for i in dict:
        if dict[i]>highest:
            second=highest
            highest=dict[i]

        elif dict[i]>second and dict[i]<highest:
            second=dict[i]

    return (highest,second)

print(highest_lowest(n))

# Q1 — Count a Character
s = "azyxyyzaaaa"
q = ["a", "a", "y", "x"]

def count_character(num1,num2):
    count_dict={}

    for ch in num1:
        ascii_val=ord(ch)
        index=ascii_val-97
        count_dict[index]=count_dict.get(index,0)+1

    for ch in num2:
        ascii_val=ord(ch)
        index=ascii_val-97
        print(count_dict.gret(index,0))


print(count_character(s,q))

# Q4 — Count Distinct Characters
s = "aabbccddeeffa"
def count_distinct(num):
    count_dict={}
    count=0

    for i in num:
        count_dict[i]=count_dict.get(i,0)+1

    for i in count_dict:
        count+=1

    print(count)

print(count_distinct(s))

Q2 — Count All Characters
s = "banana"
def countall_characte(char1):
    countdict_={}
    n=len(char1)

    for i in range(0,n):
        countdict_[char1[i]]=countdict_.get(char1[i],0)+1

    for key,value in countdict_.items():
        print(key,value)


print(countall_characte(s))


Q3 — Most Frequent Character
s="programing"

def mostfrequent_(char1):
    countmost={}
    highest=0
    key=0

    for i in range(len(char1)):
        countmost[char1[i]]=countmost.get(char1[i],0)+1

    for i in range(0,len(countmost)):
        if highest<countmost[char1[i]]:
            highest=countmost[char1[i]]
            key=i

        
        

    print(highest,chr(key+97))


print(mostfrequent_(s))