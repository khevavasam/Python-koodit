import numpy as np
import matplotlib.pyplot as plt

#-3π...3π
X = np.linspace(-3*np.pi, 3*np.pi, 256)
C = np.cos(X)
S = np.sin(X)

#kuva
plt.figure(figsize=(19.2, 4.8))

#käyrät eri väreillä ja tyyleillä
plt.plot(X, C, 'r--', label='cos(x)')
plt.plot(X, S, 'b:', label='sin(x)')

#selite ja akselit
plt.legend()
plt.xticks(
    [-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
    [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$']
)
plt.yticks([-1, 0, 1])

plt.show()
