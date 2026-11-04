from blocks import BlockType

class Mapmanager():
    def __init__(self):
        self.model = "resources/block.egg"
        self.texture = {
            BlockType.OBSIDIAN: 'resources/obsidian.jpg',
            BlockType.GLOWSTONE: 'resources/glowstone_texture.jpg',
            BlockType.DIAMOND: 'resources/diamond.jpg'
        }




        self.map = render.attachNewNode("Map")
        self.map.setPos(0,20,0)
        self.generate_world()


    def add_block(self, position, blockType):
        block = loader.loadModel(self.model)
        
        block.setTexture(loader.loadTexture(self.texture.get(blockType)))
        
        block.setPos(position)
        block.setHpr(0, 90 ,0)
        block.reparentTo(self.map)

    def generate_world(self):
        for x in range(0,128):
            for y in range(0,128):
                self.add_block((x,y,0), BlockType.OBSIDIAN)    