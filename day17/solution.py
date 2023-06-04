import copy
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def plus(self, other):
        return Point(self.x + other.x, self.y + other.y)


shapes = [
    # ####
    (Point(2, 0), Point(3, 0), Point(4, 0), Point(5, 0)),
    # .#.
    # ###
    # .#.
    (Point(3, 0), Point(2, 1), Point(3, 1), Point(4, 1), Point(3, 2)),
    # ..#
    # ..#
    # ###
    (Point(2, 0), Point(3, 0), Point(4, 0), Point(4, 1), Point(4, 2)),
    # #
    # #
    # #
    # #
    (Point(2, 0), Point(2, 1), Point(2, 2), Point(2, 3)),
    # ##
    # ##
    (Point(2, 0), Point(3, 0), Point(2, 1), Point(3, 1)),
]

pattern = ">>>><<<><>>><<<<>>><>>><>><<<<>>><>><<<<>><<<<>><<<>>>><>>>><<<<>>><>><<>>>><>>>><<>>>><<<<>>>><<<<>>><<>>><<<>>><<<<>><<>><>>>><<<>>><>><<<<>><<<>><<>>>><<<<>>>><<><>>><<<<><>><<<<>>>><><<<<>>><<<<>><<<<>>><<<>><<<>>><<>><>>>><<<>>><>>>><<<<>>>><<>>>><><>>>><<<><<<<><<<<>>><<>>><<<<>>><<<>><<<<>><>><<>>><<>>><<<<>>>><<>>><<<>>><<>>><<<>>><<<>><<>><<<>>>><>><<<<>>>><><>><>><<><<<><<<<>>><<<<>>><>><<<<><<<>>><<<<>><<>><<<<>>><<<>>><<>>>><<<>>><<<>>><<<<><<>><>><<<<><<<><<><<<><<<>>>><<<><<>>><<<<><<<<>>><>><>>><<<>><<>><<<<>>><<>>><><<<<>><<><<<<>><<<<>>><<<<>><>><<>><<<<>><<>>>><<<>><<<<>>><<<>>>><><<<>>>><<<>>>><<><<<<>>>><><<>>>><<>><<<<>>>><><<<>><><<<>>><><<<>><<<>>><>>><<<>>><<<<>>>><<<>>>><>>><>>>><<>><<><<<><<>>><<>><<<><<<<><<<>>>><<>>><<>><<>><><><<>>><>>>><<>><<<>>>><>>><><<>>>><>>>><>>><<<>><<<<>><<><<<<>>><<><<>>>><<<<>>><<<<>>>><<<<>><<><<<<>><>>>><<<<>><<<>>><<<>>>><>><>>>><>><<>>><<>>>><<<>><<>>>><<<<>>>><<><<<<>>><><<<><<<<>>><<>>>><>>>><>>>><<>><<>><<><<<><<<<>>><<<<><<<>>>><<>>><<<<>>><>>>><<>>>><<>><<>>><<>><<<<>><>><<<<>>>><<>>><<<>>>><>>>><<<><>>>><<>>>><<<>>><<><>>><>>><<<<><>><<<>><<><<<>><><>><><<>><<<>><<<>><<<>>><<>><<>><<<<>><>>><><<<><>><>><<<<>><<>>><<>>>><<<<>><<<<>>>><<<<><<<<>>><>>>><<<>>>><<<>><<><<<<>>><<<><<><<<>>>><<<<>><<>>>><>>>><<>><<<<>><<<<><>>>><><<<<>><>><<>>><><>><><><<<<>>>><>>><<>><<<>>><<<>><<>>>><<<><<<<><>><<>><>><>>><>>><<>>><<<<>><>>>><>>><<<<><<><<<<>><>><>>>><>><<>>><>><><<<><<<>>><<<>>><<<<><<>>>><><<<>>>><<>>><<<>>><<<>>><<<<><><<<>>>><<<<>>>><<<<>>><><<<<><>>>><<<><>>>><>>>><<<<>>>><<<>>>><<<<><<<>><<>>><<<>><>><>>><><<<<><<<<><<<><><<<<>><<>>>><>>><><<<<>>><>><<<>><<>>><<<><<><<>>>><<<<>>><<<>>>><<<>>><<><<<><<<<>>>><<>><>><<<>>>><<>>><>>><<<>>><<<<>>><><<<<>>>><<<>><<<><<>><<>>>><<<>><<>>>><<>><<<><>>><>><><<<<>>>><><<<<>>><<<>>>><<<<>>>><<>>>><<>>><>>>><<<>>>><<<>>><<<><<<<><>><<<<>>><<<<>>><<>><<<<>>><>>><<<<>>>><<>><<>>><<<<><<>>>><<>><<>>>><>>>><<<>>>><<<><>><>>>><<<<>><<>>>><<<>>><<<<>>>><><<>>><<<>>><<<>>><<>>>><<<>>><>>><<<<>><<><<<<>><<<<>>>><<<>>>><>>>><>>><<>>>><<><<<>><>><<<>>>><<<<><<<<><<<<>>><<<<><><<>><<>><<<<>>>><<>>>><>>><<>>>><<<<><>><<>>>><>><>>><<<>><<<<>><<<><<<>>>><<<>><<>>>><<<<><<<<>>><<<>><>>><<><<>>>><<<<><<<<>>>><<<>>>><<>>><>>><<<>><<><<<>>>><>>>><<<>>>><<<<>>><<<>>>><>>>><<<<>>>><<<>><<<<>>>><><<<>><<<<><<<><<>>>><<>>><>>><<<>>><<<<><<><<><<<><<<>>>><<<<><<<<><<><<>>><>><<>><<><<<>>>><<<><<<<>>><>>>><<<<>>>><<<<><<<>>>><<<>>>><>><<>>><>>>><<>>><<>>><>><<>><<>>>><<>>>><>><<><<<<>>><<>>><>>>><<<<>>><<<>>><<<><<<<><<>><>><<<<>>><<>>>><>>>><<<><><<>>><<><<<><<<><>>>><<><>><>><>><<<>>>><<<>><<>>>><<<>>><>>>><<<><<><<<<>>>><>><<><<<<><<<><<<>><><<<>><><<<<>>><<<<>><<<<><<<>>>><<<<>>>><<<>><<><>>>><<>>><>>><<<>>><>>>><<>><<<<>><<<<>>>><<>>><<<>><<<<>>><<<<>>>><>>>><<<<>><>>>><<<>><>>><<<<>>><<<<><<<<>>><<>><<<>><<<<>><<><<>>><<>>><<<>><<>>><<>>>><<<>>>><<<<>>>><<><>>>><<>><>><<<>>><<<>>>><>>>><<<>><<><><>>>><<><<<>><>><><<>><<<>>><<>><<<<><<>>><<<><<<<>>><<>><<<>>><<>>>><<<>><<<><<<<>>>><<<>>><<<<><<<<><>>>><<<>><<<>>>><<<>>>><><<<<>>>><>>>><<<>><>><<<<>><><<<>>><<<<>>>><>><<<<>><><<<>>>><<<>>>><<<<>>><>><<<<>><<<<>><<<<>>><<>><<<><>>><><<<<>>><<<>>>><<<>>>><<<>>><<<<>><<><<<<>>><<>>>><<<<>><<>>><>>><<<>>><<<<>>>><<>><<<>><<>>>><<>>><<<<>>><<>>>><><<<>>>><<<<>>><<<<>><<<>>><>><<>>><<>>>><<<>>><<>>>><>><>>>><<<<>>>><>>>><<<>><<<<>>>><<<<>>><>>><<<>>>><<><<><><<<><<<>>>><<>>><<>><<<<>><<>>><<><<<<>><<<>>><<>><>><<><<<<><>>><<<>>>><>>>><<<<><<<>><<>>><>><>><<>>><<<><<<<>>><>>>><<<>>>><<<>>>><>><><<<>>>><<<<><<<>>>><<<<>>><>>><<<<>>><>>>><<>>><<<>><<<<><<<><<>>><<<<><<>>>><<<>>>><<<>>><<>><<<<>><><<<<><<<>><<>>>><>>><<><<><<<><<>>>><<>><<>>>><<>>>><<<>>><<>><<>>><<<><>>>><<<>>><>>><>>><>><<>><>><<<<>>>><><<<<>>><><<<>>>><<<<>><<<<>>><<>>><<<>>>><<<<>>>><<<<><>>><<><<<>>>><<<>><<<<>>>><<<><<<>><<<>><<>>><<<>>><><><>>>><>>>><<>>><<<>>><>>>><<<>><>>><>>><<<<>><<><<<<><<><<<<>>>><<<>><><>>>><<<>>><<<>><<>>>><><<<<>><<<<>>>><<<><<>>><<>>><<<<>>>><<>><<>>><>>><<>>><<><>><<>><>>><<<<>><<<>>>><<<>><<<<>>>><>>><<<>>><<<<>>>><<<>><<><>>>><<<<><<>>><<>>>><<<<><>>><<<<>>>><><<<<>>><>><<<<>><<<<><<<>>><<<<><<>>>><<<<>>><<<><<><<<>><<<<><<<>><<<><>>><<<<>>>><>>><<>>>><<<>>><<<<>>>><<<<>>>><<<>><<>>><<>>><<<>>><<<<>><<<>>><<><<>>><<<<>>>><>>><<<>><<<>>><<><<<>>>><<<><<<<>>>><<<>><<<<>>><<>>>><<>><<<><><><<<><<<>>><<<>><><><<<><<<<>><>>>><<<>>><<<>><<<>>>><>><<>><>>>><<>>>><><>><<>>>><<<>>><<<>>>><<<>>>><<<><<><<<>><>>><<<<>>>><<>><<<<><>>><<>>>><<<<>>><<><<<>>>><<<><<<>>>><<<<>>><<<<>>><<<>><<>>>><<<>>>><<<><<><>>><<<<>>><<>>><<>>><<<><<<><<>><<<><>><<>><<<<><<>>>><>>><>>><>>><>><><<<>>><<<>>>><<>><>><<><<>>><<>>><><<<><<><<<<>>><>>>><<<<>>>><<>>>><<<>><<<>><><<<<>>><<<><<<<>>><>>>><<>>>><<>><<<>>><<<><<<<>>><<>>><<><>>>><><<<>>><<<>><><><<<><<<><<<<>>><<><>>><<<<>><<<<>>><<<><<<>>><<><<<><<<><<<<>><><>><><<<>>>><<>>><>><>>><><<<<>>>><<<<>>>><<<>>>><<<>>><<<<>>>><<<<><<<<>><>>>><<><<<<>>>><<>>><<><><<<<>><<<>>>><<<>>><<<><<>>>><<><<>>><<>><<>><<<>>>><<>>><<<<>>>><<<><>>>><>><<<>>>><><<<<>>>><<>>>><<<>>><<>>>><<<>>><<<<>><<>>><<<<>>><>>><<<><<>>><>><<>><<<<><<<<>>>><<<<>><>>><<<<>>>><<<<>>>><<<<>><<<<>>><<<>>><<<>>><<>><>>><<>>>><>>><>>>><>>><<<><<<>><<<><<<<><<<>><>><><<<<>>>><<>>><<<>>>><<><>>>><<<<>>><<><<>><<><<<><<<<>><>>>><><<<><<>><<<>><<<<>>>><>>>><<<<>><<<><<<<><<>>><<<<><<<>>>><<<>>>><<>><<<<><>><><><><<>>><<<><<>><<>>>><<<>>><>><<<>>><<<>>><<>>><>>><<<<>>>><<<<>><<<<>>><<<>><<<>>>><<><>><><<><<>><<<>>>><<<><<>>>><<><<<<>>><<>><<<>>><<><<>>><<<>><<><<>><<><<><<<>>>><>>><<<><<<>>>><><<<>><<<>>><<><>>><<<<>>>><>><<<><>>><<>>>><<<><<<>><>>>><<<><<<<><>><<<<>>><<<<>><><><<<>>>><<<>>><<>>><<<<>>><<<<>>><<<<>>><<<<>>><<>>>><<>>>><<<<>>><<>><><>>>><<>>><>>>><<<>><<<<>>>><<<<>>><<<>>>><>><<<<>>>><<<<><<<<>>>><><>><>>><<>><>>>><<<<>>><<<><<<><<<>>>><<<>>>><><><<<>>>><>>><<<>><><<<<><<<<>><<<>><><<>>><<<<><<>>><<>>><<>>><>>>><<<>><><<<>>><<<<>>><<<<>><><<<<>><<<>>>><<<<>>><<<>>><<><<>>>><>><<<><<<>>>><<<><<<<>>><>>>><<>>><<<<>><<<<>>>><<<>>><<<>>><<<>>><<<>>><<<>>><><><<>><>>><<<>>><<><>>>><<>>><<<<>><<><<<<>>><<<<><<>><>><<<>><<<<><<<<>>><<><>><<<<>><<<>>>><<<>>>><<<<>><<<>>><<>>>><<<<><<<<>>>><<<<><<<<>>>><>>><<<<><<<><<<>>><<<>>>><>><<<>><<>>>><>>><><<>>><<<<>>>><>>><<<>><<>><<<>><<<<>><<<<><<<<><<<<><<<<>><<>><<<><<>>><<<<>>><>><<><>>>><<<>>><<<<>>><<>>><<<><<<<>><<>><<>>>><<<<><>>>><<<><<>>>><<<<>>>><<<>><<>>>><>><<<<>>><<<<><<>><<<<>>>><><><<>><<>>><<<>><<<<><<<>>>><<<>>><<<<><<<<><>>>><><<<>><<<>><>>><<><><<<><<><>>>><<<<>>><<<<><<<<>>><<<<>>><<<<><>>>><<<>>>><<<>>>><<<<><<>>><<>>><<<<>>>><<<<>>><<>>>><><><<><<>><<>><<><<>>>><>><><<<>>>><<<>><<<>>>><<>>>><>>><<>><<<<>><>>><<<><<<<><<<><<<<>>><<<>><<>>>><<<>>>><<<<>>>><<<<>>><>>><<<>>><>>>><<<<>><<<<>>>><<>>>><<>><<<<>>>><<>><>>><<<>>><>>>><<><<<<>><<>>><<<>>><<<><<<<><<<<>><<>><>><>><<>><<>>><<<<>><<<>><<<<>><>><<<>>>><>>>><>>><<>>><><<<<>>>><<>><<<<>>>><<>><<<>>><<<><<<<>>><<>><<<>>>><<<>>>><<>>>><>><<<>><>>>><<>>><<>>>><<<>>>><<>>><>>><<<>>>><<>><<<<>>><<>><<<>><>><<<><<<><<<>><<<<>><<<<>>>><<>><><>>><<<>>><<<<><<<>>>><<<<>>><>><<<>>><<<<>>><<<>>><><<><<>><>>><<>>><<<<>>>><<<<>>>><<<>>>><><<<>>>><<><<<<>>>><<>><>>><><<<>>><<<>>><<<>>>><<<<>>><>>><<<<><<<>>>><<<>>>><<<>>><<<<><<>>><>><<<<>><>><<<<><<>>>><<<>>>><<<<>>>><<>>><><<<>>><<<>><<<<>>>><<<<>>><<>>><<<>>>><>>>><<<>>><<>><<<<>><<<>><<<>><<<<>><<<>><<><<><>><><><<>>>><<>>><>>>><>><><>><><<>>><<>>>><>><<<<>><><<<><<<<>>><<>>>><<<<>>>><><>><<>>>><<><<<>>><>><<<<>>><<>><<><<>>>><<<<>>><<<>>><<<<><<<><<<><<<><>><<<>><<<><<<<><<<>><<><<<<>><<>><>>><<>>><>>>><><<>><<>><<>>>><>>><<<<>>>><<<>><>><<<>>><<<<>><<>>><<<<>>>><<<<>><<<><>><<><<<>>><<<<>>><<<>>><<>><<<>>><>>>><<<<>><<<<>><<>>>><<<>>>><<<><<<>><>>>><<><<<<>>>><<<><>>>><<>>><<<>>><<>>>><<<>>>><<<><<<>><<<><<>>><<<<>>><<><<<<>><<<><<<<>>>><<>>>><<<>><<>><<<>>>><<<><<<><<<<>>>><>>><<<>>><<<<>>><<<<><<<>>>><<<<>><<>><<><<<>>><<<>>><<<>><>>>><>><<><<<<>>>><>><><><<<<>><>><<<<>><><<<>>><<<<><>>><><>>><<<<>>><<>>><<<>>>><<<<>>><<<<><<<>>>><<>>>><>><<<>>><<<<>><<>>><<<<>>>><<<<><<>>>><<<>><<<>>><<<<><<>>><<>>><>>>><<<<>>><<<><<<>>>><>><<<>><<<>><><<<<><<>>>><<>><>>><<>><<<<>>>><<>><>>><<<<>><><<<<>><<<<>>><<<<>>>><<<><<>>><<<>><<<>>>><<>><<>><>>><<>>>><><<>><<>>>><<>>><>>><<<<>><<>>><<<>>><<><<<<>><<<><<<<>>>><<<>>><<<<>>><<<<>>><<<>>><<<<>>>><>>><<<<>>><<<>>>><<><<<<>>><<>>>><<<>>>><<<<>>>><<>>>><<><<<<>><><<<>>>><>>>><<>>>><><<<>>><<>>>><><<<>><<<>>><<<>>>><>>>><>>><<>>>><<<>>>><<>>><<<<><<<<>><>><<<>>>><<><<<>>><<<>><<>><<<<>>>><<><<<<><<>><<>>><>><<<>>><><<<>>>><<><<<>>>><<<><<<>><>>>><>>>><<<>>>><>>><>>><<<><<<<>>><<<<><<<><<>>>><<<>>>><<<<><<<><<<>>>><<<>>>><<>>>><<<><<>>>><><<>><<<><<<>>><<<>><<<<><<><<<<><<<>>>><<<>><<><<>><<><<<>><<>>>><<<>><<<<>><<<>>><>>>><<<<>>>><<>>>><>>>><<>><<>><<<><<<<>><<>>><<<<>>><<>>>><<><<<<><<<>>><<<<><<<>>><<>><<<<>>><<<<>>><<<<>>>><<>><<<<>>>><<<<>><<<<>>><<<<>>><<<>>>><<>><<<<>>><<><<<<>><<>>>><<<<><<>>>><>>>><>>><>>>><<<><<<<><<>><<<<>><<<>>>><<<<>>>><<>><<>>><<<><<<>><><<<<><<<<>>><<<<>>><<<>>><>><<><<>><<<>>>><<<<>><>><<><<<<>>><<<>>><<<<>><<>>>><>><>>>><<<>>><<<<>>><<><<>><<<>><<<><>>><><<>>><<<>>><<<>>><<<<>>>><<<>><<<>><<<>>><<<<>>>><<<><<>>><>>><>><>>>><<<>><<<><<<>>>><<<<><<<>><>>><>><<<><><<><<<>>><>><<<<>><<<<>>>><<>><>><<<<>><>><<<<>>><<<<>><>>><>>>><<<<>>>><<<><<<>>><>>>><<<<>>>><<<<>><<<><<<<>>>><<<>>><<><<<>>><<<>>>><>><<><<<><<<<>><<<>>><<<>>><<<>>><<<>><<<<>>>><<<<>><<>>><>>><<<><<>>><<<<><<<>>><<<<>>>><<<<><>><<>>>><<<>><>>><<><<<<>>><><<<><<>><<<<><<<>>>><><<><<>>><<>>><>>><>>><>>>><<><><><<>>>><>>>><<<<>><<<<>>>><><<<<>>><<<><<<<><><<>>><<<<>>><<<<>><<<<>>>><<><<<>>><<<<>>>><<<><<<<><>>><<<>>><>>>><<<>><<<<>>>><<<<>><<<><<<>>><><<>>><<>>><>>><<<<><<<>>><<<<><<<>>><<>>><<<><<>><><<>>><<<<>>><<<<>>>><<>><<<<><><<<><<<<>>>><<><>><<>>>><>>><<>>>><<><<<>>>><<<<>><<<><<>>>><<>>><<>><<<>>><<><<<<>>><<<<>>>><<<<><<<>><>>><<<>>>><<<><<<<><<>>><<>><>>>><>>><<<<>>>><<<<>><><>>>><<>>><<><<<>>><<<<><<<<>>><>>>><<<<><<<><<<<>>>><<>><<<<>>>><<<>><<>><>>><<<<>>>><>>><>>><<><>><<<><>><<<<>>>><><<>><<<>><>>><><<>>><<<<>><<><<<<><>>><<<><<<<>>"


def calculate_heights(iterations):
    cache = {}

    i = 0
    pattern_i = 0

    occupied = set()
    height = 0

    def is_valid(shape: Tuple[Point]) -> bool:
        for rock in shape:
            is_valid_rock = 0 <= rock.x <= 6 and rock.y >= 0 and rock not in occupied
            if not is_valid_rock:
                return False
        return True

    while i < iterations:
        shape_i = i % len(shapes)
        shape = copy.deepcopy(shapes[shape_i])
        offset = 3 if not occupied else 4
        shape = tuple(rock.plus(Point(0, height + offset)) for rock in shape)

        cache_key = [shape_i, pattern_i]
        for y in range(height, height - 20, -1):
            for x in range(0, 7):
                cache_key.append(Point(x, y) in occupied)
        cache_key = tuple(cache_key)

        if cache_key in cache:
            old_height, old_i = cache[cache_key]
            height_in_one_cycle = height - old_height
            cycle_length = i - old_i
            number_of_cycles_to_take = (iterations - i) // cycle_length
            extra_height_from_cycles = number_of_cycles_to_take * height_in_one_cycle
            i += number_of_cycles_to_take * cycle_length
            cache = {}
        else:
            cache[cache_key] = (height, i)
            falling = True
            while falling:
                jet = pattern[pattern_i]
                match jet:
                    case "<":
                        new_shape = tuple(rock.plus(Point(-1, 0)) for rock in shape)
                        if is_valid(new_shape):
                            shape = new_shape
                    case ">":
                        new_shape = tuple(rock.plus(Point(1, 0)) for rock in shape)
                        if is_valid(new_shape):
                            shape = new_shape

                new_shape = tuple(rock.plus(Point(0, -1)) for rock in shape)
                if is_valid(new_shape):
                    shape = new_shape
                else:
                    falling = False

                pattern_i = (pattern_i + 1) % len(pattern)

            for rock in shape:
                occupied.add(rock)
                height = max(height, rock.y)
            i += 1
    return extra_height_from_cycles + height + 1


print(f"Part 1: {calculate_heights(2022)}")
print(f"Part 2: {calculate_heights(1000000000000)}")