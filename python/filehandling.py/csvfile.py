import csv
with open(r'C:\Users\User\Desktop\python BI Rabindra sir\python\filehandling.py\mycsvfile.csv', 'r') as file_obj:
    csv_reader=csv.reader(file_obj)
    data=list(csv_reader)
print(data)