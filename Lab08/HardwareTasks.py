import string
def idIsAcceptable(ver_id):
    for item in ver_id:
        if item not in string.ascii_letters and item not in string.digits and item !='_':
            return False
    return True

def processSingle(ver_assignment):
    names=ver_assignment.split("(")
    port=names[0][1:]
    pin=names[1][:-1]
    if len(names) == 2 and ver_assignment[0]=='.' and ver_assignment[-1] == ')' and idIsAcceptable(port) and idIsAcceptable(pin):
        value=(port,pin)
        return value
    else:
        raise  ValueError(ver_assignment)

def processLine(ver_line):
    components=[]
    if(len(ver_line.split())>=3):
        components.append(ver_line.split()[0])
        components.append(ver_line.split()[1])
        components.append(ver_line.split()[2:])
    else:
        raise ValueError(ver_line)
    if len(components[2])==1:
        components[2][0]=components[2][0][1:-1]
        components[2]=components[2][0].split(",")
        components[2]=["("]+components[2]+[")"]
    if len(components) != 3 or not idIsAcceptable(components[0]) or not idIsAcceptable(components[1]) or components[2][0] != "(" or components[2][-1] != ")":
        raise ValueError(ver_line)
    else:
        list=[]
        assignments=components[2][1:-1]
        for item in assignments:
            if item[-1]==",":
                item=item[:-1]

            list.append(processSingle(item))
        list=tuple(list)
    return (components[0],components[1],list)




