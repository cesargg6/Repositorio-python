from typing import NamedTuple, Set

class Point(NamedTuple):
    x: int
    y: int

def test_typing(data: Set[Point])-> bool:
    data.union(set())
    return True

x:int = 2 
