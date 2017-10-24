# while loop
count = 0
while (count < 9):
    print("the count is", count)
    count  = count + 1


#for loop
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

# for loop get second index value
for index in range(1):
       print('Second fruit :', fruits[1])

# find prime numbers
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) :
       print (i, " is prime")
   i = i + 1

