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
    
    @staticmethod
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
    
    @staticmethod
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
    
    @staticmethod
    def __d6p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        
        numbers = []
        operators = []
        n = len(lines)

        for i in range(n):
            line = lines[i]
            if i == n - 1:
                operators = line.split()
                break
            lineNumbers = [int(x) for x in line.split()]
            numbers.append(lineNumbers)
        
        m = len(numbers[0])
        ans = 0

        for j in range(m):
            res = numbers[0][j]
            for i in range(1, n - 1):
                if operators[j] == '+':
                    res += numbers[i][j]
                else:
                    res *= numbers[i][j]
            ans += res
        return ans

    @staticmethod
    def __d6p2(fileName):
        def isColumnOfSpaces(lines, column, n):
            for i in range(n):
                if lines[i][column] != ' ':
                    return False
            return True
        
        def calculateColumnNumber(lines, column, n):
            number = 0
            for i in range(n - 1):
                if lines[i][column] != ' ':
                    number = number * 10 + int(lines[i][column])
            return number

        with open(fileName) as f:
            lines = f.readlines()
        operators = lines[-1].split()
        n = len(lines)
        m = len(operators)
        numberEndPositions = [-1]
        ans = 0

        for i in range(n - 1):
            lines[i] = lines[i][:-1]

        for j in range(len(lines[0])):
            if isColumnOfSpaces(lines, j, n):
                numberEndPositions.append(j)
        numberEndPositions.append(len(lines[0]))

        for j in range(m):
            res = 0
            if operators[j] == '*':
                res = 1
            for k in range(numberEndPositions[j] + 1, numberEndPositions[j + 1]):
                columnNumber = calculateColumnNumber(lines, k, n)
                if operators[j] == '+':
                    res += columnNumber
                else:
                    res *= columnNumber
            ans += res
        return ans
    
    @staticmethod
    def __d7p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()

        n = len(lines)
        m = len(lines[0]) - 1
        ans = 0
        beams = [False] * m
        for j in range(m):
            if lines[0][j] == 'S':
                beams[j] = True
        
        for i in range(1, n):
            for j in range(m):
                if lines[i][j] == '^' and beams[j]:
                    ans += 1
                    beams[j] = False
                    if j > 0:
                        beams[j - 1] = True
                    if j < m - 1:
                        beams[j + 1] = True

        return ans
    
    @staticmethod
    def __d7p2(fileName):
        with open(fileName) as f:
            lines = f.readlines()

        n = len(lines)
        m = len(lines[0]) - 1
        beams = [0] * m
        for j in range(m):
            if lines[0][j] == 'S':
                beams[j] = 1
        
        for i in range(1, n):
            for j in range(m):
                if lines[i][j] == '^' and beams[j] > 0:
                    if j > 0:
                        beams[j - 1] += beams[j]
                    if j < m - 1:
                        beams[j + 1] += beams[j]
                    beams[j] = 0

        return sum(beams)
    
    @staticmethod
    def __d8p1(fileName):
        import math
        with open(fileName) as f:
            lines = f.readlines()

        points = []
        for line in lines:
            point = [int(x) for x in line.split(',')]
            points.append(point)

        circuits = [-1] * len(points)
        circuitCnt = 0
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = math.sqrt(pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2) + pow(points[i][2] - points[j][2], 2))
                distances.append((dist, i, j))
        
        distances.sort()

        maxConnections = 1000
        for entryInd in range(maxConnections):
            entry = distances[entryInd]
            dist, i, j = entry

            if circuits[i] == -1 and circuits[j] == -1:
                circuits[i] = circuitCnt
                circuits[j] = circuitCnt
                circuitCnt += 1
            elif circuits[j] == -1:
                circuits[j] = circuits[i]
            elif circuits[i] == -1:
                circuits[i] = circuits[j]
            elif circuits[i] != circuits[j]:
                for k in range(len(circuits)):
                    if k != j and circuits[k] == circuits[j]:
                        circuits[k] = circuits[i]
                circuits[j] = circuits[i]
        
        circuitLengths = [0] * len(circuits)
        for circuit in circuits:
            if circuit != -1:
                circuitLengths[circuit] += 1
        
        circuitLengths.sort(reverse=True)
        return circuitLengths[0] * circuitLengths[1] * circuitLengths[2]



    @staticmethod
    def __d8p2(fileName):
        import math
        with open(fileName) as f:
            lines = f.readlines()

        points = []
        for line in lines:
            point = [int(x) for x in line.split(',')]
            points.append(point)

        circuits = [-1] * len(points)
        circuitCnt = 0
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = math.sqrt(pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2) + pow(points[i][2] - points[j][2], 2))
                distances.append((dist, i, j))
        
        distances.sort()
        last = tuple()

        for entryInd in range(len(distances)):
            entry = distances[entryInd]
            dist, i, j = entry

            if circuits[i] == -1 and circuits[j] == -1:
                circuits[i] = circuitCnt
                circuits[j] = circuitCnt
                circuitCnt += 1
                last = (i, j)
            elif circuits[j] == -1:
                circuits[j] = circuits[i]
                last = (i, j)
            elif circuits[i] == -1:
                circuits[i] = circuits[j]
                last = (i, j)
            elif circuits[i] != circuits[j]:
                for k in range(len(circuits)):
                    if k != j and circuits[k] == circuits[j]:
                        circuits[k] = circuits[i]
                circuits[j] = circuits[i]
                last = (i, j)
        
        return points[last[0]][0] * points[last[1]][0]

    def __d9p1(fileName):
        with open(fileName) as f:
            lines = f.readlines()
        points = []
        for line in lines:
            point = [int(x) for x in line.split(',')]
            points.append(point)
        maxArea = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xDiff = abs(points[i][0] - points[j][0]) + 1
                yDiff = abs(points[i][1] - points[j][1]) + 1
                area = xDiff * yDiff

                if area > maxArea:
                    maxArea = area
        return maxArea


    def __d9p2(fileName):
        def crossesRect(rect, segment):
            rx1, ry1, rx2, ry2 = rect
            x1, y1, x2, y2 = segment

            xMin, xMax = min(rx1, rx2), max(rx1, rx2)
            yMin, yMax = min(ry1, ry2), max(ry1, ry2)

            if xMin < x1 < xMax and yMin < y1 < yMax:
                return True
            if xMin < x2 < xMax and yMin < y2 < yMax:
                return True

            if y1 == y2:
                if yMin < y1 < yMax:
                    segXMin, segXMax = min(x1, x2), max(x1, x2)
                    if segXMax > xMin and segXMin < xMax:
                        return True

            if x1 == x2:
                if xMin < x1 < xMax:
                    segYMin, segYMax = min(y1, y2), max(y1, y2)
                    if segYMax > yMin and segYMin < yMax:
                        return True

            return False

        with open(fileName) as f:
            lines = f.readlines()
        points = []
        for line in lines:
            point = [int(x) for x in line.split(',')]
            points.append(point)
        maxArea = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                ok = True
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]

                for k in range(len(points)):
                    lineStart = points[k]
                    lineEnd = points[(k + 1) % len(points)]

                    if crossesRect((x1, y1, x2, y2), (lineStart[0], lineStart[1], lineEnd[0], lineEnd[1])):
                        ok = False
                        break

                if ok:
                    xDiff = abs(x1 - x2) + 1
                    yDiff = abs(y1 - y2) + 1
                    area = xDiff * yDiff

                    if area > maxArea:
                        maxArea = area
        return maxArea

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
        },
        6: {
            1: __d6p1,
            2: __d6p2
        },
        7: {
            1: __d7p1,
            2: __d7p2
        },
        8: {
            1: __d8p1,
            2: __d8p2
        },
        9: {
            1: __d9p1,
            2: __d9p2
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
AdventOfCode.Solve(9, 2, "Inputs/Day9/p9.txt")