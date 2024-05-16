import pandas as pd

data = pd.read_csv('dataset.txt', sep='\t', header=None, names=['input_text', 'target_text'])
print(f"Veri kümesinin boyutu: {len(data)}")
