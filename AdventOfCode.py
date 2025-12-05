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
    
    @staticmethod
    def __d4p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()

        neighs = [-1, 0, 1]
        
        n = len(lines)
        m = len(lines[0]) - 1
        ans = 0
        for i in range(n):
            line = lines[i]
            if i != n - 1:
                line = line[:-1]
            for j in range(m):
                cnt = 0
                for yOff in neighs:
                    for xOff in neighs:
                        if xOff == 0 and yOff == 0:
                            continue
                        x = j + xOff
                        y = i + yOff
                        if x >= 0 and x < m and y >= 0 and y < n and lines[y][x] == '@':
                            cnt += 1
                if cnt < 4 and lines[i][j] == '@':
                    ans += 1
        return ans
    
    @staticmethod
    def __d4p2(fileName):
        with open(fileName) as f:
            lines = f.readlines()

        neighs = [-1, 0, 1]
        
        n = len(lines)
        m = len(lines[0]) - 1
        ans = 0
        i = 0

        while i < n:
            line = lines[i].strip()
            lines[i] = [line[k] for k in range(m)]
            i += 1
        i = 0

        while i < n:
            j = 0
            while j < m:
                cnt = 0
                for yOff in neighs:
                    for xOff in neighs:
                        if xOff == 0 and yOff == 0:
                            continue
                        x = j + xOff
                        y = i + yOff
                        if x >= 0 and x < m and y >= 0 and y < n and lines[y][x] == '@':
                            cnt += 1
                if cnt < 4 and lines[i][j] == '@':
                    ans += 1
                    lines[i][j] = '.'
                    i = max(0, i - 1)
                    j = max(-1, j - 2)
                j += 1
            i += 1
        return ans
    
    def __d5p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        
        isReadingFreshRange = True

        ranges = []
        ans = 0

        for line in lines:
            if line.strip() == '':
                isReadingFreshRange = False
                continue
            if isReadingFreshRange:
                a, b = [int(x) for x in line.split('-')]
                ranges.append((a, b))
            else:
                a = int(line)
                for range in ranges:
                    if a >= range[0] and a <= range[1]:
                        ans += 1
                        break
        return ans
    
    def __d5p2(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        ranges = []
        ans = 0

        for line in lines:
            if line.strip() == '':
                break
            a, b = [int(x) for x in line.split('-')]
            ranges.append((a, b))
        
        ranges.sort(key=lambda x: (x[1], x[0]))
        mergedRanges = []
        for rng in ranges:
            mergedRanges.append(rng)
            while len(mergedRanges) > 1 and mergedRanges[-2][1] >= mergedRanges[-1][0]:
                mergedRanges[-2] = (min(mergedRanges[-2][0], mergedRanges[-1][0]), mergedRanges[-1][1])
                mergedRanges.pop()
        
        for rng in mergedRanges:
            ans += rng[1] - rng[0] + 1
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
        },
        4: {
            1: __d4p1,
            2: __d4p2
        },
        5: {
            1: __d5p1,
            2: __d5p2
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
AdventOfCode.Solve(5, 2, "Inputs/Day5/p5.txt")