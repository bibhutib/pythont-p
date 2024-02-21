def is_Prime(data):
    if data<=2:
        print("It is Even and Prime")
    for i in range(2,int(data**0.5)+1):
        print(f"{i} times exeuted")
        if data % i ==0:
            return False
        return True

num =10
print(is_Prime(num))
        