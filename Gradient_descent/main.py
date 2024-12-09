import numpy as np

def gradient_descent(x, y):
    m_curr =  b_curr = 0
    learning_rate = 0.01

    iteration = 3000
    n = len(x)

    for i in range (iteration):
        y_predict = m_curr * x + b_curr
        cost = (1/n) * sum([val ** 2 for val in (y - y_predict)])
        print("iteration {}  m {} b{} cost{}".format(i, m_curr, b_curr, cost))
        dm = -(2/n) * sum(x * (y - y_predict))
        db = -(2/n) * sum((y - y_predict))
        m_curr = m_curr - learning_rate * dm
        b_curr = b_curr - learning_rate * db



x = np.array((1, 2,3, 4, 5))
y = np.array((5, 7, 9, 11, 13))

gradient_descent(x, y)