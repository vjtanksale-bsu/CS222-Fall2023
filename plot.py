import matplotlib.pyplot as plt
x  = ['Q1', 'Q2', 'Q3', 'Q4']
y = [10000, 12000, 11000, 8000]
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.title('Sales by quarter')
#plt.bar(x, y)
plt.plot(x,y, marker='o', color='yellow', linestyle='--')
plt.show()