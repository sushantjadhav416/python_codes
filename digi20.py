def King_george(num:int) -> int:
    x = [0,1,1]
    y = [0,1,2]
    for i in range(3,num+1):
        x += [y[i-1]]
        y += [x[i-1] + y[i-1]]
    result = x[num] + y[num]
    return result*result

n = King_george(int(input()))
print(n)
