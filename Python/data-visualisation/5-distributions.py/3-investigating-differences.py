# Histograms for benign and malignant tumors
sns.histplot(data=cancer_data, x="Area (mean)", hue="Diagnosis")
sns.histplot(data=cancer_data, x="Area (mean)", hue="Diagnosis")

# Add title
plt.title("Histogram of Area, by Diagnosis")