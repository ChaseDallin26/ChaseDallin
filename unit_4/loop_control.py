for i in range (21):
    if i == 15:
        break
    print(i)
for i in range (31):
    if i % 2 == 0:
        continue
    print (i)
for i in range (10):
    if i == 2:
        pass # print ("hi there")
    print(i)
for i in range (10,0,-1):
    if i == 5:
        continue
    print (i)

list = [7,38,-2,9,-1]
sum = 0
for num in list:
    if num < 0:
        break
    sum += num
print (sum)