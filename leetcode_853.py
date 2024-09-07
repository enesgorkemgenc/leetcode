#LeetCode 853 - Car Fleet


def car_fleet(target, position, speed):

    cars = []
    num_fleets = 1

    for i in range(len(position)):
        cars.append({
            'position': position[i],
            'speed': speed[i],
            'time_needed': (target - position[i]) / speed[i]
            })

    cars = sorted(cars, key=lambda car: car['position'])

    j = len(cars) - 2

    while j >= 0:
        car = cars[j]
        next_car = cars[j + 1]

        if next_car['time_needed'] < car['time_needed']:
            num_fleets += 1
        else:
            car['time_needed'] = next_car['time_needed']

        j -= 1

    return num_fleets
