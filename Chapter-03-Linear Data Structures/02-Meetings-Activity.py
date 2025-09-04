### Meetings ###
def can_attend_meeting(intervals):
    if not intervals:        # check if list is empty
        return True
    
    intervals.sort(key=lambda x: x[0])        # sort intervals by start time

    for i in range(1, len(intervals)):    # check for overlaps
        previous = intervals[i - 1]
        current = intervals[i]
        if current[0] < previous[1]:     #overlap
            return False   # overlap found

    return True        # if no overlaps

# Example 1
intervals = [[0,30], [5,10], [15,20]]
print()
print("Meeting Intervals:", intervals)
print("Can the meetings be attended?:", can_attend_meeting(intervals))
print()



# Example 2
intervals = [[7,10], [2,4]]

print()
print("Meeting Intervals:", intervals)
print("Can the meetings be attended?:", can_attend_meeting(intervals))
print()

