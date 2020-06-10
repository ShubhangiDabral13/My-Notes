import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
ages_x = [25,26,27,28,29,30,31,32,33,34,35]

x_indexex = np.arange(len(ages_x))
#defining thw width of the bar so that we can shift the value of the bars
width = 0.25

dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]

plt.bar(x_indexex - width,dev_y,width = width,color = "#444444",label = "All Devs")

py_dex_y = [45372,48876,53850, 57287,63016,65998,70003,70000,71496,75370,83640]

plt.bar(x_indexex,py_dex_y,width = width ,color = "#5a7d9a",label = "Python")

js_dev_y = [37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]
plt.bar(x_indexex + width,js_dev_y,width = width ,color = "#e5ae38",label = "JavaScript")

#xticks so that ages value can be assigned at the x axis rather than x_indexex
plt.xticks(ticks= x_indexex,labels = ages_x)
plt.xlabel("Ages")
plt.ylabel("Median salary (USD)")
plt.title("Median salary (USD) by age")

#Legend are added to tell which line  is for what
#plt.legend(["All Devs","Python"])
plt.legend()

#To add grid
#plt.grid()

#automatically adjust plot parameters to give it padding.
plt.tight_layout()

#to save the plot
#plt.savefig("plot.png")

plt.show()
