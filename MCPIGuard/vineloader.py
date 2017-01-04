from mcpi import minecraft
import cPickle as pickle
import sys
mc = minecraft.Minecraft.create()
pFile = open("saves/save.p", "rb")
pFileData = open("saves/dataSave.p", "rb")
blockList = pickle.load(pFile)
dataList = pickle.load(pFileData)
def main():
    i = 0
    block = 3
    rBlock = 1
    while True:
        blockHits = mc.events.pollBlockHits()
        for blockHit in blockHits:
            if(mc.getBlockWithData(blockHit.pos).id == block):
                oX, oY, oZ = blockHit.pos
                x, y, z = oX, oY, oZ
                
                xX, xY, xZ = x, y, z
                mxX, mxY, mxZ = x, y, z

                nxX, nxY, nxZ = x, y, z
                nmxX, nmxY, nmxZ = x, y, z
                while mc.getBlockWithData(x, y, z).id == block:
                    mc.setBlock(x, y, z, rBlock)
                    print "INITIAL called 1"
                    for l in range(y + 2, y + 4):
                        mc.setBlock(x, y, z, blockList[i], dataList[i])
                        print blockList[i]
                        print "[", i, "]"
                        i += 1
                        y += 1
                        #print blockList
                    
                    
                    
                    
                    y = oY
                    x += 1
                    xZ += 1
                    while mc.getBlockWithData(xX, xY, xZ).id == block:
                        mc.setBlock(xX, xY, xZ, rBlock)
                        
                        for l in range(xY + 2, xY + 4):
                            mc.setBlock(xX, xY, xZ, blockList[i], dataList[i])
                            print blockList[i]
                            print "[", i, "]"
                            i += 1
                            xY += 1
                            #print blockList
                        
                        xZ += 1
                        xY = oY

                    xZ = oZ
                    mxZ -= 1
                    while mc.getBlockWithData(mxX, mxY, mxZ).id == block:
                        mc.setBlock(mxX, mxY, mxZ, rBlock)
                        
                        for l in range(mxY + 2, mxY + 4):
                            mc.setBlock(mxX, mxY, mxZ, blockList[i], dataList[i])
                            print blockList[i]
                            print "[", i, "]"
                            i += 1
                            mxY += 1
                            #print blockList
                        
                        mxZ -= 1
                        
                        
                        mxY = oY
                    mxZ = oZ
                    xX += 1
                    mxX += 1
                #print "[DEBUG] Positive X Scan Complete"

                nxX -= 1
                nmxX -= 1
                while mc.getBlockWithData(nxX, nxY, nxZ).id == block:
                    mc.setBlock(nxX, nxY, nxZ, rBlock)
                    nxZ += 1
                    while mc.getBlockWithData(nxX, nxY, nxZ).id == block:
                        mc.setBlock(nxX, nxY, nxZ, rBlock)
                        
                        for l in range(nxY + 2, nxY + 4):
                            mc.setBlock(nxX, nxY, nxZ, blockList[i], dataList[i])
                            print blockList[i]
                            print "[", i, "]"
                            i += 1
                            nxY += 1
                            #print blockList
                        
                        nxZ += 1
                        
                        
                        nxY = oY
                    nxZ = oZ
                    nmxZ -= 1
                    while mc.getBlockWithData(nmxX, nmxY, nmxZ).id == block:
                        mc.setBlock(nmxX, nmxY, nmxZ, rBlock)
                        
                        for l in range(nmxY + 2, nmxY + 4):
                            mc.setBlock(nmxX, nmxY, nmxZ, blockList[i], dataList[i])
                            print blockList[i]
                            print "[", i, "]"
                            i += 1
                            nmxY += 1
                            #print blockList
                        
                        nmxZ -= 1
                        
                        
                        nmxY = oY
                    
                    nmxZ = oZ
                    nxX -= 1
                    nmxX -= 1
                #print "[DEBUG] Negative X Scan Complete"
                print blockList
                print dataList
                sys.exit()

if __name__ == "__main__":
    main()
                
