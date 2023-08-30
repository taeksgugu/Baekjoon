import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    order = input().rstrip()
    x, y = 0,0
    minx, maxx, miny, maxy = 0,0,0,0
    direction = 'top'
    for o in order:
        if o == 'F':
            if direction == 'top':
                y += 1
                maxy = max(maxy, y)
            elif direction == 'bottom':
                y -= 1
                miny = min(miny, y)
            elif direction == 'right':
                x += 1
                maxx = max(maxx, x)
            else:
                x -=1
                minx = min(minx, x)
        elif o == 'B':
            if direction == 'top':
                y -= 1
                miny = min(miny, y)
            elif direction == 'bottom':
                y += 1
                maxy = max(maxy, y)
            elif direction == 'right':
                x -=1
                minx = min(minx, x)
            else:
                x += 1
                maxx = max(maxx, x)
        elif o == 'L':
            if direction == 'top':
                direction = 'left'
            elif direction == 'bottom':
                direction = 'right'
            elif direction == 'right':
                direction = 'top'
            else:
                direction = 'bottom'
        else:
            if direction == 'top':
                direction = 'right'
            elif direction == 'bottom':
                direction = 'left'
            elif direction == 'right':
                direction = 'bottom'
            else:
                direction = 'top'
    if minx==maxx or miny==maxy:
        print(0)
    else:
        print(abs(minx-maxx)*abs(miny-maxy))