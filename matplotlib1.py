import matplotlib.pyplot as plt
#year=[1950,1970,1990,2010]
#pop=[2.519,3.692,5.263,6.972]
#plt.plot(year,pop)
#plt.title("year wise polpulation")
#plt.xlabel("year")
#plt.ylabel("population")
#tick_val=[1950,1970,1990,2010]
#tick_lab=['1950year','1970year','1990year','2010year']
#plt.xticks(tick_val,tick_lab)
#plt.yticks([2,3,4,5,6,7],['2B','3B','4B','5B','6B','7B'])
#plt.show()

year=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
temp=[32,34,37,37.5,39,36,34,38,40,43,47,49,51]
plt.plot(year,temp)
plt.title("year wise temperature variation")
plt.xlabel("year")
plt.ylabel("temperature in Celsius")
tick_val=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
tick_lab=['1900year','1910year','1920year','1930year','1940year','1950year','1960year','1970year','1980year','1990year','2000year','2010year','2020year']
plt.xticks(tick_val,tick_lab)
plt.yticks([32,34,37,37.5,39,36,34,38,40,43,47,49,51])
plt.show()