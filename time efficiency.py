# 1  (measure time to execute)
# import time 

# star = time.time()    # current time(time.time())
# for i in range(1,101) :
#     print(i)

# print(time.time()- star)    # current time me initial time delete kar diya 

# 2(counting operation)

# def my_sum(x) :
#     total = 0
#     for i in range(x+1) : 
#         total += i
#     return total

# x = my_sum(8)
# print(x)
# no of operation (1+3x)

# 3  ()
# def fact_iter(n) :
#     total = 1
#     for i in range(1,n+1) :
#         total *= i
#     return total

# a = fact_iter(5)
# print(a)


# 4 (practise of type of order of growth )

# we have what type of code is this
# Q1
# import time

# start = time.time
# L = [1,2,3,4,5]
# sum = 0
# for i in L :
#     sum += i
# print(sum)

# product = 1
# for i in L:
#     product = product*i
# print(product)               # linear   
# print(time.time-start)

# Q2

# L = [1,2,3,5,6]

# for i in L:
#     for j in L:
#         print('({},{})'.format(i,j))     # (quadratic) matlab agar inout 2 time hota hai to time bhi 2 time badh jaayega



# Q5
# def intToStr(i) :
#     digits = "0123456789"
#     if i == 0:
#         return "0"
#     result = ''
#     while i>0 :
#         result = digits[i%10] +result
#         i = i//10
#     return result

# print(intToStr(123))      #output = log 

# Q9
#  0(ab)
# A = [1,2,3,4]
# B = [2,3,4,5,6]

# for i in A:
#     for j in B:
#         if i<j:

#            print('({},{})'.format(i,j))


#  Q10

# A = [1,2,3,4]
# b = [2,3,4,5]

# for i in A:
#     for j in b:
#         for k in range(2):
#              print('({},{})'.format(i,j))



#  Q11
# L = [1,2,3,4,5]
# for i in range(0,len(L)//2):
#     other = len(L) - i - 1
#     temp = L[i]
#     L[i] = L[other]
#     L[other] = temp

# print(L)                                  # o(n)  kyoki loop n/2 baar chal rha hai aur fir further hum 1/2 ko hata denge to hame o(n) mil jaayega

#  Q12

# def factorial(n) :

#     if n== 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))


no = int(input("enter the no till what you want the series : "))
a = 1
b = 1
c = 0
print(a,end=' ')
print(b,end = ' ')
i = 1
while i <no:
    c= a +b
    b = a
    b = c
    i += 1
    print(c, end= ' ')











