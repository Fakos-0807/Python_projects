
from panda3d.core import WindowProperties









class Player:
    def __init__(self, position, land):
        self.player = render.attachNewNode("Player")
        self.player.setPos(position)

        base.disableMouse()
        properties = WindowProperties()
        properties.setCursorHidden(True)
        base.win.requestProperties(properties)
        
        base.camera.reparentTo(self.player)

        base.camera.setPos(0, 0, 2)
        base.camera.setHpr(0, 0, 0)        
    
        self.keys = {"w": False, "s": False, "a": False, "d": False}
        for key in self.keys:
            base.accept(key, self.set_key, [key, True])
            base.accept(f"{key}-up", self.set_key, [key, False])

        taskMgr.add(self.update, "update")



    def set_key(self, key, value):
        self.keys[key] = value



    def update(self, task):
        dt = globalClock.getDt()
        speed = 10

        if self.keys["w"]:
            self.player.setY(self.player, speed * dt)
        if self.keys["s"]:
            self.player.setY(self.player, -speed * dt)
        if self.keys["a"]:
            self.player.setX(self.player, -speed * dt)
        if self.keys["d"]:
            self.player.setX(self.player, speed * dt)

        return task.cont