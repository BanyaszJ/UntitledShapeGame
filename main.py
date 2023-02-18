from imporlist import *
from gamefiles.units import Player
pygame.init()

class Main:
    def __init__(self) -> None:
        self.playfield = Playfield(w = SCREENWIDTH, h = SCREENHEIGHT)
        self.player = Player()

    def mainloop(self) -> None:
        while not self.playfield.check_quit_pressed():            
            self.player.collect_inputs()            
            self.player.move(self.playfield.display)
            self.playfield.update_frame()

class Playfield:
    def __init__(self, w = 0, h = 0) -> None:
        self._width     = w
        self._height    = h
        self._refresh_color = BACKGROUNDCOLOR

        self.display  = pygame.display.set_mode((self._width, self._height))
        self.clock  = pygame.time.Clock()

        pygame.display.set_caption(GAMETITLE)
        print("Playfiled created")

    def check_quit_pressed(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit pressed")
                return True

    def clear(self) -> None:
        self.display.fill(self._refresh_color)

    def update_frame(self) -> None:
            self.flip()
            self.tick(25)
            self.clear()

    def flip(self):
        pygame.display.flip()

    def tick(self, spd = 10) -> None:
        self.clock.tick(spd)
        print("----------tick-tock----------")


main    = Main()
main.mainloop()
