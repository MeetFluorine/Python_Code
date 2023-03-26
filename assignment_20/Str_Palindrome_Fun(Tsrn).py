def Check_Palindrome(s1):
    s2= str()
    for i in s1:
        s2= i +s2
    if s2==s1:
        print(" {} and {} is a palindrome string".format(s2,s1))
    else:
        print(" {} and {} are not palindrome string".format(s2,s1))


s1= input("enter a string:-")
Check_Palindrome(s1)