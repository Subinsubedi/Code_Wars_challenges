num=("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")

num = num.split(" ")

for i in range(0, len(num)):
    num[i]= int(num[i])
    print(num)

low=min(num)
high=max(num)

print("-------")
print(low,high)






