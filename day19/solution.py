import dataclasses
from dataclasses import dataclass
from enum import Enum

ORE_ROBOT_COST_ORE = 4
CLAY_ROBOT_COST_ORE = 2
OBSIDIAN_ROBOT_COST_ORE = 3
OBSIDIAN_ROBOT_COST_CLAY = 14
GEODE_ROBOT_COST_ORE = 2
GEODE_ROBOT_COST_OBSIDIAN = 7


@dataclass(frozen=True)
class Stock:
    ore: int
    clay: int
    obsidian: int
    geode: int


@dataclass(frozen=True)
class Robots:
    ore: int
    clay: int
    obsidian: int
    geode: int


class InProduction(Enum):
    NOTHING = 1
    ORE = 2
    CLAY = 3
    OBSIDIAN = 4
    GEODE = 5


total_minutes = 24

best_score = 0


def recurse(stock: Stock, robots: Robots, in_production: InProduction, minutes_left):
    global best_score
    # Tick
    new_stock = Stock(
        ore=stock.ore + robots.ore,
        clay=stock.clay + robots.clay,
        obsidian=stock.obsidian + robots.obsidian,
        geode=stock.geode + robots.geode,
    )

    new_robots = robots
    match in_production:
        case InProduction.ORE:
            new_robots = dataclasses.replace(robots, ore=robots.ore + 1)
        case InProduction.CLAY:
            new_robots = dataclasses.replace(robots, clay=robots.clay + 1)
        case InProduction.OBSIDIAN:
            new_robots = dataclasses.replace(robots, obsidian=robots.obsidian + 1)
        case InProduction.GEODE:
            new_robots = dataclasses.replace(robots, geode=robots.geode + 1)

    upper_bound = minutes_left * robots.geode + sum(1 for i in range(minutes_left - 1))
    if stock.geode + upper_bound < best_score:
        return
    if minutes_left - 1 == 0:
        best_score = max(best_score, stock.geode)
        print(best_score)
        return

        # Branch
    if stock.ore >= GEODE_ROBOT_COST_ORE and stock.obsidian >= GEODE_ROBOT_COST_OBSIDIAN:
        deducted_stock = dataclasses.replace(
            new_stock,
            ore=new_stock.ore - GEODE_ROBOT_COST_ORE,
            obsidian=new_stock.obsidian - GEODE_ROBOT_COST_OBSIDIAN
        )
        recurse(deducted_stock, new_robots, InProduction.GEODE, minutes_left - 1)
    if stock.ore >= OBSIDIAN_ROBOT_COST_ORE and stock.clay >= OBSIDIAN_ROBOT_COST_CLAY:
        deducted_stock = dataclasses.replace(
            new_stock,
            ore=new_stock.ore - OBSIDIAN_ROBOT_COST_ORE,
            clay=new_stock.clay - OBSIDIAN_ROBOT_COST_CLAY,
        )
        recurse(deducted_stock, new_robots, InProduction.OBSIDIAN, minutes_left - 1)
    if stock.ore >= CLAY_ROBOT_COST_ORE:
        deducted_stock = dataclasses.replace(
            new_stock,
            ore=new_stock.ore - CLAY_ROBOT_COST_ORE,
        )
        recurse(deducted_stock, new_robots, InProduction.CLAY, minutes_left - 1)

    if stock.ore >= ORE_ROBOT_COST_ORE:
        deducted_stock = dataclasses.replace(
            new_stock,
            ore=new_stock.ore - ORE_ROBOT_COST_ORE,
        )
        recurse(deducted_stock, new_robots, InProduction.ORE, minutes_left - 1)

    recurse(new_stock, new_robots, InProduction.NOTHING, minutes_left - 1)


recurse(Stock(0, 0, 0, 0), Robots(1, 0, 0, 0), InProduction.NOTHING, 24)
