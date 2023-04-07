WIDTH = 800
HEIGHT = 600
PLAYER_ACC = .4
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 10
PLAYER_GRAV = 1
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 5, 100, 20, (200,200,200), "bouncey"),
                 (500, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
                 (190, 450, 100, 20, (200,200,200), "normal"),
                 (105, 500, 50, 20, (100,100,100), "normal")]
