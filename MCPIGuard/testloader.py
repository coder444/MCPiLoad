from mcpi import minecraft
import cPickle as pickle
import sys
mc = minecraft.Minecraft.create()
pFile = open("saves/save.p", "rb")
pFileData = open("saves/dataSave.p", "rb")
blockList = pickle.load(pFile)
dataList = pickle.load(pFileData)
x, y, z = mc.player.getPos()
for block in blockList:
    
    mc.setBlock(x, y, z, block)
    y += 1
