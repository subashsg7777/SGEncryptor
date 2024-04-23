#import File 
'''import datetime
import time
tdate = datetime.date("DD/MM/YYYY")
ttime = datetime.time("HH:MM:SS")
print (tdate,ttime)'''
def readengine(length,index,data):
    op = ""
    print("the length of the data is :",length)
    for i in range(index,length):
        printer = data[index]
        #print(printer)
        index += 1
        if (printer == "a"): 
            op = op+"71"       
            print("71 ")
        
        elif (printer == "b"):
            print("77 ")
            op = op+"77"

        elif (printer == "c"):
            op = op+"81"
            print("87 ")

        elif (printer == "d"):
            op = op+"67"
            print("67 ")

        elif (printer == "e"):
            op = op+"57"
            print("57 ")

        elif (printer == "f"):
            op = op+"47"
            print("47 ")

        elif (printer == "h"):
            op = op+"37"
            print("37 ")

        elif (printer == "i"):
            op = op+"27"
            print("27 ")

        elif (printer == "j"):
            op = op+"17"
            print("17 ")

        elif (printer == "k"):
            op = op+"07"
            print("07 ")

        elif (printer == "l"):
            op = op+"36"
            print("36 ")

        elif (printer == "m"):
            op = op+"00"
            print("00 ")

        elif (printer == "n"):
            op = op+"78"
            print("78 ")

        elif (printer == "o"):
            op = op+"76"
            print("76 ")

        elif (printer == "p"):
            op = op+"75"
            print("75 ")

        elif (printer == "q"):
            op = op+"74"
            print("74 ")

        elif (printer == "r"):
            op = op+"73"
            print("73 ")

        elif (printer == "s"):
            op = op+"72"
            print("72 ")

        elif (printer == "t"):
            op = op+"06"
            print("06 ")

        elif (printer == "w"):
            op = op+"97"
            print("97 ")

        elif (printer == "x"):
            op = op+"79"
            print("79 ")

        elif (printer == "y"):
            op = op+"18"
            print("18 ")

        elif (printer == "z"):
            op = op+"81"
            print("81 ")

        elif (printer == "u"):
            op = op+"09"
            print("09 ")

        elif (printer == "v"):
            op = op+"08"
            print("08 ")

    print("the whole data in encrypted form is :",op)
    print(data)
    '''source.close()
    loging = open("log.txt")
    plog= loging.readlines()
    loging.writelines(plog,op+"")'''

#here is the write engine 

def writeengine(data,length,index):
    op = ""
    print("the length of the data is :",length)
    for i in range(index,length):
        printer = data[index:index+2]
        #print(printer)
        index += 2
        if (printer == "71"): 
            op = op+"a"       
            print("a ")
        
        elif (printer == "77"):
            print("b ")
            op = op+"b"

        elif (printer == "87"):
            op = op+"c"
            print("c ")

        elif (printer == "67"):
            op = op+"d"
            print("d ")

        elif (printer == "57"):
            op = op+"e"
            print("e ")

        elif (printer == "47"):
            op = op+"f"
            print("f ")

        elif (printer == "37"):
            op = op+"h"
            print("h ")

        elif (printer == "27"):
            op = op+"i"
            print("i ")

        elif (printer == "17"):
            op = op+"j"
            print("j ")

        elif (printer == "07"):
            op = op+"k"
            print("k ")

        elif (printer == "36"):
            op = op+"l"
            print("l ")

        elif (printer == "00"):
            op = op+"m"
            print("m ")

        elif (printer == "78"):
            op = op+"n"
            print("n ")

        elif (printer == "76"):
            op = op+"o"
            print("o ")

        elif (printer == "75"):
            op = op+"p"
            print("p ")

        elif (printer == "74"):
            op = op+"q"
            print("q ")

        elif (printer == "73"):
            op = op+"r"
            print("r ")

        elif (printer == "72"):
            op = op+"s"
            print("s ")

        elif (printer == "06"):
            op = op+"t"
            print("t ")

        elif (printer == "97"):
            op = op+"w"
            print("w ")

        elif (printer == "79"):
            op = op+"x"
            print("x ")

        elif (printer == "18"):
            op = op+"y"
            print("y ")

        elif (printer == "81"):
            op = op+"z"
            print("z ")

        elif (printer == "09"):
            op = op+"u"
            print("u ")

        elif (printer == "08"):
            op = op+"v"
            print("v ")

    print("the whole data in encrypted form is :",op)
    print(data)

'''source = open("samplesource.sg")
data = source.readlines()
index = 2
data = str(data)
length = len(data)
length = length-2'''
reversesource = open("encrypted.txt")
data = reversesource.readlines()
index = 2
data = str(data)
length = len(data)
length = length-2

#readengine(index = index,data=data,length=length)
writeengine(index = index,data=data,length=length)
