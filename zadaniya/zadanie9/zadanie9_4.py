import numpy as np
import matplotlib.pyplot as plt
import os
def f(x, alpha, beta):
    return (x**beta + alpha**beta)/x**beta
dir = os.getcwd()

# Значения x для основного графика
x_main = np.linspace(-100, 100, 5000)

# Значения x для врезки
x_inset = np.linspace(-100, 100, 4000)

# Параметры для графиков
alphas = [1, 1, 1]
betas = [0.5, -0.5, -1.5]
colors = ['g', 'y', 'r']
labels = [rf'$\alpha={a}, \beta={b}$' for a, b in zip(alphas, betas)]

# Основной график
fig, ax = plt.subplots()
for alpha, beta, color, label in zip(alphas, betas, colors, labels):
    ax.plot(x_main, f(x_main, alpha, beta), color=color, label=label)
    
# Прямые f(x) = 0, x = 0
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Врезка
inset_ax = fig.add_axes([0.55, 0.15, 0.35, 0.25])
for alpha, beta, color, label in zip(alphas, betas, colors, labels):
    inset_ax.plot(x_inset, f(x_inset, alpha, beta), color=color, label=label)

# Прямые f(x) = 0, x=0 на врезке
inset_ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Оформление основного графика
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 7.5])
plt.axvline(x=0, color='black', linewidth=1)
ax.set_title('Функции типа (x**b + a**b)/x**b при разных значениях a и b')
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.legend()

# Оформление врезки
inset_ax.set_xlim([0, 5])
inset_ax.set_ylim([0, 5])
inset_ax.set_title('Поведение графиков при $x \\rightarrow -\infty$')
inset_ax.set_xlabel('$x$')
inset_ax.set_ylabel('$f(x)$')
inset_ax.grid(True)
inset_ax.legend(loc='lower right')
plt.savefig(dir + '/zadanie9_4', dpi=300)
plt.show()