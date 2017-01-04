from mcpi import minecraft
import cPickle as pickle
import sys
mc = minecraft.Minecraft.create()

blockList = []
dataList = []
def main():
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
                    
                    for i in range(y + 1, y + 3):
                        blockList.append(mc.getBlockWithData(x, y, z).id)
                        dataList.append(mc.getBlockWithData(x, y, z).data)
                        print "np", "[", x, y, z, "]", mc.getBlockWithData(x, y, z).id
                        y += 1
                        #print blockList
                    
                    
                    
                    
                    y = oY
                    
                    x += 1
                    
                    xZ += 1
                    while mc.getBlockWithData(xX, xY, xZ).id == block:
                        mc.setBlock(xX, xY, xZ, rBlock)
                        
                        for i in range(xY + 1, xY + 3):
                            blockList.append(mc.getBlockWithData(xX, xY, xZ).id)
                            dataList.append(mc.getBlockWithData(xX, xY, xZ).data)
                            print "x", "[", xX, xY, xZ, "]", mc.getBlockWithData(xX, xY, xZ).id
                            xY += 1
                            #print blockList
                        
                        xZ += 1
                        
                        
                        xY = oY
                        
                    xZ = oZ
                    mxZ -= 1
                    while mc.getBlockWithData(mxX, mxY, mxZ).id == block:
                        mc.setBlock(mxX, mxY, mxZ, rBlock)
                        
                        for i in range(mxY + 1, mxY + 3):
                            blockList.append(mc.getBlockWithData(mxX, mxY, mxZ).id)
                            dataList.append(mc.getBlockWithData(mxX, mxY, mxZ).data)
                            print "mx", "[", mxX, mxY, mxZ, "]", mc.getBlockWithData(mxX, mxY, mxZ).id
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
                        
                        for i in range(nxY + 1, nxY + 3):
                            blockList.append(mc.getBlockWithData(nxX, nxY, nxZ).id)
                            dataList.append(mc.getBlockWithData(nxX, nxY, nxZ).data)
                            print "nx", "[", nxX, nxY, nxZ, "]", mc.getBlockWithData(nxX, nxY, nxZ).id
                            nxY += 1
                            #print blockList
                        
                        nxZ += 1
                        
                        
                        nxY = oY
                        
                    nxZ = oZ
                    nmxZ -= 1
                    while mc.getBlockWithData(nmxX, nmxY, nmxZ).id == block:
                        mc.setBlock(nmxX, nmxY, nmxZ, rBlock)
                        
                        for i in range(nmxY + 1, nmxY + 3):
                            blockList.append(mc.getBlockWithData(nmxX, nmxY, nmxZ).id)
                            dataList.append(mc.getBlockWithData(nmxX, nmxY, nmxZ).data)
                            print "nmx", "[", nmxX, nmxY, nmxZ, "]", mc.getBlockWithData(nmxX, nmxY, nmxZ).id
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

                pFile = open("saves/save.p", "wb")
                pFileData = open("saves/dataSave.p", "wb")
                print "LOAD"
                pickle.dump(blockList, pFile)
                pickle.dump(dataList, pFileData)
                print "DUMP"
                pFile.close()
                pFileData.close()
                print "ClOSE"
                print "EXIT"
                sys.exit()

if __name__ == "__main__":
    main()
                
