def listParams(paramList):
    for item in paramList:
        return(str(item)+' ')
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

#def playInstrument(f, iNum, dur, iParams)
