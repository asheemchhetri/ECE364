import re
def warmup1():
    input=" A A AAA AAAAAA"
    m=re.search(r"(\sA{2,5}\s)",input)
    if m:
        print(m.groups())
    else:
        print("Not found")

def warmup2():
    input=" 12.35 is a float"
    m=re.sub(r"(\d+\.\d+)","float",input)
    if m:
        print(m)
    else:
        print("Not found")

def warmup3():
    input=" 12.35 and 1.35 are floats"
    m=re.subn(r"(\d+\.\d+)","float",input)
    if m:
        print(m)
    else:
        print("Not found")

def warmup4():
    input=" 1 2 3 4 5 6 string "
    m=re.findall(r"([0-9]+)",input)
    if m:
        print(sum([int(item) for item in m])/len(m))
    else:
        print("Not found")

def warmup5():
    input="ECE364 ECE364 ECE264"
    m=re.sub(r"ECE\d{3}","ECE461",input,1)
    if m:
        print(m)
    else:
        print("Not found")

def warmup6():
    input=" 128.210.011.007 0.0.0.0 3132.132.3213213.23132 "
    m=re.findall(r"(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})",input)
    if m:
        print(m)
    else:
        print("Not found")

if __name__ == '__main__':
    warmup6()