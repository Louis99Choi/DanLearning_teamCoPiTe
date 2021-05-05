# 4-3 왕실의 나이트
xy = input()

def move(arg, xx, yy):
    arg[0] = chr(ord(arg[0]) + xx)
    arg[1] = int(arg[1])
    arg[1] = arg[1] + yy

    return arg[0] + str(arg[1])

p_xy = [move(list(xy), 2, 1), move(list(xy), 2, -1), move(list(xy), -2, 1), move(list(xy), -2, -1),
        move(list(xy), 1, 2), move(list(xy), 1, -2), move(list(xy), -1, 2), move(list(xy), -1, -2)]

result = 0
for i in range(8):
    tmp = list(p_xy[i])
    if 97 <= ord(tmp[0]) <= 104 and 49 <= ord(tmp[1]) <= 57:
        result += 1

print(result)
