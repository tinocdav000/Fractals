# David Tinoco Morales
# 30 October
# Dragon curve turn generator

# For the dragon curves, each True symbolizes a right turn and each 0 symbolizes a left turn
# Each iteration is the previous iteration followed by a right turn, followed by the reversed inverse of
def dragon(iteration):
    # p is the previous iteration and q will be its reverse inverse
    p = iteration
    q = []

    # Generate the inverse of P
    for i in p:
        if i == 1:
            q.append(0)
        elif i == 0:
            q.append(1)

    # Reverse the inverse of p
    leng = len(q)
    n = []
    for i in range(1, leng + 1):
        n.append(q[-i])
    q = n

    # produce the next iteration from parts
    next = p
    next.append(1)
    next = next + q

    # return the next iteration
    return next


def iterChoose(iteration):
    # n is the desired iteration and f is the first iteration
    n = iteration - 1
    f = [1]

    # The previous function will be used to generate the desired iteration's instructions
    for i in range(n):
        t = dragon(f)
        f = t
    # Return the iteration's instructions
    it = f
    return it


def dragon2(iteration):
    # p is the previous iteration and q will be its reverse inverse
    p = iteration
    q = []

    # Generate the inverse of P
    for i in p:
        if i == 1:
            q.append(0)
        elif i == 0:
            q.append(1)

    # Reverse the inverse of p
    leng = len(q)
    n = []
    for i in range(1, leng + 1):
        n.append(q[-i])
    q = n

    # produce the next iteration from parts
    next = p
    next.append(0)
    next = next + q

    # return the next iteration
    return next


def iterChoose2(iteration):
    # n is the desired iteration and f is the first iteration
    n = iteration - 1
    f = [1]

    # The previous function will be used to generate the desired iteration's instructions
    for i in range(n):
        t = dragon2(f)
        f = t
    # Return the iteration's instructions
    it = f
    return it

    # Generate the inverse of P
    for i in p:
        if i == 1:
            q.append(0)
        elif i == 0:
            q.append(1)

    # Reverse the inverse of p
    leng = len(q)
    n = []
    for i in range(1, leng + 1):
        n.append(q[-i])
    q = n

    # produce the next iteration from parts
    next = p
    next.append(1)
    next = next + q

    # return the next iteration
    return next


def iterChoose(iteration):
    # n is the desired iteration and f is the first iteration
    n = iteration
    f = [1]

    # The previous function will be used to generate the desired iteration's instructions
    for i in range(n):
        t = dragon(f)
        f = t
    # Return the iteration's instructions
    it = f
    return it
