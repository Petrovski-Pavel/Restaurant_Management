class IdGenerator:
    def __init__(self):
        self._nextId = 0

    def get_next_id(self):
        self._nextId += 1
        return self._nextId


class IdGeneratorProd:
    def __init__(self):
        self._nextId = 100

    def get_next_id(self):
        self._nextId += 1
        return self._nextId