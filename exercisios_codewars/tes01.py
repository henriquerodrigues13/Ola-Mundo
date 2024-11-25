class User:
    def __init__(self, rank=-8, progress=0):
        self.rank = rank
        self.progress = progress

    def inc_progress(self, inc_progress):
        if inc_progress > 8 or inc_progress < -8 or inc_progress == 0:
            raise Exception
        if self.rank < 0 < inc_progress:
            inc_progress -= 1
        if self.rank == inc_progress:
            self.progress += 3
        elif (inc_progress - self.rank) == -1:
            self.progress += 1
        elif (inc_progress - self.rank) >= 1:
            self.progress += 10 * (inc_progress - self.rank) * (inc_progress - self.rank)
        while self.progress >= 100:
            if self.rank == 8:
                self.progress = 0
                break
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1