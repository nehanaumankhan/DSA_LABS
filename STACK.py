import ctypes
class stack:
    def __init__(self,n) : # n is the size of stack
        self.MAXSTK = n # Maximum size of stack is n
        self.STACK=(ctypes.py_object*n)()   # initializing an array of size n
        self.TOS=-1 # Top of stack is -1 when the stack is empty


    def __str__(self) :
        stack_list = '['
        for i in range(self.TOS+1):
            stack_list += str(self.STACK[i])
            if i != self.TOS:
                stack_list += ','
        stack_list += ']'
        return stack_list


    def PUSH(self,ITEM):
        if self.TOS == (self.MAXSTK - 1): #Checking for overflow condition
            print("OVERFLOW!!!")
            return
        self.TOS += 1
        self.STACK[self.TOS] = ITEM


    def POP(self):
        if self.TOS == -1:  #Checking for underflow condition
            print("UNDERFLOW!!!!")
            return
        ITEM = self.STACK[self.TOS]
        self.TOS -= 1
        return ITEM
              

