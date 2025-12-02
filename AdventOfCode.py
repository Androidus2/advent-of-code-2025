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
    
    @staticmethod
    def __d2p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        f.close()

        line = lines[0]
        ans = 0

        for interval in line.split(','):
            left, right = [int(x) for x in interval.split('-')]
            for i in range(left, right + 1):
                strNum = str(i)
                n = len(strNum) // 2
                if strNum[:n] == strNum[n:]:
                    ans += i
        return ans
    
    @staticmethod
    def __d2p2(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        f.close()

        line = lines[0]
        ans = 0

        for interval in line.split(','):
            left, right = [int(x) for x in interval.split('-')]
            for i in range(left, right + 1):
                strNum = str(i)
                ok = True
                for n in range(1, len(strNum)):
                    if strNum[:n] * (len(strNum) // n) == strNum:
                        ok = False
                        break
                if not ok:
                    ans += i
        return ans

    __table = {
        1: {
            1: __d1p1,
            2: __d1p2
        },
        2:{
            1: __d2p1,
            2: __d2p2
        }
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
AdventOfCode.Solve(2, 2, "Inputs/Day2/p2.txt")