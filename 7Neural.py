print("Dharmik Bosamia")
print("53013240021")
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y = [0, 0, 0, 1]

w1 = 0
w2 = 0
bias = 0

learning_rate = 0.1
epochs = 10


def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0


for epoch in range(epochs):

    for i in range(len(X)):

        
        total = X[i][0] * w1 + X[i][1] * w2 + bias

        
        prediction = step_function(total)

        
        error = y[i] - prediction

        
        w1 = w1 + learning_rate * error * X[i][0]
        w2 = w2 + learning_rate * error * X[i][1]
        bias = bias + learning_rate * error


# Testing
print("AND Gate Output:")

for inputs in X:

    total = inputs[0] * w1 + inputs[1] * w2 + bias
    output = step_function(total)

    print(inputs, "=>", output)