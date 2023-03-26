import re
from dataclasses import dataclass
from functools import lru_cache
from queue import Queue
from typing import List

from read_file.read_file import read_file

lines = read_file("input.txt")


@dataclass
class Valve:
    name: str
    flow_rate: int
    tunnels: List[str]


valves = {}
for line in lines:
    possible_paths = re.match(
        "Valve (.+) has flow rate=(.+); (tunnels lead to|tunnel leads to) (valve|valves) (.+)", line)
    name = str(possible_paths.group(1))
    flow_rate = int(possible_paths.group(2))
    tunnels = possible_paths.group(5).split(", ")
    valves[name] = Valve(name, flow_rate, tunnels)


def compute_distances(valves):
    distances = {}
    for valve in valves.values():
        visited = {valve.name}
        queue = Queue()
        queue.put((valve, 0))
        while not queue.empty():
            current, distance = queue.get()
            for tunnel in current.tunnels:
                if tunnel not in visited:
                    distances[(valve.name, tunnel)] = distance + 1
                    queue.put((valves[tunnel], distance + 1))
                    visited.add(tunnel)
    return distances


distances = compute_distances(valves)


@lru_cache
def recurse(current, time_left, remaining_valve_names):
    paths = []
    for remaining_name in remaining_valve_names:
        if remaining_name == current:
            continue
        time_needed = distances[(current, remaining_name)] + 1
        if time_needed < time_left:
            new_time_left = time_left - time_needed
            pressure_due_to_opening = valves[remaining_name].flow_rate * new_time_left
            recursion_paths = recurse(remaining_name, new_time_left,
                                      tuple(valve for valve in remaining_valve_names if valve != remaining_name))
            for (pressure, path) in recursion_paths:
                paths.append((pressure + pressure_due_to_opening, {remaining_name} | path))

    if not paths:
        return [(0, set())]
    return paths


valves_with_flow_rate = tuple(valve.name for valve in valves.values() if valve.flow_rate > 0)

possible_paths = recurse("AA", 26, valves_with_flow_rate)
possible_paths.sort(reverse=True)

# This solution assumes that not all the valves can be opened, which is true for input but not for the example
max_pressure = 0
i = 0
for (human_pressure, human_opened_valves) in possible_paths:
    i += 1
    for (elephant_pressure, elephant_opened_valves) in possible_paths:
        if human_pressure + elephant_pressure < max_pressure:
            break
        if not (human_opened_valves & elephant_opened_valves):
            max_pressure = max(max_pressure, human_pressure + elephant_pressure)
print(f"Part 2: {max_pressure}")
