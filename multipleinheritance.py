class A:     
      def display_A(self):        
         print("This is A class")
class B: 
       def display_B(self):
          print("This is B class")
class C(A,B):
      def display_C(self):    
         print("This is C class")

C1 = C()
C1.display_A()
C1.display_B()
C1.display_C()            
