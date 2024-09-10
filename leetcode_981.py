#LeetCode 981 - Time Based Key Value Store


class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if not self.storage.get(key):
            self.storage[key] = []
        self.storage[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:

        l, r = 0, len(self.storage.get(key, [])) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2
            values = self.storage[key][mid]

            if values[0] == timestamp:
                return values[1]
            elif values[0] > timestamp:
                r = mid - 1
            else:
                result = values[1]
                l = mid + 1

        return result
