##def regressiva(i):
##        print(i)
##        regressiva(i - 1)  
##regressiva(5)


def regressiva(i):
    print (i)
    if i <= 1:
        return
    else:
        regressiva(i-1)
regressiva(10)