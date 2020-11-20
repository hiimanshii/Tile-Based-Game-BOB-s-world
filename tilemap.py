import pygame as pg
import pytmx
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)
    # everytime when it tries collision b/w player and wall going to compare player hit_rect vs wall rect
class Map:
    def __init__(self, filename):
        self.data = []
        #  open and read from the files rt for read any location we find a one we spawn a wall
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
                # line read hogi txt file se fr usse empty list me append krate c hle jayengy
                # strip command strip away the any slash ends or newline character  and they won't be there when it looks at file
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True )  # pytmx is just for reading tiled map, we use pixelalpha for transparency that goes with our tiles
        self.width = tm.width * tm.tilewidth   # 50 * 64
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm


    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                #  gid global identifier as each tile has its unique id
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface


class Camera:
    # camera object keeps the track of how big our map is
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    # whenever the player move we calculate the offset for how much the player is shifted
    def update(self, target):
        # we move opposite direction of the player  and to keep player centered we add width/2, height/2
        x = -target.rect.centerx + int(WIDTH/2)
        y = -target.rect.centery + int(HEIGHT/2)

        # limit scrolling to  map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # width of camera 2048 - width of the screen 1024 (RIGHT)
        y = max(-(self.height - HEIGHT), y)  # (BOTTOM)
        # rect is now going to be that x,y it stays the same size
        self.camera = pg.Rect(x, y, self.width, self.height)



























