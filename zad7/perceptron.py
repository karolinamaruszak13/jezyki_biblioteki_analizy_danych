from jezyki_biblioteki_analizy_danych.zad7.loading_training_data import LoadCSV
import numpy as np


class Perceptron:
    def __init__(self, data):
        self.data = data
        self.x, self.y = data.getX(), data.get_label()
        self.y -= 0.5
        self.y = self.y * 2
        self.x_train, self.x_test = data.getX()[:int(data.getX().shape[0] * 0.6)], \
                                    data.getX()[int(data.getX().shape[0] * 0.6):]   # podział 60:40?
        self.y_train, self.y_test = data.get_label()[:int(data.get_label().shape[0] * 0.6)], \
                                    data.get_label()[int(data.get_label().shape[0] * 0.6):]
        self.y_test += 0.5  # o co tu chodzi?
        self.weights = np.zeros(data.getX().shape[1])
        self.bias = 0

    def train(self, max_iter=62):
        for epoch in range(max_iter):
            error = 0
            loss = 0
            for i in range(self.x_train.shape[0]):
                activation = self.weights @ self.x_train[i]
                if activation * self.y_train[i] <= 0:
                    self.weights += self.y_train[i] * self.x_train[i]
                    self.bias += self.y_train[i]
                    error += 1
                loss += max(0, 1 - activation * self.y_train[i])
            print(
                f"epoch={epoch + 1}, loss={loss / self.x_train.shape[0]}, accuracy={1 - error / self.x_train.shape[0]}")

    def predict(self, X, Y):    # to nie jest predict tylko test
        print(f"accuracy = {sum(list(map(lambda x: int(x), self.weights @ X.T + self.bias > 0)) == Y)/Y.shape[0]}")
        # return list(map(lambda x: int(x), self.weights @ X.T + self.bias > 0)) == Y


l = LoadCSV('sample1.csv')
for i in range(l.getX().shape[1]):
    l.column_centering(i+1)
# l.rows_normalization()
p = Perceptron(l)
p.train(max_iter=100)
# print(p.x_test)
# p.predict(np.array([[7,21,21,-9,56,-8,17,44]]), np.array([0]))
p.predict(p.x_test, p.y_test)
