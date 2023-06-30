# Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent'
sns.regplot(x=candy_data["sugarpercent"], y=candy_data["winpercent"])