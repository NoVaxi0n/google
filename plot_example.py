import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Save the plot to a file (you can specify the file format with the file extension)
plt.savefig('line_plot.png')

# Optionally, you can specify additional parameters such as DPI (dots per inch) for image quality
# plt.savefig('line_plot.png', dpi=300)

# Close the plot to free up resources
plt.close()
