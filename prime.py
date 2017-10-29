def findprime(upto):
    i = 2
    while(i < upto):
       j = 2
       while(j <= (i/j)):
          if not(i%j): break
          j = j + 1
       if (j > i/j) :
           print (i, " is prime")
       i = i + 1

findprime(10)