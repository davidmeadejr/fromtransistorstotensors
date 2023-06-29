# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data['Avila Adobe'], label="Avila Adobe")
sns.lineplot(data=museum_data['Firehouse Museum'], label="Firehouse Museum")
sns.lineplot(data=museum_data['Chinese American Museum', label="Chinese American Museum"])
sns.lineplot(data=museum_data['America Tropical Interpretive Center', label="America Tropical Interpretive Center"])

# Displays the line graph
plt.show()