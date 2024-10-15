import math

from scipy.stats import alpha

from data_file import random_data

class OurSuperMotherFuckinggGeneratorToGenerateAbsolutelyRandomNumbers:
    def __init__(self, seed, a, m):
        self.state = seed
        self.a = a
        self.m = m

    def next(self):
        self.state = (self.a * self.state) % self.m
        return self.state / self.m


if __name__ == "__main__":
    seed = 1
    a = 1357
    m = 5689

    data = []

    generator = OurSuperMotherFuckinggGeneratorToGenerateAbsolutelyRandomNumbers(seed, a, m)
    for _ in range(301):
        # print(generator.next())
        data.append(round(- 68.62 * math.log(generator.next(), math.e), 2))

    for _ in range(301):
        data[_] += round(- 68.62 * math.log(generator.next(), math.e), 2)

    for _ in range(301):
        data[_] += round(- 68.62 * math.log(generator.next(), math.e), 2)
    for _ in range(301):
        print(f"{data[_]},")

    # print(len(data))