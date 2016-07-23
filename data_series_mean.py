#calculate(xData): returns Arithment Mean of number series
#       xData = number series

def calculate(xData):
    xData = [float(x) for x in xData]
    return sum(xData)/len(xData)