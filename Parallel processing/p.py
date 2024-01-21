import multiprocessing
import sys
from datetime import datetime
import functools

def test_func(manager_list, maxNo, id = 0, CPU = 1):
    l = []
    for i in range(int(id*(maxNo/CPU)) , int((id+1) * (maxNo/CPU)) ):
      if i % 9999 == 0:
        l.append(f'{i}')
    if len(l) > 0:
      manager_list.append(l) #### this is impt... but may need to flush occasionally
    return manager_list

def uni(maxNo):
    if __name__ == '__main__':
        print('Running... Uni')
        manager_list = []
        newList = test_func(manager_list, int(maxNo), id = 0 , CPU = 1)

        return newList[0]

def multi(maxNo, CPU = 1):
    if __name__ == '__main__':
        print('Running... Multi')
        manager_list = multiprocessing.Manager().list()
        processes= []
        
        for id in range(CPU):
            # print(f'{id=}')
            p = multiprocessing.Process(target=test_func, args=(manager_list, int(maxNo), id,  CPU))
            p.start()
            processes.append(p)
        
        # print('joining...')
        ended = False

        while not ended:
            ended=True
            for p in processes:
                # print(f'{p=}')
                p.join(15)  # check every 15 sec
                if (p.is_alive()):
                  ended = False
                # print(f'{p=} {p.is_alive()=}')

        # res = list(manager_list)
        # res1 = []
        # for i in res:
        #     res1 += i
        return manager_list

# main()
if __name__ == '__main__':  ### apparently, if you have this, it won't run in the parallet CPU 
    print()
    start_time = datetime.now()
    print(f'* Start = {start_time}')

    if (sys.argv[1] == 'u'):
        res = uni(sys.argv[2])
        end_time = datetime.now()
        
        res1 = sorted(res)
    else:
        res = multi(int(sys.argv[2]),int(sys.argv[3]))
        end_time = datetime.now()
        res = list(res)
        res1 = []
        for i in res:
            res1 += i
        res1 = sorted(res1)

    print(f'* End   = {end_time}')
    time_difference = end_time - start_time
    print(f'\n{time_difference = }')

    print(f'\n{len(res1) = }')
    print(f'{res1 = }')
    