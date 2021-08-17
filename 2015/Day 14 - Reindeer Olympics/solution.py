import re

f = open("input.txt")
inp = f.read().split('\n')
f.close()


def get_raindeer(line):
    regex = re.compile(
        r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    results = re.findall(regex, line)
    return results[0][0], int(results[0][1]), int(results[0][2]), int(results[0][3])


def part_1(total_time=2503):
    def get_distance(speed, fly, rest, total):
        remaining = total
        flown = 0
        while remaining > 0:
            if remaining >= fly:
                flown += speed*fly
                remaining -= fly
            else:
                flown += speed*remaining
                remaining = 0
            if remaining >= rest:
                remaining -= rest
            else:
                remaining = 0
        return flown

    top = 0
    for raindeer in inp:
        name, speed, fly, rest = get_raindeer(raindeer)
        distance = get_distance(speed, fly, rest, total_time)
        if distance > top:
            top = distance
    return top


def part_2(total_time=2503):
    class Raindeer:
        def __init__(self, name, speed, fly_time, rest_time):
            self.__name = name
            self.__speed = int(speed)
            self.__fly_time = int(fly_time)
            self.__rest_time = int(rest_time)
            self.__pos = 0
            self.__is_resting = False
            self.__flying_time = 0
            self.__resting_time = 0
            self.__distance = 0
            self.__points = 0

        def move(self):
            if self.__is_resting:
                self.__resting_time += 1
                if self.__resting_time == self.__rest_time:
                    self.__resting_time = 0
                    self.__flying_time = 0
                    self.__is_resting = False
            else:
                self.__distance += self.__speed
                self.__flying_time += 1
                if self.__flying_time == self.__fly_time:
                    self.__is_resting = True

        def get_distance(self):
            return self.__distance

        def add_point(self):
            self.__points += 1

        def get_points(self):
            return self.__points

        def get_name(self):
            return self.__name

    raindeers = list()
    for line in inp:
        name, speed, fly_time, rest_time = get_raindeer(line)
        raindeers.append(Raindeer(name, speed, fly_time, rest_time))

    for x in range(2503):
        for r in raindeers:
            r.move()
        m = max([r.get_distance() for r in raindeers])
        for r in raindeers:
            if r.get_distance() == m:
                r.add_point()

    return max([r.get_points() for r in raindeers])


print(part_1())
print(part_2())
