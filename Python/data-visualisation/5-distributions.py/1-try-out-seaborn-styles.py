# Change the style of the figure
sns.set_style("dark")

# Line chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)