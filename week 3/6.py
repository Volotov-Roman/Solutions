import numpy as np
x=np.array([2,3,4,5,6,7])
y=np.array([0,1,2,3,4,5])
#МНК:
a=(np.mean(x*y)-np.mean(x)*np.mean(y)) / (np.mean(x**2)-np.mean(x)**2)
b=np.mean(y)-a*np.mean(x)

#Стандартное отклонение:
std_a= 1/np.sqrt(len(x))*np.sqrt((np.mean(y**2)-np.mean(y)**2)/((np.mean(x**2)-np.mean(x)**2))-a**2)
std_b=std_a*np.sqrt(np.mean(x**2)-np.mean(x)**2)