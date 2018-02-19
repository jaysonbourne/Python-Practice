print ("hello world")

#multiples part 1: Print all odd numbers from 1 - 1000

for x in range (1,1000):
    if(x%2 == 1):
        print (x)

#mulitples part 2: Print all multiples of 5 from 5 to 1M

for B in range (5,100):
    if(B%5 == 0):
        print (B)

#Part 3: Get the sum of a list.

a = [1, 2, 5, 10, 255, 3]
ave_count = 0
# sum = 0
# for count in range(0,6):
#     sum += a[count]
#     print (sum)

all_sum = sum(a)
print (all_sum)

#Part 4: Get the Average (I used the same list from above)
# for count in range(0,6):
#     sum += a[count]
#     ave_count += 1
# sum = sum / ave_count
# print (sum)

average = all_sum/len(a)
print (average)
