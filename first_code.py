def fun(length , arr): 
    i, j = 1 , 1
    p = [1 for i in range(length)]
    #print(p)
    #print(p)

    for i in range(length):
        p[i] = j
        j *= arr[i]
        # print('j is: ')
        # print(j)
        # print(p)

    j = 1

    for i in range(length-1 , -1 , -1):
        p[i] *= j
        j *= arr[i]
        # print('j || is: ')
        # print(p)
        # print(p[i])
        # print(j)

    print('i || is: ')
    for i in range(length):   
        print(p[i])

    return

a = [3,4,6]
l = len(a)
fun(l , a)

###########OUTPUT###########
[24,18,12]
