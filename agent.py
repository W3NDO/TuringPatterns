import random

class Agent:
    def __init__(self, x, y):
        self.front_x = x
        self.front_y = y

    def propagate(self):
        self.random = random.randint(0,4)
        if self.random== 0:
            if self.front_x+3 > 720:
                self.front_x -= 3
            else:
                self.front_x +=3
        elif self.random== 1:
            if self.front_x-3 < 0:
                self.front_x += 3
            else:
                self.front_x -=3
        elif self.random== 2:
            if self.front_y+3 > 400:
                self.front_y -= 3
            else:
                self.front_y +=3
        elif self.random== 3:
            if self.front_y-3 < 0:
                self.front_y += 3
            else:
                self.front_y -=3

    def get_front(self):
        return self.front_x, self.front_y


class Activator(Agent): #subclass the agent. 
    def __init__(self, x, y):
        super().__init__(x, y)
        self.active = True

    def propagate(self):
        if self.active:
            self.random = random.randint(0,5)
            if self.random== 0:
                if self.front_x+3 > 720:
                    self.front_x -= 3
                else:
                    self.front_x +=3
            elif self.random== 1:
                if self.front_x-3 < 0:
                    self.front_x += 3
                else:
                    self.front_x -=3
            elif self.random== 2:
                if self.front_y+3 > 400:
                    self.front_y -= 3
                else:
                    self.front_y +=3
            elif self.random== 3:
                if self.front_y-3 < 0:
                    self.front_y += 3
                else:
                    self.front_y -=3
            elif self.random== 4:
                self.front_x = self.front_x
                self.front_y = self.front_y

class Inhibitor(Agent): #subclass the agent
    def __init__(self, x, y):
        super().__init__(x, y)