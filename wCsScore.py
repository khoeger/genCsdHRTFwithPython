def listParams(paramList):
    paramStr = ''
    for item in paramList:
        paramStr += str(item)+' \t'
    return(paramStr)
def funcTable(f, tableNum, time, tableSize, genNum, paramsGen):
    """
        Generate F statment
            - Cause a GEN subroutine to place values in stored function table
            - f p1  p2  p3  p4  p5 ... PMAX
        tableNum = function table number
        time = action time of function generation
        tableSize = function table size
        genNum = Number of Gen Routine called
        paramsGen = parameters determined by function
        See http://csounds.com/manual/html/f.html
    """
    f.write('f'+str(tableNum)+' \t'+str(time)+' \t'+str(tableSize)+' \t'+str(genNum))
    f.write(' \t'+listParams(paramsGen)+'\n')

def playNote(f, iNum, start, dur, iParams):
    """ iiNum start dur iParams
        http://www.csounds.com/manual/html/i.html
        if want chord, iNum needs to be decimal, iNum.noteNum
    """
    f.write('i'+str(iNum)+' \t'+str(start)+' \t'+str(dur))
    f.write(' \t'+listParams(iParams)+'\n')
    pass
