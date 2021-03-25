import csv
import math

import numpy as np

# Function replaces nan with approximate data
def replaceNan(fromPath, toPath):
    with open(fromPath) as file:
        lines = file.readlines()
        data = np.genfromtxt(lines, delimiter=",", skip_header=1)
        BMI = data[:, 4]

        # checking if data have Nan
        if np.isnan(BMI).any():
            mask = np.isnan(BMI)
            BMI = BMI[~mask]
            mean_BMI = np.mean(BMI)

            # approximate missing data
            for record in data:
                if np.isnan(record[4]):
                    record[4] = np.round(mean_BMI, 2)
                    record[3] = int(math.sqrt(10000*float(record[2]/mean_BMI)))

    with open(fromPath) as file:
        header = np.genfromtxt(file.readlines(), delimiter=",", encoding='utf8', dtype=str, skip_footer=len(data))

    with open(toPath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == '__main__':
    replaceNan("files/data_broken.csv", "new_files/data_not_broken")
