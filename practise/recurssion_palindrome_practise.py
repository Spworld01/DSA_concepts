# 1. Check palindrome — Beginner
s = list("MADAM")

def palindrome_recurresion1(str,left,right):
    if left>=right:
        return True

    if str[left]!=str[right]:
        return False
    return palindrome_recurresion1(str,left+1,right-1)

print(palindrome_recurresion(s,0,4))

# 2. Check non-palindrome — Beginner
s = list("HELLO")

def palindrome_recurresion2(str,left,right):
    if left>=right:
        return True

    if str[left]!=str[right]:
        return False
    return palindrome_recurresion2(str,left+1,right-1)

print(palindrome_recurresion(s,0,4))

# 3. Ignore case — Intermediate
s = "madam"
def ignore_case(str,left,right):
    str=str.lower()

    if left>=right:
        return True

    if str[left]!=str[right]:
        return False

    return ignore_case(str,left+1,right-1)

print(ignore_case(s,0,4))


# 4. Count matching pairs — Intermediate
s = list("NITIN")

def count_matching(str,left,right,count):
    if left>=right:
        count+=1
        return count

    if str[left]!=str[right]:
        return count

    return count_matching(str,left+1,right-1,count+1)

print(count_matching(s,0,4,0))

# 5. Recursive palindrome with one mismatch allowed — Advanced  

s=list("RAcAR")

def recursive_palindrome3(str,left,right):
    if left>=right:
        return True

    if str[left]!=str[right]:
        return False

    return recursive_palindrome3(str,left+1,right-1)

print(recursive_palindrome3(s,0,4))


    