import csv
# scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     headers = list(map(str.lstrip, next(csvreader))) # Moves us one along in an iterable
#     for row in csvreader:
#         scores.append(int(row[-1]))
# print(headers)
# print(scores)
#
# # Scores stored as strings
# # Get rid of the header
#
# # with open("some_data.csv") as csvfile:
# #     csvreader = csv.reader(csvfile)
# #     print(list(csvreader)) # List of list
#
# data_to_write = [["David", 5], ["Paula", 6], ["Nish", 7]]
#
# with open ("new_data.csv", "w", newline='\n') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     # for row in data_to_write:
#     #     csv_writer.writerow(row)
#     csv_writer.writerows(data_to_write)


# Write a fucntion that will read in the iris dataset
# Write a function that will return the mean for each column
    # csv as a list
    # for each row, add the first column value to a list as a float
    # implement counter to count next row

# Write a function that will write the means to a new csv file
def read_dataset(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Moves us one along in an iterable
        # print(headers)
        return list(csvreader)


def return_mean(list_of_data):
    column_averages = [["sepal_length"], ["sepal_width"], ["petal_length"], ["petal_width"]]
    for index in range(4):
        sum = 0
        for row in list_of_data:
            sum += float(row[index])
        mean = sum / len(list_of_data)
        column_averages[index].append(mean)
    return column_averages



def mean_to_new_file(list_of_data, averages):
    average_list = [[list_of_data[0], averages[0]], [list_of_data[1], averages[1]], [list_of_data[2], averages[2]],
                    [list_of_data[3], averages[3]]]
    with open ("iris_averages", "w", newline='\n') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(average_list)


print(read_dataset("iris.csv"))
print(return_mean(read_dataset("iris.csv")))
mean_to_new_file(["sepal_length", "sepal_width", "petal_length", "petal_width"], return_mean(read_dataset("iris.csv")))


