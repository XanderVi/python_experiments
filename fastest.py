#script for finding fastest "something": runner, horse, car, etc.
#inputs: time in format hh:mm:ss
#output: fastest time in format hh:mm:ss

times = []
arr = []
n = int(input())
for i in range(n):
    times.append([])
    t = input()
    t = t.split(":")
    times[i] = t

for i in range(n):
    arr.append(int(times[i][0])*3600 + int(times[i][1])*60 + int(times[i][2]))

i_min = arr.index(min(arr))
print(":".join(times[i_min]))
