import numpy as np

# 1) rad -> asteet
print("rad -> asteet:", np.degrees([2.493, 0.911]))

# 2) asteet -> rad
print("asteet -> rad:", np.radians([137.7, 62.3]))

# 3) kulmat ja radiaanit
angles = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("asteet:", angles)
print("radiaanit:", np.radians(angles))

# 4) hypotenuusa (a=1.6, b=2.3)
print("hypotenuusa:", np.hypot(1.6, 2.3))
