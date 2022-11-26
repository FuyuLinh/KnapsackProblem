

def getBestInClass(length, num_class, weights, values, labels, keys):
    contained = [0, 0]
    class_uncomplete = []
    res = []
    for i in range(num_class):
        class_uncomplete.append(1)
    x = length - 1
    while x > 0:
        if len(res) != num_class:
            if class_uncomplete[labels[x] - 1] == 1:
                res.append(keys[x])
                contained[0] += weights[x]
                contained[1] += values[x]
                del weights[x]
                del values[x]
                del keys[x]
                class_uncomplete[labels[x] - 1] = 0
                del labels[x]
            x = x - 1
        else:
            break
    return [res,contained], length - num_class, [weights, values, keys]


def Sort(length, num_class, weight_list, value_list, label_list):
    def ratio(e):
        return e[1] / e[0]

    X = [[weight_list[x], value_list[x], label_list[x], x] for x in range(length)]
    Y = sorted(X, key=ratio)
    weights = [Y[x][0] for x in range(length)]
    values = [Y[x][1] for x in range(length)]
    labels = [Y[x][2] for x in range(length)]
    keys = [Y[x][3] for x in range(length)]
    return getBestInClass(length, num_class, weights, values, labels, keys)

