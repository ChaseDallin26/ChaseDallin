count_down = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,]
list = [1, 2, 3, 4, 5]
name = ["chase", "chance", "harper", "dane"]
for numbers in count_down:
    print(numbers)
for numbers in count_down:
    sum_1 = (sum(count_down))

print(sum_1)
squares = []
for i in list:
    squares.append(i*i)
print (squares)

word = input ("enter a word\n>")

for letters in word:
    vowel_sum= 0 
    if letters == "a" or letters == "e" or letters == "i" or letters == "o" or letters == "u":
        vowel_sum += 1

print (vowel_sum)


num = input ("give one number\n>")


for i in range(1, 11):
    print(num + " x " + str(i) + "=" + str(int(num) * i))

for names in name:
     print ("hello, " + names + "!")    