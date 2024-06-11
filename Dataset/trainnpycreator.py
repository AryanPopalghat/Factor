import numpy as np
import os

# Specify the directory containing the individual .npy files
directory = "E:\\Aiwi\\FACTOR\\Dataset\\claimed_identity_features.npy"

# Initialize an empty list to store individual arrays
arrays = []

# Iterate over each .npy file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.npy'):
        # Load the array from the .npy file
        array = np.load(os.path.join(directory, filename))
        # Append the loaded array to the list
        arrays.append(array)

# Concatenate the arrays along the first axis to create a single 2D array
combined_array = np.vstack(arrays)

# Save the combined array into a single .npy file
np.save('train_combined_features.npy', combined_array)
