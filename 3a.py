import matplotlib.pyplot as plt
a = int(input('Введи число: '));
b = [];
while (a!=1):
    if (a%2 == 0):
        a = a/2;
    else:
        a = a*3;
        a = a+1;
    b.append(a);
fig, ax = plt.subplots();
ax.plot(b);