def fatorial(x, show=False):
    calculo = 1

    while x != 0:
        if show:
            if x != 1:
                print(f'{x}', end='x')
            else:
                print(f'{x}', end=' = ')

        calculo *= x
        x -= 1
    return calculo


print(fatorial(5, show=True))
