# Set the width and height of the figure
plt.figure(figsize=(8, 6))

# Bar chart showing the average score for racing games by platform
sns.barplot(x=ign_data["Racing"], y=ign_data.index)

# Add label for horizontal axis
plt.xlabel("")

# Add label for vertical axis
plt.title("Average Score for Racing Games, by Platform")
