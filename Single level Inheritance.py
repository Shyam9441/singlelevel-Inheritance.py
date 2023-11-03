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




