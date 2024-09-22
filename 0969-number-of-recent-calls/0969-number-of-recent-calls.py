class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        requests = 1
        check = t - 3000
        for time in reversed(self.queue):
            if check <= time <= t:
                requests += 1
            else:
                break
        
        self.queue.append(t)
        return requests


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)