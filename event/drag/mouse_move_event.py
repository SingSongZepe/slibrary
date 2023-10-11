

def mouseMoveEvent(s, eve):
    if s.isMousePressed:
        diff = eve.pos() - s.mousePressPos
        s.move(s.pos() + diff)