# Identification of Points:
points = [
    (1,3),  # First point
    (3,7),  # Second point
    (7,9),  # Third point
    (7,3)   # Fourth point
]

# Writing a Function for Euclidean Distance:
def euclideanDistance(x1,y1,x2,y2):
    x_diff = (x2 - x1) ** 2  # Square of X difference
    y_diff = (y2 - y1) ** 2  # Square of Y difference
    distance = (x_diff + y_diff) ** 0.5  # Take the square root
    return distance

# Calculation of Distances:

# An empty list to store distances
distances = []

# Let's calculate distances by looking at all points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        # Calculate distance using the function
        distance = euclideanDistance(x1, y1, x2, y2)

        # Add the distance to the list
        distances.append(distance)

# Finding the Minimum Distance:

# Now let's find the minimum distance
min_distance = min(distances)  # Find the smallest of distances

print("Minimum Distance:", min_distance)  # Print on screen
