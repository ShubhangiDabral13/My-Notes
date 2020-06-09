from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
ages_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496,4200,46752,49320,53200,56000,62316,64928,67317,68748,73752]

plt.plot(ages_x,dev_y,color = "#444444",linestyle = "--",label = "All Devs")

py_dex_y = [45372,48876,53850, 57287,63016,65998,70003,70000,71496,75370,83640]

plt.plot(ages_x,py_dex_y,color = "#5a7d9a",linewidth = 3,label = "Python")

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
