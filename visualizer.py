from networktables import NetworkTables
import logging
from pygame import *
import threading
from networktables import NetworkTables
from collections import namedtuple
Pos=namedtuple('Pos',['x','y'])
class GUI():

    def __init__(self,table):
        self.table=table
        self.screen=display.set_mode((1000, 518))
        self.field=transform.scale(image.load("field.png"),(1000,518))
        self.running=True
        self.initPos=Pos()
        self.robotPos=Pos()
        self.mPos=None


    def run(self):
        self.mPos=Pos(mouse.get_pos())

        for e in event.get():
            if e.type == QUIT:
                self.running = False
            if e.type==MOUSEBUTTONDOWN:
                if not self.curPos:
                    self.initPos=Pos(self.mx,self.my)
                    table.setNumber('initX',self.initPos.x)
                    table.setNumber('initY',self.initPos.y)





        self.screen.blit(self.field,(0,0))
        display.flip()
        






def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified = True
        cond.notify()





if __name__ == '__main__':

    # cond = threading.Condition()
    # notified = False
    #
    # NetworkTables.initialize(server='10.49.3.2')
    # NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
    #
    # with cond:
    #     print("Waiting")
    #     if not notified:
    #         cond.wait()
    #table = NetworkTables.getTable('Grid')
    table=0

    gui=GUI(table)
    while gui.running:
        gui.run()


