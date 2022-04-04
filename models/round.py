class Round:
    def __init__(self, number, start_time=0, end_time=0):
        self.number = number
        self.matchs = []
        self.star_time = start_time
        self.end_time = end_time

    def add_match(self, match):
        self.matchs.append(match)

    def serializer(self):
        data = {
            "number": self.number,
            "matchs": [match.serializer() for match in self.matchs],
            "start_time": str(self.star_time),
            "end_time": str(self.end_time),
        }
        return data
