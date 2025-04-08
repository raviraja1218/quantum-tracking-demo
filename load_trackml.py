import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Simulate fake hits data
hits = pd.DataFrame({
    'x': np.random.normal(0, 100, 100),
    'y': np.random.normal(0, 100, 100),
    'z': np.random.normal(0, 300, 100)
})

print("✅ Generated simulated hits data.")
print(f"🔢 Loaded {len(hits)} hits.")

# Visualize hits in 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot hits (x, y, z coordinates)
ax.scatter(hits['x'], hits['y'], hits['z'], s=1, c='blue', alpha=0.6, label='Hits')
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
ax.set_title('Simulated TrackML Event - Particle Hits')
plt.legend()
plt.show()
