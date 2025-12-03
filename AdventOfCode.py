from functools import cache

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
    
    @staticmethod
    def __d3p1(fileName):
        def getMaxDigitFromLine(line):
            if len(line) == 0:
                return (0, -1)
            maxx = int(line[0])
            maxi = 0
            for i in range(len(line)):
                ch = line[i]
                digit = int(ch)
                if digit > maxx:
                    maxx = digit
                    maxi = i
            return (maxx, maxi)

        with open(fileName) as f:
            lines = f.readlines()

        ans = 0
        
        for i in range(len(lines)):
            line = lines[i]
            if i != len(lines) - 1:
                line = line[:-1]
            
            maxx, maxi = getMaxDigitFromLine(line)
            if maxi == len(line) - 1:
                secondMaxx = maxx
                maxx, _ = getMaxDigitFromLine(line[:maxi])
            else:
                secondMaxx, _ = getMaxDigitFromLine(line[maxi + 1:])
            
            ans += maxx * 10 + secondMaxx
        return ans

    @staticmethod
    def __d3p2(fileName):
        @cache
        def solve(string, digitsToPick):
            if digitsToPick == 0:
                return 0
            if digitsToPick > len(string):
                return -1
            elif digitsToPick == len(string):
                return int(string)
            return max(int(string[0]) * pow(10, digitsToPick - 1) + solve(string[1:], digitsToPick-1), solve(string[1:], digitsToPick))

        with open(fileName) as f:
            lines = f.readlines()

        ans = 0
        
        for i in range(len(lines)):
            line = lines[i]
            if i != len(lines) - 1:
                line = line[:-1]
            
            ans += solve(line, 12)
        return ans

    __table = {
        1: {
            1: __d1p1,
            2: __d1p2
        },
        2:{
            1: __d2p1,
            2: __d2p2
        },
        3: {
            1: __d3p1,
            2: __d3p2
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
AdventOfCode.Solve(3, 2, "Inputs/Day3/p3.txt")