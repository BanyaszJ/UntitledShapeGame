from imporlist import *
from gamefiles.abilities import Abilities

class Unit:
    def __init__(self) -> None:
        self.position = [SCREENWIDTH//2, SCREENHEIGHT//2]
        self.player = pygame.Surface((PLAYERSIZE, PLAYERSIZE))
        print("pos: %s %s" % (self.position, self.player))

class Player(Unit, Abilities):
    def __init__(self) -> None:
        super().__init__()
        # self.position = [SCREENWIDTH//2, SCREENHEIGHT//2]
        # self.player = pygame.Surface((PLAYERSIZE, PLAYERSIZE))
        self.player.fill(PLAYERCOLOR)


    def collect_inputs(self) -> None:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT]:
            print("K_RIGHT")
            self.position[0] += STEPSIZE

        if pressed[pygame.K_LEFT]:
            print("K_LEFT")
            self.position[0] -= STEPSIZE
            
        if pressed[pygame.K_UP]:
            print("K_UP")
            self.position[1] -= STEPSIZE
            
        if pressed[pygame.K_DOWN]:
            print("K_DOWN")
            self.position[1] += STEPSIZE
        
        if pressed[pygame.K_SPACE]:
            print("K_PSACE")
            # self.pulse_aoe = True


    def move(self, surface):
        surface.blit(self.player, self.position)