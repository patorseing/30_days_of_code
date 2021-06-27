class Difference:
    def __init__(self, a):
        self.__elements = a
        # Add your code here
        self.maximumDifference = 0
    def computeDifference(self):
        l = len(self.__elements)
        for i in range(0, l):
            for j in range(i + 1, l):
                difference = abs(self.__elements[i] - self.__elements[j])
                self.maximumDifference = max(
                    difference, self.maximumDifference)


# End of Difference class
if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
