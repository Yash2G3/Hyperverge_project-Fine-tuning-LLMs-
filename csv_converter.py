import pyarrow.parquet as pq

path = input("Enter the json file path: ")
data = pq.read_table(path)

df = data.to_pandas()

csv_save_path = input("Enter the path where you want to save the converted csv file along with the file name: ")
df.to_csv(csv_save_path)