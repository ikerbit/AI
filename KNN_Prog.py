from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt 

# Defining data
x = [2, 3, 8, 7, 6, 12, 14, 9, 11, 13]
y = [18, 16, 20, 15, 14, 22, 20, 19, 18, 18]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# Create KNN classificator
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(np.column_stack((x, y)), classes)

# Define the new point to be classified
new_point = np.array([[6, 20]])

# Classify the new point
predicted_class = knn_classifier.predict(new_point)
print(f"The predicted class for the new point {new_point} is: {predicted_class[0]}")

# Create a scatter plot with the new colored dot
plt.scatter(x, y, c=classes)
plt.scatter(new_point[0, 0], new_point[0, 1], marker='X', c='red', label='New point')
plt.legend()

# Save the graphic as a PNG image
plt.savefig('scatter_plot.png')
