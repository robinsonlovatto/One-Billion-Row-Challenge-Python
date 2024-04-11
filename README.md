# One Billion Rows: Data Processing Challenge with Python

## Introduction

The objective of this project is to demonstrate how to efficiently process a massive data file containing 1 billion rows (~15GB), specifically to calculate statistics (Including aggregation and sorting which are heavy operations) using Python.

This challenge was inspired by [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originally proposed for Java.

The data file consists of temperature measurements from several weather stations. Each record follows the format `<string: station name>;<double: measurement>`, with the temperature being presented with precision to one decimal place.

Here are ten example lines from the file:

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0
```

The challenge is to develop a Python program capable of reading this file and calculating the minimum, average (rounded to one decimal place) and maximum temperature for each station, displaying the results in a table ordered by station name.

| station      | min_temperature | mean_temperature | max_temperature |
|--------------|-----------------|------------------|-----------------|
| Abha         | -31.1           | 18.0             | 66.5            |
| Abidjan      | -25.9           | 26.0             | 74.6            |
| Abéché       | -19.8           | 29.4             | 79.9            |
| Accra        | -24.8           | 26.4             | 76.3            |
| Addis Ababa  | -31.8           | 16.0             | 63.9            |
| Adelaide     | -31.8           | 17.3             | 71.5            |
| Aden         | -19.6           | 29.1             | 78.3            |
| Ahvaz        | -24.0           | 25.4             | 72.6            |
| Albuquerque  | -35.0           | 14.0             | 61.9            |
| Alexandra    | -40.1           | 11.0             | 67.9            |
| ...          | ...             | ...              | ...             |
| Yangon       | -23.6           | 27.5             | 77.3            |
| Yaoundé      | -26.2           | 23.8             | 73.4            |
| Yellowknife  | -53.4           | -4.3             | 46.7            |
| Yerevan      | -38.6           | 12.4             | 62.8            |
| Yinchuan     | -45.2           | 9.0              | 56.9            |
| Zagreb       | -39.2           | 10.7             | 58.1            |
| Zanzibar City| -26.5           | 26.0             | 75.2            |
| Zürich       | -42.0           | 9.3              | 63.6            |
| Ürümqi       | -42.1           | 7.4              | 56.7            |
| İzmir        | -34.4           | 17.9             | 67.9            |


## Results

The tests were carried out on a laptop equipped with a processor 12th Gen Intel(R) Core(TM) i7-1270P 2.20 GHz and 32GB of RAM. The implementations used purely Python, Pandas, Dask, Polars and DuckDB approaches. The runtime results for processing the 1 billion lines file are presented below. I added some tests with files of different sizes to check if the time would be linear and if there would be differences between the libraries. The times in the table below are the average of 3 executions.

| Implementation / Files | 1B (~15GB) | 100M (~1.5GB) | 10M (~160MB) | 1M (~16MB) | 100K (~1.6MB) | 10K (~160KB)
| --- | --- | --- | --- | --- | --- | --- | 
| Python | 40 min | 181.78 sec | 16.25 sec | 1.45 sec | 0.2 sec | 0.06 sec | 
| Python + Pandas | 458.73 sec | 61.21 sec | 6.84 sec | 2.66 sec | 2.5 sec | 2.36 sec | 
| Python + Dask | 297.96 sec | 27.79 sec | 3.01 sec | 0.68 sec | 0.34 sec | 0.36 sec |
| Python + Polars | 33.1 sec | 3.67 sec | 0.7 sec | 0.21 sec | 0.12 sec | 0.1 sec |
| Python + Duckdb | 25.6 sec | 2.71 sec | 0.27 sec | 0.08 sec | 0.02 sec | 0.02 sec | 

Thank you [Koen Vossen](https://github.com/koenvo) for the Polars implementation.

Thank you [Luciano Filho](https://github.com/lvgalvao) for the other implementations.

## Conclusion

This challenge clearly highlighted the effectiveness of several Python libraries in handling large volumes of data. Pure Python and Pandas required a series of tactics to implement "batch" processing, while libraries like Dask, Polars and DuckDB have proven to be exceptionally effective, requiring fewer lines of code due to its inherent ability to distribute data into "streaming batches" more efficiently. DuckDB stood out, achieving the shortest execution time thanks to its execution and data processing strategy. Polars came close.

Worth highlighting that as bigger the file is closer Polars came to DuckDB, from 5 times (10K file) slower to just 1.3 times slower in the 1B file.

It is also interesting that Python is a good approach in simple transformations in files under 1M lines, it have interesting performance and avoids problems with bandwith, deploy, compatibility, etc by installing other libraries.

These results emphasize the importance of selecting the right tool for large-scale data analysis, demonstrating that Python, with the right libraries, is a powerful choice for tackling big data challenges.


## How to execute

Para executar este projeto e reproduzir os resultados:

To run this project and reproduce the results:

1. Clone this repository.
2. Set the Python version using `pyenv local 3.12.1`.
3. `poetry env use 3.12.1`, `poetry install --no-root` and `poetry lock --no-update`.
4. Run the `python src/create_measurements.py` command to generate the test file (the 1B lines file). This will take a while.
5. Run the scripts `python src/using_python.py`, `python src/using_pandas.py`, `python src/using_dask.py`, `python src/using_polars.py` and `python src/using_duckdb.py` through a terminal or development environment that supports Python.

