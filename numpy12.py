import matplotlib.pyplot as plt
import numpy as np
year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
np_pop=np.array(pop)
np_pop=np_pop*20
plt.scatter(year,pop, s = np_pop)
plt.title("year wise polpulation")
plt.xlabel('year')
plt.ylabel('population')
plt.show()