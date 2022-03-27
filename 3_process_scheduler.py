import csv
from statistics import mean
processes = list(csv.reader(open('processes.csv')))
#print(processes)
import matplotlib.pyplot as plt 


global turnaround
turnaround = []

global x
x = []
  
## 4GHZ PROCESSORS
def processor_1_execute(process, arrival_time):
    cycles = process[1] # burst time cycles
    gigahertz = 4000000000 # hertz, so this many cycles per second 4gigahertz
    memory = 16000
    memory_instances = memory / float(process[2])
    completion_time = gigahertz / cycles # completion time of this process
    completion_time /= memory_instances
    turnaroundtime = arrival_time - completion_time
    if turnaroundtime < 0 :
        turnaroundtime = turnaroundtime * -1
    print('Turnaround for process ' + str(process[0]) + ' is :' + str(turnaroundtime) + 'ms')
    x.append(int(process[0]))

    turnaround.append(turnaroundtime)
## 2GHZ Processors
def processor_2_execute(process, arrival_time):
    cycles = process[1] # burst time cycles
    gigahertz = 2000000000 # hertz, so this many cycles per second 4gigahertz
    memory = 8000
    memory_instances = memory / float(process[2])
    completion_time = gigahertz / cycles # completion time of this process
    completion_time /= memory_instances
    turnaroundtime =  arrival_time - completion_time
    if turnaroundtime < 0 :
        turnaroundtime = turnaroundtime * -1
    print('Turnaround for process ' + str(process[0]) + ' is :' + str(turnaroundtime))
    x.append(int(process[0]))

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
    if int(process[1]) >= mean_bt:
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

plt.plot(x,turnaround)
plt.xlabel('Process IDs')
plt.ylabel('Turnaround Times')
plt.title('Problem 3')
print('Average Turnaround is: ' + str(mean_turnaround))
plt.show()
