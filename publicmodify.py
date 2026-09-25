class public:
    def __init__(self):
        self.name = "Swinu"
    def show(self):
        print(f"name is: {self.name}")

obj=public()
obj.show() 
print("Access public variable outside class, ", obj.name)
