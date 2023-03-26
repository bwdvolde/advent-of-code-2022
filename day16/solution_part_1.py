import re
from dataclasses import dataclass
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
    result = re.match("Valve (.+) has flow rate=(.+); (tunnels lead to|tunnel leads to) (valve|valves) (.+)", line)
    name = str(result.group(1))
    flow_rate = int(result.group(2))
    tunnels = result.group(5).split(", ")
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


def recurse(current, time_left, remaining_valve_names):
    max_pressure = 0
    for remaining_name in remaining_valve_names:
        if remaining_name == current:
            continue
        time_needed = distances[(current, remaining_name)] + 1
        if time_needed < time_left:
            new_time_left = time_left - time_needed
            pressure_due_to_opening = valves[remaining_name].flow_rate * new_time_left
            max_pressure_in_recursion = recurse(remaining_name, new_time_left,
                                                [valve for valve in remaining_valve_names if valve != remaining_name])
            max_pressure_of_remaining = pressure_due_to_opening + max_pressure_in_recursion
            max_pressure = max(max_pressure, max_pressure_of_remaining)
    return max_pressure


remaining_valves = [valve.name for valve in valves.values() if valve.flow_rate > 0]

result = recurse("AA", 30, remaining_valves)
print(result)
