class Address:
    __address: str = ""
    def addAddress(self,address):
        self.__address = address
    def getAddress(self):
            return self.__address
class Employee(Address):
    __fitsrName: str = ""
    __lastName: str = ""
    __surName: str = ""

    def setName(self, fName: str, lName: str, sName: str= ""):
        self.__fitsrName = fName
        self.__surName = sName
        self.__lastName = lName
    def __nameFormat(self):
        return f'{ self.__fitsrName } {self.__lastName} {self.__surName}'
    def getFullName(self):
        return self.__nameFormat()
emp = Employee()
emp.setName(fName="Shyam Raj", sName="b", lName="battu")
emp.addAddress("Nizamabad")
print(emp.getFullName())
print(emp.getAddress())

class PerminentEmployee(Employee):
    __sal: int = 30000
    def salcal(self)->float:
        return 12*self.__sal
pemp= PerminentEmployee()
pemp.setName (fName="sai",sName="G",lName="sundhar")
pemp.addAddress("Hyderabad")
print(pemp.getFullName())
print(pemp.getAddress())
print(pemp.salcal())

class ContractEmployee(Employee):
    __hr_pay: int = 300
    def salcal(self, hrs: int) -> str:
        return f'salcal for {hrs} hrs: {self.__hr_pay*hrs}'
cemp= ContractEmployee()
cemp.setName (fName="sai",sName="G",lName="sundhar")
cemp.addAddress("Hyderabad")
print(cemp.getFullName())
print(cemp.getAddress())
print(cemp.salcal(20))

class classB:
    def printData(self):
        print(1)
class ClassC:
    def printData(self):
        print(2)
class classA (classB,ClassC):
        pass

a=classA()
a.printData()
