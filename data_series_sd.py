#calculate(m, xData): returns Standard Deviation of number series
#       m = Arithmetic Mean of xData series
#       xData = number series

def calculate(m, xData):
    xData = [float(x) for x in xData]
    return (sum([(x-m)**2 for x in xData])/len(xData)) ** 0.5