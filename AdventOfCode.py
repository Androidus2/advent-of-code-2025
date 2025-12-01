class AdventOfCode:

    @staticmethod
    def __d1p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        f.close()

        position = 50
        zeroCnt = 0
        for line in lines:
            movement = int(line[1:])
            if line[0] == 'L':
                movement *= -1
            position = (position + movement) % 100
            if position == 0:
                zeroCnt += 1
        return zeroCnt

    @staticmethod
    def __d1p2(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        f.close()

        position = 50
        zeroCnt = 0
        for line in lines:
            movement = int(line[1:])
            if line[0] == 'L':
                movement *= -1
            position = position + movement

            if (position < 0 and position - movement > 0) or position == 0:
                zeroCnt += 1
            zeroCnt += abs(position) // 100

            position = position % 100
        return zeroCnt

    __table = {
        1: {
            1: __d1p1,
            2: __d1p2
        },
    }

    @staticmethod
    def Solve(day, part, fileName):
        """
        Solve the problem for the given day and part, while reading the input from the given file
        """
        try :
            print(f"Day {day} Part {part}: {AdventOfCode.__table[day][part](fileName)}")
        except KeyError:
            print("Day or part not found")

# Usage
AdventOfCode.Solve(1, 2, "Inputs/Day1/p1.txt")