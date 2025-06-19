import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
y_bwdgv = [0
,0
,60.7
,66.1
,60.7
,66.1
,68.1
,75.8
,80.4
,87.2
,86.5
,87.9
,86.8
,86.8
,87.8
,87.6
,87.8
,87.5
,88.0
,88.4] 
y_prgc=[0
,28.1
,68.5
,74.1
,83.7
,85.5
,87.5
,85.9
,84.1
,87.7
,86.6
,85.4
,87.5
,86.4
,86.4
,87.1
,87.6
,87.1
,87.5
,87.0
]
y_CasRel=[
58.5
,74.1
,79.0
,81.5
,82.1
,81.8
,81.6
,83.2
,82.2
,83.1
,82.4
,82.6
,82.4
,81.8
,82.8
,82.5
,82.5
,83.3
,81.6
,82.2
]

y_OneRel=[
0
,0
,0
,0
,6.5
,14.6
,29.6
,39.0
,50.1
,63.1
,67.4
,76.1
,78.9
,75.5
,78.3
,77.2
,79.1
,79.0
,80.9
,81.1
]
x_train_acc = [i for i in range(1,21)] 

plt.figure()
plt.xlabel('epochs')  
plt.ylabel('recall') 

def smooth_curve(points, factor=0.5):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
  
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:

            smoothed_points.append(point)
    return smoothed_points



plt.plot(x_train_acc, smooth_curve(y_bwdgv), color='red', linewidth=0.5, linestyle="solid", label="Bwdgv")
plt.plot(x_train_acc, smooth_curve(y_prgc), color='blue', linewidth=0.5, linestyle="solid", label="PRGC")
plt.plot(x_train_acc, smooth_curve(y_CasRel), color='green', linewidth=0.5, linestyle="solid", label="CasRel")
plt.plot(x_train_acc, smooth_curve(y_OneRel), color='grey', linewidth=0.5, linestyle="solid", label="OneRel")

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(4))
plt.legend(loc='lower right',fontsize=8)
plt.savefig("recall.jpg",dpi=500)

plt.show()
