class Box:
    x1: int
    y1: int
    x2: int
    y2: int
    offsets: Tuple[int, int] = (0, 0)

    def __init__(self, x1: int, y1:int, x2:int, y2:int, offsets=(0, 0)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.offsets = offsets

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    def size(self):
        return self.width, self.height

    def area(self):
        return self.width * self.height

    def fits(self, box: 'Box'):
        return self.width >= box.width and self.height >= box.height

    def empty(self):
        return None

    def merge(self, box: 'Box'):
        return Box.replace(self, x1=min(self.x1, box.x1), y1=min(self.y1, box.y1), x2=max(self.x2, box.x2), y2=max(self.y2, box.y2))


    def trim(self, margin: int):
        return Box.replace(self, x1=self.x1+margin, y1=self.y1+margin, x2=self.x2-margin, y2=self.y2-margin)

    @classmethod
    # TODO: add some method if needed

    @property
    def priority(self):
        return (self.x1 + self.y1)/2

    @classmethod
    def replace(cls, box:'Box', **kwargs):
        values = box.__dict__.copy()
        values.update(kwargs)
        return Box(**values)


    def __lt__(self, other: 'Box'):
        return self.priority < other.priority
