class UndergroundSystem:

    def __init__(self):
        self.checkin_ids = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_info = self.checkin_ids[id]
        time = t - checkin_info[1]
        route = (checkin_info[0], stationName)
        if self.routes.get(route) is None:
            self.routes[route] = (time, 1)
        else:
            self.routes[route] = (self.routes[route][0] + time, self.routes[route][1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routes[route][0] / self.routes[route][1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)