from typing import Callable, TypeVar, Iterable

E = TypeVar('E')
def find_first(predicate: Callable[[object], bool], iterable: Iterable[E])->E:
    for element in iterable:
        if predicate(element):
            return element

def find_every(predicate: Callable[[object], bool], iterable: Iterable[E])->E:
    all = []
    for element in iterable:
        if predicate(element):
            all.append(element)
    return all
