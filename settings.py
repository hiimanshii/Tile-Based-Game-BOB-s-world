import pygame as pg

vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16(divisible by) a whole no squares up n down cross
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "BOB's WORLD"
BGCOLOR = BROWN

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tileGreen_39.png'

# player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300.0
PLAYER_ROT_SPEED = 250.0  # everything is per second we are using delta time on the frames(easy way adjust how fast or sow we wan the player to be able to turn )
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30,
                    10)  # vec representing how far from the center sprite the barrel of the gun is(20 pixels forward, 20 pixels downward)

# weapons settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 5,
                      'bullet_size': 'sm',
                      'bullet_count': 12}

BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150  # how fast we can shoot if we hold space bar down how fast did the bullets get produced
KICKBACK = 200
GUN_SPREAD = 5  # to give bullet inaccuracy every bullet come out in a perfectly straight line (5 represents how many degree to the left and right that the bullet will travel)
BULLET_DAMAGE = 10  # 10 points of damage and zombie will have 1000 health

# mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400  # how far can zombie see

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png', 'whitePuff18.png']
FLASH_DURATION = 50
SPLAT = 'splat green.png'
DAMAGE_ALPHA = [i for i in range(0, 255, 5)]
NIGHT_COLOR = (50, 50, 50)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_med.png"

# Layers
WALL_LAYER = 1  # wall is at lowest layer as we set 1 (lowest number)
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15  # how many pixels up and down we want our item
BOB_SPEED = 0.4

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}
