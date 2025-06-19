import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
y_bwdgv = [0
,0
,65.4
,72.1
,79.7
,77.3
,82.0
,78.4
,82.1
,81.3
,86.1
,85.6
,83.6
,84.4
,85.1
,85.8
,85.6
,85.2
,85.8
,86.0 ]  # 训练准确率值，即y轴
y_prgc=[0
,68.1
,59.6
,75.5
,76.7
,79.8
,78.2
,83.5
,79.9
,81.5
,85.4
,84.1
,83.4
,85.6
,84.1
,86.0
,84.9
,85.4
,83.9
,85
]
y_CasRel=[
73.5
,80.0
,80.0
,79.1
,80.3
,81.0
,81.8
,80.4
,82.1
,80.5
,82.4
,81.4
,81.8
,82.6
,82.3
,81.7
,81.6
,81.8
,82.5
,82.2
]

y_OneRel=[
0
,0
,0
,0
,96.6
,87.7
,74.5
,80.2
,75.3
,75.1
,77.3
,76.1
,78.9
,75.4
,79.0
,84.6
,81.6
,84.3
,83.1
,84.0
]
x_train_acc = [i for i in range(1,21)] # 训练阶段准确率的数量，即x轴

plt.figure()
plt.xlabel('epochs')  # x轴标签
plt.ylabel('prec')  # y轴标签

def smooth_curve(points, factor=0.5):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            # 上一个节点*0.8+当前节点*0.2
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            # 添加point
            smoothed_points.append(point)
    return smoothed_points

# 以x_train_acc为横坐标，y_train_acc为纵坐标，曲线宽度为1，实线，增加标签，训练损失，
# 增加参数color='red',这是红色。
plt.plot(x_train_acc, smooth_curve(y_bwdgv), color='red', linewidth=0.5, linestyle="solid", label="Bwdgv")
plt.plot(x_train_acc, smooth_curve(y_prgc), color='blue', linewidth=0.5, linestyle="solid", label="PRGC")
plt.plot(x_train_acc, smooth_curve(y_CasRel), color='green', linewidth=0.5, linestyle="solid", label="CasRel")
plt.plot(x_train_acc, smooth_curve(y_OneRel), color='grey', linewidth=0.5, linestyle="solid", label="OneRel")

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(4))
plt.legend(loc='lower right',fontsize=8)
plt.savefig("prec.jpg",dpi=500)

plt.show()
