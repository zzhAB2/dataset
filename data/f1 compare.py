import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
y_bwdgv = np.array([0,0
,63
,69
,73.4
,76.5
,81.2
,82.6
,84.2
,84.2
,86.3
,86.2
,85.7
,85.9
,86.4
,86.6
,86.8
,86.3
,86.9
,87.2  ])  # 训练准确率值，即y轴
y_prgc=np.array([0
,39.8
,63.7
,74.8
,80.0
,82.5
,82.6
,84.7
,82.0
,84.5
,86.0
,84.9
,85.5
,86.2
,85.4
,086.8
,86.2
,86.2
,86.0
,86.4
])
y_CasRel=np.array([
65.2
,76.9
,79.5
,80.3
,81.2
,81.4
,81.7
,81.8
,82.1
,81.8
,82.4
,82.0
,82.1
,82.2
,82.6
,82.1
,82.1
,82.3
,82.1
,82.0
])

y_OneRel=np.array([
0
,0
,0
,0
,12.1
,25.0
,42.4
,52.5
,60.2
,68.6
,72.0
,74.8
,77.0
,75.4
,78.7
,80.7
,81.4
,81.6
,82.0
,82.5
])
x_train_acc = np.array([i for i in range(1,21)]) # 训练阶段准确率的数量，即x轴

plt.figure()
plt.xlabel('epochs')  # x轴标签
plt.ylabel('F1-score')  # y轴标签


def smooth_curve(points, factor=0.3):
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
plt.savefig("f1.jpg",dpi=500)

plt.show()

