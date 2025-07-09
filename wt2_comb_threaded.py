from itertools import combinations
from multiprocessing import Pool, cpu_count
import os, psutil, gc, time, threading
import datetime

current_time_str = ""
N = 0

def update_time_every_second():
    global current_time_str
    while True:
        current_time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)


def diffChecker(lst,n):
    result = [0] * (lst[-1] + 1)
    result[0] = n
    result[-1] = 1
    for i in range(1, lst[-1]):  # difference values
        dontCount = set()
        for j in lst:
            if (j + i) in lst and frozenset((j, j + i)) not in dontCount: #frozenset is used to ensure no repitition, i.e (i,j) == (j,i)
                result[i] += 1
                dontCount.add(frozenset((j, j + i)))
            elif (j - i) in lst and frozenset((j, j - i)) not in dontCount:
                result[i] += 1
                dontCount.add(frozenset((j, j - i)))
    return result


def constraint_check(arr, L, n):
    lst = diffChecker(arr,n)

    if 0 in lst[:-1] or 1 in lst[:-1]:
        return False

    for i in range(1,n):
        temp = arr.copy()
        del temp[i]
        if 0 in diffChecker(temp,n-1): 
            return False

    # print(f"{arr} is a solution for {L}\n")
    return arr
    
def process_combo(combo_info):
    combo, L, n = combo_info
    proto = [0, 1, 2] + list(combo) + [L - 1, L]
    return constraint_check(proto, L, n)

def tryAllCombinations_parallel(n, current_N):
    middle_values = list(range(3, current_N - 1))
    job_inputs = ((combo, current_N, n) for combo in combinations(middle_values, n - 5)) #lazy generation, instead of storing millions of combinations in a list

    with Pool(processes=cpu_count()) as pool: #creates new processes (NEW PYTHON INTERPRETERS) - more isolation, separate memory
        for result in pool.imap_unordered(process_combo, job_inputs, chunksize=100): #combinations calculated isolatedly. imap_unordered holds only 100 memory instead of themilllions of combinattions, reducing memory usage
            if result:
                print(f"{result} is a solution for {current_N}\n")
                return True
        #the processes are actice only in the 'with Pool' statement and die after it terminates
    return False


if __name__ == "__main__": #otherwise, child processes(called later) will also run this again
    n = int(input("Enter array size: "))
    N = n-1
    threading.Thread(target=update_time_every_second, daemon=True).start()
    # threading.Thread(target=print_memory_periodically, daemon=True).start() #will print time/memory every 1 hour
    print(current_time_str)
    while N < 100:
        found = tryAllCombinations_parallel(n, N)
        gc.collect()
        if found:
            print("success, checking for higher L, current time:", current_time_str)
        else:
            print(f"failure for {N}, still checking for higher L, current time:", current_time_str)
        
        N += 1    

