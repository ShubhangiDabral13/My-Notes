from matplotlib import pyplot as plt
dev_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496,4200,46752,49320,53200,56000,62316,64928,67317,68748,73752]

plt.plot(dev_x,dev_y)

plt.xlabel("Ages")
plt.ylabel("Median salary (USD)")
plt.title("Median salary (USD) by age")

plt.show()
