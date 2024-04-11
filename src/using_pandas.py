import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm  # progress bar

CONCURRENCY = cpu_count()

number_of_lines = 1_000_000_000  # known number of lines
chunksize = 100_000_000  # chunk size
filename = "data/measurements.txt"  

def process_chunk(chunk):
    # Agregate the data of each chunk using pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

def create_df_with_pandas(filename, number_of_lines, chunksize=chunksize):
    total_chunks = number_of_lines // chunksize + (1 if number_of_lines % chunksize else 0)
    results = []

    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:
        # enclosing the iterator with tqdm to show the progress
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processing"):
                # process each chunk in parallel
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time

    print("Starting the file processing.")
    start_time = time.time()
    df = create_df_with_pandas(filename, number_of_lines, chunksize)
    took = time.time() - start_time

    print(df.head())
    print(f"Processing took: {took:.2f} sec")
