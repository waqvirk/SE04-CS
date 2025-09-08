### Time To Buy Tickets ###
def ttbt(tickets: list[int], k: int) -> int:
    time = 0      # total seconds passed
    queue = tickets.copy()     # copy so we can keep track and update

    while queue[k] > 0:   # loop until person k has bought all the tickets
        for i in range(len(queue)):
            if queue[i] > 0:
                queue[i] -= 1
                time += 1
                if i == k and queue [i] == 0:
                    return time


# Example 1
tickets = [2, 3, 2]
k = 2
print()
print("Example 1")
print("Queue (tickets each person wants):", tickets)
print(f"Person k = {k} index (wants {tickets[k]} tickets)")
print("Time needed for person k to finish:", ttbt(tickets, k), "seconds")
print("-" * 40)

# Example 2
tickets = [5, 1, 1, 1]
k = 0
print()
print("Example 2")
print("Queue (tickets each person wants):", tickets)
print(f"Person k = {k} index (wants {tickets[k]} tickets)")
print("Time needed for person k to finish:", ttbt(tickets, k), "seconds")
print()