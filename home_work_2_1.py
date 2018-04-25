import sys,math
x = float(sys.argv[1])
m = float(sys.argv[2])
q = float(sys.argv[3])
result = (1/(q*math.sqrt(2*math.pi)))*math.exp((-(((x-m)**2)/(2*q**2))))
print result
