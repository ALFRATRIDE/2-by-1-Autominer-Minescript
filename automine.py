import minescript
import time
import sys
import math

originYaw, originPitch = minescript.player_orientation()

x, y, z = minescript.player().position

def stepBack():
    minescript.player_press_backward(True)
    time.sleep(0.5)
    minescript.player_press_backward(False)
def walkBack():
    minescript.player_press_backward(True)
    time.sleep(2)
    minescript.player_press_backward(False)

lavaLevels = [
    "minecraft:lava[level=0]",
    "minecraft:lava[level=1]",
    "minecraft:lava[level=2]",
    "minecraft:lava[level=3]",
    "minecraft:lava[level=4]",
    "minecraft:lava[level=5]",
    "minecraft:lava[level=6]",
    "minecraft:lava[level=7]",
    "minecraft:lava[level=8]"
]
susGravelDustLevels = [
    "minecraft:suspicious_gravel[dusted=0]",
    "minecraft:suspicious_gravel[dusted=1]",
    "minecraft:suspicious_gravel[dusted=2]",
    "minecraft:suspicious_gravel[dusted=3]",
    "minecraft:suspicious_gravel[dusted=4]"
]

times = int(sys.argv[1]) if len(sys.argv) > 1 else 1

for _ in range(times):
    x, y, z = minescript.player().position
    ##


    direYaw, direPitch = minescript.player_orientation()
    direYaw_rad = math.radians(direYaw)
    direX = -math.sin(direYaw_rad)
    direZ = math.cos(direYaw_rad)

    targetX = math.floor(x + direX)
    targetZ = math.floor(z + direZ)
    targetY = y - 1
    upY = y + 2
    normY = y + 1

    futureAboveBlock = minescript.getblock(x=targetX, y=upY, z=targetZ)
    # minescript.echo(f"Next Above Block: {futureAboveBlock}")
    futureBottomBlock = minescript.getblock(x=targetX, y=targetY, z=targetZ)
    # minescript.echo(f"Next Below Block: {futureBottomBlock}")

    sideBlock1 = minescript.getblock(x=targetX-1, y=normY, z=targetZ)
    sideBlock2 = minescript.getblock(x=targetX+1, y=normY, z=targetZ)
    sideBlock3 = minescript.getblock(x=targetX, y=normY, z=targetZ-1)
    sideBlock4 = minescript.getblock(x=targetX, y=normY, z=targetZ+1)
    bSideBlock1 = minescript.getblock(x=targetX-1, y=y, z=targetZ)
    bSideBlock2 = minescript.getblock(x=targetX+1, y=y, z=targetZ)
    bSideBlock3 = minescript.getblock(x=targetX, y=y, z=targetZ-1)
    bSideBlock4 = minescript.getblock(x=targetX, y=y, z=targetZ+1)

    diagonalBlock1 = minescript.getblock(x=targetX-1, y=y+1, z=targetZ-1)
    diagonalBlock2 = minescript.getblock(x=targetX-1, y=y+1, z=targetZ+1)
    diagonalBlock3 = minescript.getblock(x=targetX+1, y=y+1, z=targetZ-1)
    diagonalBlock4 = minescript.getblock(x=targetX+1, y=y+1, z=targetZ+1)
    bDiagonalBlock1 = minescript.getblock(x=targetX-1, y=y, z=targetZ-1)
    bDiagonalBlock2 = minescript.getblock(x=targetX-1, y=y, z=targetZ+1)
    bDiagonalBlock3 = minescript.getblock(x=targetX+1, y=y, z=targetZ-1)
    bDiagonalBlock4 = minescript.getblock(x=targetX+1, y=y, z=targetZ+1)

    # Checks
    if futureBottomBlock == "minecraft:air":
        minescript.echo("-! Air Block")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break
    if futureBottomBlock in lavaLevels or futureAboveBlock in lavaLevels:
        minescript.echo("-! Lava Above or Below")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        walkBack()
        break
    if sideBlock1 in lavaLevels or sideBlock2 in lavaLevels or sideBlock3 in lavaLevels or sideBlock4 in lavaLevels:
        minescript.echo("-! Lava")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        walkBack()
        break
    if bDiagonalBlock1 in lavaLevels or bDiagonalBlock2 in lavaLevels or bDiagonalBlock3 in lavaLevels or bDiagonalBlock4 in lavaLevels:
        minescript.echo("-! Lava b.Diagonals")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break
    if futureAboveBlock == "minecraft:gravel" or futureAboveBlock in susGravelDustLevels:
        minescript.echo("-! Gravel")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break
    if futureAboveBlock == "minecraft:sand":
        minescript.echo("-! Sand")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break

    minescript.player_set_orientation(yaw=originYaw, pitch=15)
    minescript.player_press_forward(True)
    minescript.player_press_attack(True)
    time.sleep(0.3)

    x, y, z = minescript.player().position
    # Log
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(r'./blocks.log', "a") as logFile:
        logFile.write(f"{timestamp} Position: {math.floor(x), math.floor(y), math.floor(z)} \n")
        logFile.write(f"{timestamp} f.Side Blocks: {sideBlock1}, {sideBlock2}, {sideBlock3}, {sideBlock4} \n")
        logFile.write(f"{timestamp} b.Side Blocks: {bSideBlock1}, {bSideBlock2}, {bSideBlock3}, {bSideBlock4} \n")
        logFile.write(f"{timestamp} Future f.Diagonal Blocks: {diagonalBlock1}, {diagonalBlock2}, {diagonalBlock3}, {diagonalBlock4} \n")
        logFile.write(f"{timestamp} Future Above Block: {futureAboveBlock}. Future Below Block: {futureBottomBlock} \n")
        logFile.write("------------------------------------------------------------------------------------------------------------------ \n")
    
    # Checks
    if futureBottomBlock == "minecraft:air":
        minescript.echo("-! Air Block")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break
    if futureBottomBlock in lavaLevels or futureAboveBlock in lavaLevels:
        minescript.echo("-! Lava Above or Below")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        walkBack()
        break
    if sideBlock1 in lavaLevels or sideBlock2 in lavaLevels or sideBlock3 in lavaLevels or sideBlock4 in lavaLevels:
        minescript.echo("-! Lava")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        walkBack()
        break
    if bDiagonalBlock1 in lavaLevels or bDiagonalBlock2 in lavaLevels or bDiagonalBlock3 in lavaLevels or bDiagonalBlock4 in lavaLevels:
        minescript.echo("-! Lava b.Diagonals")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break
    if futureAboveBlock == "minecraft:gravel" or futureAboveBlock in susGravelDustLevels:
        minescript.echo("-! Gravel")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break
    if futureAboveBlock == "minecraft:sand":
        minescript.echo("-! Sand")
        minescript.player_press_attack(False)
        minescript.player_press_forward(False)
        stepBack()
        break

    minescript.player_set_orientation(yaw=originYaw, pitch=40)
    time.sleep(0.3)


    ##
    x, y, z = minescript.player().position

    
minescript.player_press_attack(False)

minescript.player_press_forward(False)
