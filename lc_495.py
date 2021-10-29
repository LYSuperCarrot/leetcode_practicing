def findPoisonedDuration(timeSeries, duration):
        uncovered = 0
        end_time = 0
        for i in range(len(timeSeries)):
            timeSeries[i] = timeSeries[i] - 1
            if end_time < timeSeries[i]:
                uncovered = uncovered + timeSeries[i] - end_time
            end_time = timeSeries[i] + duration
        total_time = timeSeries[-1] + duration - uncovered
        return total_time

time = [1, 4]
duration_t = 2

findPoisonedDuration(time, duration_t)