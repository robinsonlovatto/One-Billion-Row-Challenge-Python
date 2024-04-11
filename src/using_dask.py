import dask
import dask.dataframe as dd

def create_dask_df():
    dask.config.set({'dataframe.query-planning': True})
    # Configuring Dask DataFrame to read CSV file
    # Since the file has no header, we specify the column names manually
    df = dd.read_csv("data/measurements.txt", sep=";", header=None, names=["station", "measure"])
    
    # Grouping by 'station' and calculating the maximum, minimum and average of 'measure'
    # Dask performs operations in a lazy way, so this part just defines the calculation
    grouped_df = df.groupby("station")['measure'].agg(['max', 'min', 'mean']).reset_index()

    return grouped_df

if __name__ == "__main__":
    import time

    start_time = time.time()
    df = create_dask_df()
    
    # calculation and sorting
    result_df = df.compute().sort_values("station")
    took = time.time() - start_time

    print(result_df)
    print(f"Dask Took: {took:.2f} sec")
