import HardwareTasks
def verilog2vhdl(ver_line):
    try:
        t=HardwareTasks.processLine(ver_line)
        string=""
        string+=t[1]+": "+t[0]+" PORT MAP("
        for item in t[2]:
            string+=item[0]+"=>"+item[1]+", "
        string=string[:-2]
        string+=");"
        return string
    except:
        return "Error: Bad Line."

def convertNetlist(sourceFile,targetFile):
    with open(sourceFile,"r") as infile:
        with open(targetFile,"w") as outfile:
            lines=infile.readlines()
            for line in lines[:-1]:
                line=line[:-1]
                outfile.write(verilog2vhdl(line)+"\n")
            outfile.write(verilog2vhdl(lines[-1]))