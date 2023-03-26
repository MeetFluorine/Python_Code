s1= input("enter a string:-")
it= iter(s1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break