count_down = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,]
list = [1, 2, 3, 4, 5]
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


num = input ("give one number")
num_1 = input ("give another one number")




