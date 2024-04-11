from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # progress bar
import time

NO_LINES = 1_000_000_000

def process_temperatures(csv_path):
    # using positive and negative infinity to compare
    minimums = defaultdict(lambda: float('inf'))
    maximums = defaultdict(lambda: float('-inf'))
    sums = defaultdict(float)
    measurements = Counter()

    with open(csv_path, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        # using tqdm directly in the iterator will show the completion percentage.
        for row in tqdm(_reader, total=NO_LINES, desc="Processing"):
            station_name, temperature = str(row[0]), float(row[1])
            measurements.update([station_name])
            minimums[station_name] = min(minimums[station_name], temperature)
            maximums[station_name] = max(maximums[station_name], temperature)
            sums[station_name] += temperature

    print("Data loaded. Calculating statistics...")

    # calculation, min, max and mean for each station
    results = {}
    for station, qtd_measurements in measurements.items():
        mean_temp = sums[station] / qtd_measurements
        results[station] = (minimums[station], mean_temp, maximums[station])

    print("Statistics calculated. Sorting...")
    # sorting by station_name
    sorted_results = dict(sorted(results.items()))

    # formating the results for display
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":
    csv_path = "data/measurements.txt"

    print("Starting file processing.")
    start_time = time.time() 

    results = process_temperatures(csv_path)

    end_time = time.time() 
    #for station, metrics in results.items():
    #    print(station, metrics, sep=': ')

    print(f"\nProcessing finished in {end_time - start_time:.2f} seconds.")