import time
import pyximport; pyximport.install()
import coinchange

# import math

def main():
    # st = input('Enter a number: ')
    # arr = st.split(' ')
    # arr = list(map(lambda x: int(x), arr))

    arr = [
        # [5],
        # [6,2,5],
        # [6,1,6],
        # [8,3],
        # [8,2,5],
        # [20,10,15],
        # [100,5,10],
        # [100,8,25],
        # [300,12],
        [300,10,15]
        ]
    for a in arr:
        coins = coinchange.generatePrimeList(a[0])
        num = a[0]
        lr =0
        hr = 0
        if len(a)==1:
            lr = 1
            hr = num 
        elif len(a)==2:
            lr = a[1]
            hr = a[1]
        else:
            lr = a[1]
            hr = a[2]

        start = time.time()
        result = coinchange.findCombiR(a[0],coins,0,0,lr,hr)
        end = time.time() - start
        for i in a:
            print(i,end=' ')
        print()
        print('Result is ' +str(result),end='\t')
        print('{:.10f}'.format(end))

 
if __name__ == '__main__':
    main()