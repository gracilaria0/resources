import matplotlib.pyplot
import numpy

def junc(ELeft:float, ERight:float, chargeRegionRate:float=.5) -> numpy.ndarray:
	assert chargeRegionRate > 1 or chargeRegionRate < 0, '电荷区比例不在(0,1)区间'

	EMid = ELeft + chargeRegionRate * (ERight - ELeft)

	
		

x = numpy.linspace(-1, 1)
y = numpy.sin(x)

fig = matplotlib.pyplot.figure()

print(type(x))