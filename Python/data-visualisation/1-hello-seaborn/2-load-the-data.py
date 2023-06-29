# Path of file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable called fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse=True)