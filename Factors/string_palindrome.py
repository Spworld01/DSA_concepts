s=list("NITIN")

def string_palindrome(str,left,right):

    if left>=right:
        return True

    if str[left]!=str[right]:
        return False

    return string_palindrome(str,left+1,right-1)

print(string_palindrome(s,0,4))