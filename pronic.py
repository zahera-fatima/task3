def pronic_n0(num):
    flag = False
    for i in range(1,num+1):
        if ((i*(i+1)) == num):
            flag = True
            break
    return flag

print("pronic no b/w 1 & 100: ")
for j in range(1,101):
    if(pronic_n0(j)):
        print(j)
        
print("enter a no to check pronic no: ")
no = int(input())
if(pronic_n0(no)):
    print(f"{no} is pronic no.")
else:
    print(f"{no} is not pronic no.")
