import numpy as np

# Create the labels array
# 1 for real (authentic), 0 for fake (attack)
labels = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Save the labels array to a .npy file
np.save('test_set_labels.npy', labels)

# To confirm, load the array and print it
loaded_labels = np.load('test_set_labels.npy')
print(loaded_labels)
