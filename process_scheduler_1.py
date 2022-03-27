import csv

processes = list(csv.reader(open('processes.csv')))

n = len(processes)
burst_time = []
ids = []
for process in processes:
    ids.append(int(process[0]))
    burst_time.append(int(process[1]))

# First In First Out (FIFO)
def FIFOWaitTime(n, burst, wait):
    wait[0] = 0
 
    for i in range(1, n):
        wait[i] = int(burst[i - 1] + wait[i - 1])
 
def FIFOTurnAroundTime(n, burst, wait, turnaround):
    for i in range(n):
        turnaround[i] = burst[i] + wait[i]
 
def FIFOavgTime(processes, n, burst):
    wait = [0] * n
    turnaround = [0] * n
    total_wait = 0
    total_turnaround = 0
 
    FIFOWaitTime(n, burst, wait)
    FIFOTurnAroundTime(n, burst, wait, turnaround)
 
    for i in range(n):
        total_wait += wait[i]
        total_turnaround += wait[i]
 
    print("FIFO: ")
    print("Average waiting time = " + str(total_wait / n))
    print("Average turn around time = " + str(total_turnaround / n))

FIFOavgTime(ids, n, burst_time)
print()

#Shortest Job First (SJF)
def SJFWaitTime(processes, n, wait):
    remaining = [0] * n
 
    for i in range(n):
        remaining[i] = int(processes[i][1])

    complete = 0
    t = 0
    max = 999999999
    temp = 0
    check = False
 
    while (complete != n):
         
        for j in range(n):
            if ((int(processes[j][2]) <= t) and
                (remaining[j] < max) and remaining[j] > 0):
                max = remaining[j]
                temp = j
                check = True
        if (check == False):
            t += 1
            continue
             
        remaining[temp] -= 1
 
        max = remaining[temp]
        if (max == 0):
            max = 999999999
 
        if (remaining[temp] == 0):
            complete += 1
            check = False
            finish = t + 1
            wait[temp] = (finish - int(processes[temp][1]) -   
                                int(processes[temp][2]))
 
            if (wait[temp] < 0):
                wait[temp] = 0
         
        t += 1
 
def SJFTurnAroundTime(processes, n, wait, turnaround):
     
    for i in range(n):
        turnaround[i] = int(processes[i][1]) + wait[i]
 
def SJFavgTime(processes, n):
    wait = [0] * n
    turnaround = [0] * n
 
    SJFWaitTime(processes, n, wait)
    SJFTurnAroundTime(processes, n, wait, turnaround)
 
    total_wait = 0
    total_turnaround = 0
    for i in range(n):
        total_wait += wait[i]
        total_turnaround += turnaround[i]
 
    print("SJF:")
    print("Average waiting time = %.5f "%(total_wait / n) )
    print("Average turn around time = ", total_turnaround / n)
    print()
     
SJFavgTime(processes, n)

#Round Robin (RR)
def RRWaitTime(n, burst, wait, quantum):
    rem_burst = [0] * n
 
    for i in range(n):
        rem_burst[i] = burst[i]
    t = 0 

    while(1):
        done = True
 
        for i in range(n):
            if (rem_burst[i] > 0) :
                done = False
                 
                if (rem_burst[i] > quantum) :
                    t += quantum
                    rem_burst[i] -= quantum

                else:
                    t = t + rem_burst[i]
                    wait[i] = t - burst[i]
 
                    rem_burst[i] = 0
                 
        if (done == True):
            break
             
def RRTurnAroundTime(n, burst, wait, turnaround):
     
    for i in range(n):
        turnaround[i] = burst[i] + wait[i]
 
def RRavgTime(n, burst, quantum):
    wait = [0] * n
    turnaround = [0] * n

    RRWaitTime(n, burst,
                         wait, quantum)

    RRTurnAroundTime(n, burst,
                                wait, turnaround)
 
    total_wait = 0
    total_turnaround = 0
    for i in range(n):
 
        total_wait = total_wait + wait[i]
        total_turnaround = total_turnaround + turnaround[i]
    
    print("RR:")
    print("Average waiting time = %.5f "%(total_wait / n) )
    print("Average turn around time = %.5f "% (total_turnaround / n))
      
quantum = 2
RRavgTime(n, burst_time, quantum)