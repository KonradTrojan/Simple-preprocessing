import numpy as np
import csv


# function, which repairs data in selected column and counts new BMI
#
def repairData(fromPath, toPath, fromRow, toRow, column, correction):

    with open(fromPath) as file:
        data = np.genfromtxt(file.readlines(), delimiter=",", skip_header=1)

        # data repairing
        data[fromRow:toRow, column] += correction

        # counting new BMI
        data[fromRow:toRow, 4] = data[fromRow:toRow, 2] / (data[fromRow:toRow, 3] * data[fromRow:toRow, 3] / 10000)
        data[fromRow:toRow, 4] = np.round(data[fromRow:toRow, 4], 2)

    with open(fromPath) as file:
        header = np.genfromtxt(file.readlines(), delimiter=",", encoding='utf8', dtype=str, skip_footer=len(data))

    with open(toPath, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


if __name__ == '__main__':
    repairData("files/data.csv", "new_files/new_BMI_data.csv", 0, 11, 2, -5)














