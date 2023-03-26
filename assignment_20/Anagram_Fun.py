def CheckAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("{} and {} are anagrams string".format(s1,s2))
    else:
        print("{} and {} are not anagrams string".format(s1,s2))


s1,s2= input("enter first string:-"),input("enter second string:-")
CheckAnagram(s1,s2)