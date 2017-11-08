
#Diagram Data Set

import matplotlib.pyplot as plt ; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python','Java','C#','C++','Clojure',' Javascript ','C','Go')
y_pos = np.arange(len(objects))
n = [12,20,6,10,4,14,10,3]

plt.bar(y_pos,n,align = 'center',alpha = 0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Pengunaan')
plt.title("Pengunaan Bahasa Pemprograman")
plt.show()


#Pie Data Set
labels = ('Python','Java','C#','C++','Clojure',' Javascript ','C','Go')
sizes = [12,20,6,10,4,14,10,3]
colors = ['gold','yellow','blue','red','pink','cyan','green','purple']
explode = (0.1, 0, 0, 0,0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
