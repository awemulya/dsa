def get_fibonancci(n):
    if n <= 1 :
        return (n,0)
    else:
        (a,b) = get_fibonancci(n-1)
        return (a+b, a)


def bad_fibo(n):
   if n <= 1:
       return n
   else:
       return(bad_fibo(n-1) + bad_fibo(n-2))


def default_fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


if __name__ == '__main__':
    import time
    start_get_fibonancci_time = time.time()
    for j in range(10):
        print(get_fibonancci(j))
    print("--- %s seconds ---" % (time.time() - start_get_fibonancci_time))

    # start_bad_fibo_time = time.time()
    # for k in range(10):
    #     print (bad_fibo(k))
    # print("--- %s seconds ---" % (time.time() - start_bad_fibo_time))
    #
    # start_default_fibo_time = time.time()
    # default_fibo(10)
    # print("--- %s seconds ---" % (time.time() - start_default_fibo_time))


