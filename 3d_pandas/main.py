from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from player import Player


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.map_manager = Mapmanager()
        self.player = Player((0, 30, 0), self.map_manager)
game = Game()
game.run()