# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# print the top few validation predictions
print(iowa_model.predict(val_X.head()))

# print the top few actual prices from validation data
print(iowa_model.predict(train_X.head()))