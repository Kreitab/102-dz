import matplotlib.pyplot as plt
subjects = ['1', '2','3','4']
y1 = [4, 5, 3, 4]
y2 = [4, 3, 3, 4] 
y3 = [4, 5, 5, 5] 
y4 = [4, 5, 5,4] 
x = range(len(subjects))
plt.figure(figsize=(2, 5))

plt.plot(x, y1, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
plt.plot(x, y2, marker='o', color='green', linestyle='-', linewidth=3, markersize=8)
plt.plot(x, y3, marker='o', color='black', linestyle='-', linewidth=5, markersize=8)
plt.plot(x, y4, marker='o', color='red', linestyle='-', linewidth=6, markersize=8)

plt.title('Оценки по предметам')
plt.xlabel('количество оценнок')
plt.ylabel('Оценки')
plt.xticks(x, subjects) 
plt.ylim(1, 6)
plt.axhline(2, color='gray', lw=0.5, ls='--') 
plt.axhline(5, color='gray', lw=0.5, ls='--') 


plt.tight_layout()
plt.show()