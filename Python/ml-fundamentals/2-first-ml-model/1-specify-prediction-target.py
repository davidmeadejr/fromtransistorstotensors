# print the list of columns in the dataset to find the name of the prediction target
home_data.describe()

# Select the target variable, which corresponds to the sales price. Save it to a new variable called y.
y = home_data.SalePrice