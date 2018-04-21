#readFileName = "cabs_CsScore_v1.cs"
def retrieveLineInfo(line):
    return(line.split())

def readScore(fileName):
    pieceArray = []
    with open(fileName) as f:
        for line in f:
            #line = f.readline()
            lineParts=retrieveLineInfo(line)
            pieceArray.append(lineParts[1:])
    f.closed
    return(pieceArray)
# Try it
