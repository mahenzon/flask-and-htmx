from dataclasses import dataclass


@dataclass
class Clicker:
    count: int = 0

    def inc_count(self):
        self.count += 1
        return self.count
