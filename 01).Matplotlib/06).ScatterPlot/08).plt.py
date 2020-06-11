import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

#paramter s is used to size the ball of the scatter plot.
#paramter c is used to give color to the balls
#marker is used to give design to the balls.
#plt.scatter(x,y,s = 100, c= "green",maker = "X")


data = pd.read_csv('data2.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

#alpha is given to soften the color little bit.
#cmap to give colors to different shades of grey of colors list.
plt.scatter(view_count,likes,c= ratio,cmap = "summer",edgecolor = "black",linewidth = 1 , alpha = 0.75)

#To add color bars
cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")


plt.xscale("log")
plt.yscale("log")
plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
