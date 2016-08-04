#given a rectangle of size 3x2,
#18 total rectangles are contained within.
#6 1x1, 4 2x1, 3 1x2, 2 3x1, 2 2x2, 1 3x2.
#given dimensions nxm containing p rectangles
#find dimensions fitting closest to 2 million (p~=2x10^6).
#approach: given a mxn rectangle, new rectangles may be formed
#using a combinational formula C(m+1,2)*C(n+1,2)
#that is the combination of horizontal lines that may be drawn multiplied
#by the number of combinations of vertical lines.
#since we are looking for p, we have C(m+1,2)*C(n+1,2) (closest to) p
#or (m+1)!/(2*(m-1)!)*(n+1)!/(2*(n-1)!)=p
#or (m+1)(m)(n+1)(n)/4=p
#or 4*p=(m+1)(m)(n+1)(n)

from math import sqrt

p = 8000000
sp = int(sqrt(8000000))
sum = 1000000
actual = 0

for m in range(sp):

    for n in range(sp):
        combo = (m+1)*m*(n+1)*n
        temp = abs(p-combo)
        if temp < sum:
            sum = temp
            actual = m*n
print actual
