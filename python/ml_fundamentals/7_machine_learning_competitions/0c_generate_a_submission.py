# Rub the code to save predictions in the format used for competition scoring

output = pd.DataFrame({"Id": test_data.Id, "SalePrice": test_preds})
output.to_csv("submission.csv", index=False)