#extract(xColName, srcTSVFile): extracts a column from source csv string
#       xColName = name of column with values to extract
#       srcCSVFile = passed by main program, which reads this value from file or stdin

def extract(xColName, srcCSVFile):
    xData = []
    xCol = None
    for line in srcCSVFile:
        if xCol is not None:
            xData.append(line.split(',')[xCol])
        else:
            xCol = line.rstrip().split(',').index(xColName)
    return xData