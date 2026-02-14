import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Data in radians
x = np.linspace(0, 2*np.pi, 1000)
line, = ax.plot(x, np.sin(x), linewidth=2)

# Axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Labels and title
ax.set_title("Animated Sine Wave")
ax.set_xlabel(r"$\theta$ (radians)")
ax.set_ylabel(r"$\sin(\theta + t)$")

# Set π-based ticks
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels([
    r"$0$",
    r"$\frac{\pi}{2}$",
    r"$\pi$",
    r"$\frac{3\pi}{2}$",
    r"$2\pi$"
])

ax.grid(True)

# Update function
def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50)

# Save video (requires ffmpeg installed)
ani.save("sine_wave_radians.mp4", writer="ffmpeg", fps=30)

plt.show()
