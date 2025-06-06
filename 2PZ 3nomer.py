import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]


plt.plot(x, y, marker='o')
plt.title('График собора в Гос Думе')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.show()