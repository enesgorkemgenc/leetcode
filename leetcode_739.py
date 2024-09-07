#LeetCode 739 - Daily Temperatures


def daily_temperatures(temperatures):

    result = [None] * len(temperatures)
    temps_stack = []

    for i, num in enumerate(temperatures):

        temps_stack.append(i)

        while True:
            if num > temperatures[temps_stack[len(temps_stack) - 2]]:
                popped_index = temps_stack.pop(len(temps_stack) - 2)
                result[popped_index] = i - popped_index
            else:
                break

    for j in temps_stack:
        result[j] = 0

    return result
