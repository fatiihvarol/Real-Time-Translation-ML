import pandas as pd

def split_data(filepath, num_parts):
    data = pd.read_csv(filepath, sep='\t', header=None, names=['input_text', 'target_text'])
    part_size = len(data) // num_parts
    parts = [data.iloc[i * part_size: (i + 1) * part_size] for i in range(num_parts)]
    if len(data) % num_parts != 0:
        parts.append(data.iloc[num_parts * part_size:])
    for idx, part in enumerate(parts):
        part.to_csv(f'processed_data_part{idx + 1}.csv', index=False)

if __name__ == "__main__":
    split_data('dataset.txt', 50)
