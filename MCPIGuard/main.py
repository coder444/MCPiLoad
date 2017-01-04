from mcpi import minecraft
import cPickle as pickle
import sys
mc = minecraft.Minecraft.create()

iIn = raw_input("Enter Command: ")

if(iIn == "save"):
    mc.postToChat("Right Click a block with your Iron Sword to load a block into memory")
    pFile = open("saves/save.p", "wb")
    while True:
        blockHits = mc.events.pollBlockHits()
        for blockHit in blockHits:
            blockInfo = {"x": blockHit.pos.x,
                         "y": blockHit.pos.y,
                         "z": blockHit.pos.z,
                         "block": mc.getBlockWithData(blockHit.pos).id,
                         "data": mc.getBlockWithData(blockHit.pos).data}
            pickle.dump(blockInfo, pFile)

            print "dump"
            pFile.close()
            print "close"
            sys.exit()

if(iIn == "load"):
    pFile = open("saves/save.p", "rb")
    blockInfo = pickle.load(pFile)
    mc.setBlock(blockInfo["x"], blockInfo["y"], blockInfo["z"], blockInfo["block"], blockInfo["data"])
