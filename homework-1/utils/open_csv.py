import csv


def get_csv(path: str) -> list:

    data = []
    count = 0

    with open(path) as csv_file:
        file = csv.reader(csv_file, delimiter=',')

        for line in file:
            if count != 0:
                data.append(line)
            else:
                count += 1

    return data
