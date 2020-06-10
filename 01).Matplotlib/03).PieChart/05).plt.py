from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]

#To add labels to our pie chart
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

#use to define by how much we want to emphasis on the slice we are emphasising on.
explode = [0, 0 , 0 , 0.1,0]
# The above explode list will emphasis on the 4th slice which is python.

#To add separator at the edges of the slices add wedgeprops parameters
#To add shadow to your slices make shadow parameter equal to True.
#To rotate your chart use parameter startangle and assign the ngle by which you want to rotate it.
#To add percentage of each slice use parameter autopct
plt.pie(slices,labels = labels, explode = explode, shadow = True, startangle = 90, autopct = "%1.1f%%",wedgeprops = {"edgecolor":"black"})

plt.title("My Awesome Pie Chart")
plt.tight_layout()

plt.show()

"""
Note :-
PieChart does not look good for large amount of data. They work fine if data is 5-6
"""
