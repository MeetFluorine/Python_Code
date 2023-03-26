s=input("enter your fav. color with the help of any sentence:-")
color=["yellow","blue","orange","white","black","red"]
for i in s:
    if i==color:
        c=i
        break
    else:
        c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("tuesday")