
import numpy as np
import matplotlib.pyplot as plt

# Load the matrices
matrix_A = np.load('totalFitnessData.npy')
matrix_B = np.load('totalFitnessData2.npy')

# Calculate the column means
means_A = np.mean(matrix_A, axis=0)
means_B = np.mean(matrix_B, axis=0)

# Create the x-axis
x_axis = np.arange(matrix_A.shape[1])

# Create the plot
plt.plot(x_axis, means_A, label='Matrix A')
plt.plot(x_axis, means_B, label='Matrix B',linewidth = 4)

# Add axis labels and legend
plt.xlabel('Generation Index')
plt.ylabel('Fitness Value')
plt.legend()

# Display the plot
plt.show()
