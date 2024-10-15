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

    generator = OurSuperMotherFuckinggGeneratorToGenerateAbsolutelyRandomNumbers(seed, a, m)
    for _ in range(10):
        print(generator.next())
