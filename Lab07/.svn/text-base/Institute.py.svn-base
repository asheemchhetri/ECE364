import re
class Simulation:
    def __init__(self,simnNo,simDate,chipName,chipCount,chipCost):
        self.simulationNumber=simnNo
        self.simulationDate=simDate
        self.chipName=chipName
        self.chipCount=chipCount
        self.chipCost=chipCost
        self.simulationCost=self.chipCount*self.chipCost

    def __str__(self):
        return self.chipName+': '+format(self.simulationNumber,'03d')+", "+str(self.simulationDate)+', $'+format(self.simulationCost,'06.2f')

class Employee:
    def __init__(self,employeeName,employeeID):
        self.employeeName=employeeName
        self.employeeID=employeeID
        self.simulationsDict={}

    def addSimulation(self,sim):
        self.simulationsDict[sim.simulationNumber]=sim

    def getSimulation(self,simNo):
        if simNo not in self.simulationsDict.keys():
            return None
        else:
            return self.simulationsDict[simNo]

    def __str__(self):
        return self.employeeID+', '+self.employeeName+': '+format(len(self.simulationsDict),'02d')+' '+"Simulations"

    def getWorkload(self):
        string_list=[]
        for sim in self.simulationsDict.values():
            string_list.append(str(sim)+'\n')

        string_list.sort()
        string=(str(self)+'\n')
        for item in string_list:
            string+=item
        return string[:-1]

    def addWorkload(self,filename):
        with open(filename,"r") as file:
            lines=file.readlines()
            for line in lines[2:]:
                m=re.search(r"(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+\$(.*)",line)
                if m:
                    sim=Simulation(int(m.group(1)),m.group(2),m.group(3),int(m.group(4)),float(m.group(5)))
                    self.addSimulation(sim)



class Facility:

    def __init__(self,facilityName):
        self.facilityName=facilityName
        self.employeesDict={}

    def addEmployee(self,employee):
        self.employeesDict[employee.employeeName]=employee

    def getEmployees(self,*args):
        results=[]
        for name in args:
            results.append(self.employeesDict[name])
        return results

    def __str__(self):
        string=""
        string_list=[]
        string+=self.facilityName+": "+format(len(self.employeesDict),'02d')+" Employees\n"
        for employee in self.employeesDict.values():
            string_list.append(str(employee)+'\n')
        string_list.sort()
        for item in string_list:
            string+=item
        return string[:-1]

    def getSimulation(self,simNo):
        for employee in self.employeesDict.values():
            if employee.getSimulation(simNo):
                return employee.getSimulation(simNo)

        return None