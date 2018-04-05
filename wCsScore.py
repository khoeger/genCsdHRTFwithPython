def listParams(paramList):
    paramStr = ''
    for item in paramList:
        paramStr += str(item)+' '
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
    f.write('f'+str(tableNum)+' '+str(time)+' '+str(tableSize)+' '+str(genNum))
    f.write(' '+listParams(paramsGen)+'\n')

def playNote(f, iNum, start, dur, iParams):
    """ iiNum start dur iParams
        http://www.csounds.com/manual/html/i.html
        if want chord, iNum needs to be decimal, iNum.noteNum
    """
    f.write('i'+str(iNum)+' '+str(start)+' '+str(dur))
    f.write(' '+listParams(iParams)+'\n')
    pass
