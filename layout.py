def random_layout(grids: typing.List[Box], slot: Box):
    packed: typing.List[Box] = []
    extras: typing.List[Box] = []
    grid : Box
    for grid in grids:
        points = [] 
        w, h = grid.size()
        for x in range(slot.x1, slot.x2+1 - w):
            for y in range(slot.y1, slot.y2+1 - h):
                for p in packed:
                    if p.overlaps(x, y, w, h):
                        break
                else:
                    points.append((x, y))
        if points:
            (x, y) = random.choice(points)
            grid_box = box_replace(grid, x1=x, y1=y, x2=x+w, y2=y+h)
            packed.append(grid_box)
        else:
            extras.append(grid)
    return packed, extras
