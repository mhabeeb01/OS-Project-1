import csv
from statistics import mean
processes = list(csv.reader(open('processes.csv')))
#print(processes)

global turnaround
turnaround = []
  
## 4GHZ PROCESSORS
def processor_1_execute(process, arrival_time):
    cycles = process[1] # burst time cycles
    gigahertz = 4000000000 # hertz, so this many cycles per second 4gigahertz
    completion_time = gigahertz / cycles # completion time of this process
    turnaroundtime = arrival_time - completion_time
    if turnaroundtime < 0 :
        turnaroundtime = turnaroundtime * -1
    print('Turnaround for process ' + str(process[0]) + ' is :' + str(turnaroundtime) + 'ms')
    turnaround.append(turnaroundtime)
## 2GHZ Processors
def processor_2_execute(process, arrival_time):
    cycles = process[1] # burst time cycles
    gigahertz = 2000000000 # hertz, so this many cycles per second 4gigahertz
    completion_time = gigahertz / cycles # completion time of this process
    turnaroundtime =  arrival_time - completion_time
    if turnaroundtime < 0 :
        turnaroundtime = turnaroundtime * -1
    print('Turnaround for process ' + str(process[0]) + ' is :' + str(turnaroundtime))
    turnaround.append(turnaroundtime)

# Turnarounf time = Completion Time - Arrival Time
#Finding the mean Bursttime for the process
total = 0 
for process in processes:
    process[1] = int(process[1]) 
    total = total + process[1]



mean_bt = total / len(processes) 

print('Mean: '  + str(mean_bt) )
arrival_time_p1 = 0
arrival_time_p2 = 0
temp_p1 = 0 
temp_p2 = 0 

processor_1 = 3
processor_2 = 3
prcoessors_used = 0 
max_arr = [] 
for process in processes:

    '''
    if len(max_arr) == 6:
        get_turnaround(max_arr)
        max_arr = []
    '''
    if process[1] >= mean_bt:
        temp_p1 = temp_p1 + 1
        processor_1_execute(process, arrival_time_p1)
        
    else:
    
        temp_p2 = temp_p2 +1 
        processor_2_execute(process, arrival_time_p2)
    if temp_p2 == 3:
        temp_p2 = 0
        arrival_time_p2 = arrival_time_p2 + 1 

    if temp_p1 == 3:
        temp_p1 = 0
        arrival_time_p1 = arrival_time_p1 + 1 

mean_turnaround = mean(turnaround)

print('Average Turnaround is: ' + str(mean_turnaround))

