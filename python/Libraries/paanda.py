import pandas as pd
file_path= r"C:\Users\User\Downloads\2022-01-02.csv"
df=pd.read_csv(file_path)
print(df.head(3)) #records from top
print(df.tail(5)) #5 records from bottom
print(df.sample(8)) #8 random records

# filter_condition= (df["Conf." > 50] & ["Conf."<55])