class Employee:
    def __init__(self):
        print("EMPLOYEE CREATED")

    def __del__(self):
        print("DESTRUCTOR CALLED")

def  Create_obj():
        print("MAKING OBJECT...")
        obj = Employee()
        print("FUNCTION END...")
        return obj
print("CALLING CREATE_OBJ FUCTION...")
obj = Create_obj()
print("PROGRAM END...")