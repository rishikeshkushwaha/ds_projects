import pandas as pd
import matplotlib.pylab as plt #For data visualization
from numpy import *

filename = "slr02.xls"


def run():
    data = pd.read_excel(filename)
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    num_iterations = 1000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m,
                                                                              compute_error_for_all_points(
                                                                                  initial_b, initial_m, data))
    print "Running..."
    [b, m, error] = gradient_decent_runner(data, initial_b, initial_m, learning_rate, num_iterations)
    # print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m,
    #                                                                   compute_error_for_all_points(b, m, data))
    plot_error(error)
    plot_line(data, m, b)
    # data visualization
    # plt.figure(figsize=(8, 6))
    # plt.title('Chirps/sec vs temperature')
    # plt.xlabel('chirps/sec for the striped ground cricket')
    # plt.ylabel('temperature in degrees Fahrenheit')
    # plt.scatter(data['X'], data['Y'], c='red', alpha=0.3)
    # plt.show()


def plot_line(data, m, b):
    X = data['X']
    Y = data['Y']
    plt.plot(X, Y, 'bo')
    plt.plot(X, m*X + b)
    plt.title('Chirps/sec vs temperature')
    plt.xlabel('chirps/sec for the striped ground cricket')
    plt.ylabel('temperature in degrees Fahrenheit')
    plt.scatter(data['X'], data['Y'], c='red', alpha=0.3)
    plt.show()


def plot_error(error):
    num_iterations = range(len(error))
    plt.figure(figsize=(8, 6))
    plt.title('Error vs Num of iterations')
    plt.xlabel('No of iterations')
    plt.ylabel('Error')
    plt.plot(num_iterations, error)
    plt.show()


def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_decent_runner(data, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    error = []
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(data), learning_rate)

        print "After {0} iterations b = {1}, m = {2}, error = {3}".format(i, b, m,
                                                                      compute_error_for_all_points(b, m, data))
        error.append(compute_error_for_all_points(b, m, data))
        if i in range(20, num_iterations, 10):
            plt.plot(data['X'], m*data['X']+b)
    return [b, m, error]


def compute_error_for_all_points(b, m, data):
    total_error = 0
    for i in range(0, len(data)):
        x = data['X'][0]
        y = data['Y'][1]
        total_error += (y - (m*x + b)) ** 2
    return total_error/ float(len(data))


if __name__ == "__main__":
    run()

