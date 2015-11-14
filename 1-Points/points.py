

'''
,x=0,y=0,directions='>>><<<~>>>~^^^'
'''
class Coordinates(object):
    def __init__(self):
        self.x,self.y=input('Starting point: ')[1:4:2]
        self.x=int(self.x)
        self.y=int(self.y)
        self.directions=input('Directions: ')
        self.forw={">":1,"<":-1,"^":-1,"v":1}
        self.rev={">":-1,"<":1,"^":1,"v":-1}
        self.vect=self.forw
    def position(self):
        for i in self.directions:
            if i in ("<",">"):
                self.x+=self.vect[i]
            elif i in ("^","v"):
                self.y+=self.vect[i]
            else:
                if self.vect==self.forw:
                    self.vect=self.rev
                else:
                    self.vect=self.forw
        print(self.x,self.y)
a=Coordinates()
a.position()

