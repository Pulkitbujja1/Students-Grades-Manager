# import ctypes 
# # isme ham  c ke array ko use karke python ka list banayenge

# class Meralist :

#     def __init__(self) :
#         self.size = 1    # maxmium kitne item store kar sakte hai 
#         self.n = 0       # abhi kitne item store hai
    
#     # create c type array wit size = self.size
#         self.A = self.__make__array(self.size)       # kyuki ye function class ke andar hai isliye hame self ka use karna pad rha hai
#     # variable ka naam hai A

#     def __make_array(self,capacity):                 # kitni length ka array banana hai
#         return (capacity*ctypes.py_object)()         # capacity times ctyps(module name)
        # (capacity*ctypes.py_object)() this code creates a C type array(static,referential) with size capacity
        # py_boject says that I want to store normal Python objects here — like numbers, strings, or anything else



# detail of this code 


 # Let’s say capacity = 4. Then this line becomes:

# 4 * ctypes.py_object
# This actually tells Python to make a new data type that is like:

# “An array of 4 Python objects.”

# 🔧 This is not a normal Python list ([]) — it's a special low-level memory space that acts like an array, built using ctypes.



# detail of this code 


# (capacity * ctypes.py_object)
# Just defines the type of array.

# But adding the () at the end: Actually creates the array in memory — it constructs an empty array that can hold capacity number of Python objects.


import ctypes

class Meralist:

    def __init__(self):
        self.size = 1    
        self.n = 0   
        self.A = self.__make_array(self.size)         # call function 
    
    def __len__(self) :
        return self.n       # agar kabhi len ka use kiya to self.n de dena
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' +result[:-1] + ']'
    
    def __getitem__(self,index) :
       if 0<= index  < self.n:
        return self.A[index]
       else :
           return "indexerror - index out of range"

    def pop(self):
        if self.n == 0:
            return "empty list"
        
        print(self.A[self.n-1])
        self.n = self.n - 1
    
    def clear(self):
         self.size = 1    
         self.n = 0  

    def find(self,item) :
        for  i in range(0,self.n) :
            if self.A[i] == item:
                return i

        return 'valueError Not in list'

    def insert(self,pos,item) :
        if self.n == self.size :
            self.__resize(self.size*2)
        
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n += 1
    
    def __delitem__(self,pos) :
        #delete

      if  0<= pos <self.n:
        for i in range(pos,self.n-1) :
            self.A[i] = self.A[i+1]
        
        
        self.n -= 1

    def remove(self,item):
        pos = self.find(item)   # ye code muijhe positon de dega

        if type(pos) == int:
            # delete
           self.__delitem__(pos)
       
        else :
           return pos

    

    def append(self,item) :
      if self.n == self.size:
            # resize
        self.__resize(self.size*2)       # call function

        # append
      self.A[self.n] = item
      self.n = self.n + 1
    
    def __resize(self,new_capacity) : 
        # create a new array with new capcity 
        B = self.__make_array(new_capacity)   # b is new array whose size is double of array
        self.size = new_capacity              # size double ho chuka hai aur isko hum update kar denge
        
        # copy the contant of A to B
        for i in range(self.n) :
            B[i] = self.A[i]
        # reassign A
        self.A = B
     
    


    def __make_array(self, capacity):                 
        return (capacity * ctypes.py_object)()   # return an empty array with size capacity

L = Meralist()
# print(len(L))

L.append(1)
L.append("pulkit")
L.append(4)
# print(L)

# print(L[0])
# print(L[3])

# L.pop()
# print(L)

# L.clear()
# print(L)

# print(L.find(4))
# print(L.find(40))

# L.insert(1,45)
# print(L)

# del L[0]
# print(L)

L.remove('pulkit')
print(L)

L.remove(4)
print(L)

L.remove(233)
print(L)