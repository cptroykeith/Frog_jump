def solution (X, Y, D):
    V = (Y - X) // D
    if X+V*D >= Y:
        return V
    else:
        return V+1
pass