import csv
import math

class Iris:
    def __init__(self, filename):
        raw_data = self.load_data(filename)
        self.headers = raw_data[0]
        self.data = raw_data[1:]

    def load_data(self, filename):
        with open(filename) as open_file:
            csv_reader = csv.reader(open_file)
            return list(csv_reader)

    def find_mean(self, headers, list_of_data):
        average_list = [[headers[0]], [headers[1]], [headers[2]],
                        [headers[3]]]
        for index in range(4):
            sum = 0
            for row in list_of_data:
                sum += float(row[index])
            mean = sum / len(list_of_data)
            average_list[index].append(mean)
        return average_list

    def list_of_column_values(self, list_of_data):
        list_of_common_values = []
        for index in range(4):
            list_of_index_column_values = []
            for row in list_of_data:
                list_of_index_column_values.append(float(row[index]))
            list_of_common_values.append(list_of_index_column_values)
        return list_of_common_values

    def mean_list(self, list_of_data):
        mean_list = []
        for i in range(len(list_of_data)):
            sum = 0
            for num in list_of_data[i]:
                sum += num
            mean = sum / len(list_of_data[i])
            mean_list.append(mean)
        return mean_list

    def stdev(self, mean_list, list_of_values):
        stdev_list = []
        for i in range(len(list_of_values)):
            stdev_sum = 0
            for num in list_of_values[i]:
                stdev_sum += (num - mean_list[i]) ** 2
            stdev = (stdev_sum / len(list_of_values[i])) ** 0.5
            stdev_list.append(stdev)
        return stdev_list


#     for value in list_of_column_values:
#         x_minus_mean_squared_sum += (value - mean) ** 2
#         stdev = math.sqrt(x_minus_mean_squared_sum / len(list_of_data))
#         stdev_list.append(stdev)
#     # average_list[index].append(mean)
# return stdev_list

    def data_to_new_file(self, average_list, filename):
        with open(filename, "w", newline='\n') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(average_list)

iris = Iris("iris.csv")

print(iris.headers)
print(iris.data)
print(iris.list_of_column_values(iris.data))
print(iris.find_mean(iris.headers, iris.data))
print(iris.mean_list(iris.list_of_column_values(iris.data)))
iris.data_to_new_file(iris.find_mean(iris.headers, iris.data), "class_iris_averages")
print(iris.stdev(iris.mean_list(iris.list_of_column_values(iris.data)), iris.list_of_column_values(iris.data)))

# Make a class that can produce means, or other statistics

list_in_list = [[1,2], [3,4]]
print(sum(iris.list_of_column_values(iris.data)[1]))
