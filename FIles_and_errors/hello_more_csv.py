import csv

class Iris:
    def __init__(self, filename):
        raw_data = self.load_data(filename)
        self.headers = raw_data[0]
        self.data = raw_data[1:]

    def load_data(self, filename):
        with open(filename) as open_file:
            csv_reader = csv.reader(open_file)
            return list(csv_reader)

    def find_mean(self, list_of_data):
        column_averages = [["sepal_length"], ["sepal_width"], ["petal_length"], ["petal_width"]]
        for index in range(4):
            sum = 0
            for row in list_of_data:
                sum += float(row[index])
            mean = sum / len(list_of_data)
            column_averages[index].append(mean)
        return column_averages

iris = Iris("iris.csv")

print(iris.headers)
print(iris.data)

print(iris.find_mean(iris.data))


# Make a class that can produce means, or other statistics
