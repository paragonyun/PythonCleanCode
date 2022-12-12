"""Container
__contains__를 가지고 있는 객체.
파이썬에서 in 키워드가 발견될 때 호출되며 Boolean값을 반환한다.

element in container  ->  container.__contains__(element)
말 그대로 있는지 없는지 __contains__ 메서드를 통해 확인하는 것
"""

## Bad Case
def mark_coordinate(grid, coord):
    if 0 <= coord.x < grid.width and 0 <= coord.y < grid.hegith:
        grid[coord] = 1

## Good CAse
class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord): # __contains__를 통해 x와 y가 width와 height 안에 있는지 T/F로 return 한다.
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height) # 아까 만들어둔 class를 통해 width와 hegith 안에 corrd가 존재하는지 확인 가능

    def __contains__(self, coord):
        return coord in self.limits

"""두 class는 매우 응집력 있으며 최소한의 logic, 간결하고 자명한 메서드, 적절한 객체명을 가지고 있다. 매우 파이써닉!"""


# 활용예시
def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = 2

