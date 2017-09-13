import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 4.5 * np.cos(np.pi*t)+2013

t1 = np.arange(0.0,5.0,.02)
plt.title('Vida estudiantil de Diana', color = 'blue')
plt.ylabel('Anios en la Licenciatura', color = 'orange')
plt.xlabel('semestres', color = 'green')
plt.plot(t1, f(t1), 'g--', linewidth=1)
plt.ylim(2013,2017)
plt.xlim(1,5)
plt.savefig('examen2.png')

plt.show()