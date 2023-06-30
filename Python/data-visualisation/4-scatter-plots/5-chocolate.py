# Scatter plot showing the relationship between "pricepercent", "winpercent", "chocolate"
sns.scatterplot(x=candy_data["pricepercent"], y=candy_data["winpercent"], hue=candy_data["chocolate"])