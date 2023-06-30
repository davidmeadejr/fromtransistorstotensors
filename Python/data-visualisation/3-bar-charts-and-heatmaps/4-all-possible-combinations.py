# Heatmap showing average game score by platform and genre

# Set the width and height of the figure
plt.figure(figsize=(14, 7))

# Add title
plt.title("Average Video Game Score by Genre and Platform")

# Heatmap showing the average video game score by genre and platform
sns.heatmap(data=ign_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Genre")

