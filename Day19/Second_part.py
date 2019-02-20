

#find number in register [1]. Final solution is sum of all factor of that number. In my case register [1] was 10551309.

def print_factors(x):

   print("The factors of",x,"are:")
   count = 0
   sum = 0
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           count += 1
           sum += i

   print(count)
   print(sum)

num = 10551309
print_factors(num)