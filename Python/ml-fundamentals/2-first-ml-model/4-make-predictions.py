predictions = iowa_model.predict(X)
print(predictions)

# Use the head method to compare the top few predictions to the actual home values (in y)
# for those same homes. Anything surprising?

print(iowa_model.predict(X.head()))
print(y.head())