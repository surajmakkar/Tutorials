import pandas as pd
data=pd.read_csv("tips.csv")
#print(data.head(10))
#import pandas as pd
import matplotlib.pyplot as plt
plt.hist(data['total_bill'])
#plt.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])
plt.title("Histogram")
#plt.xlabel('Day')
#plt.ylabel('Tip')
#plt.colorbar()
plt.show()