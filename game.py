class Game:
    
    def __init__(self,list,zero_pos,action="Initial",parent = "None", cost = 0):
        self.list = list
        self.zero_pos = zero_pos
        self.children = []
        self.cost = cost
        self.parent = parent
        self.action = action
                
    def up(self):
        if self.zero_pos >= 3:
            a = self.zero_pos - 3
            list1 = self.move(a) #move the tiles
            return Game(list1, a,"Up",self,self.cost + 1)
        else:
            return None
        
    def down(self):
        if self.zero_pos <=5:
            a = self.zero_pos + 3
            list1 = self.move(a) 
            return Game(list1, a, "Down", self,self.cost + 1)

        else:
            return None
        
    def right(self):
        if (self.zero_pos % 3 == 2):
            return None
        else:
            a = self.zero_pos + 1
            list1 = self.move(a)
            return Game(list1, a, "Right", self, self.cost + 1)
        
    def left(self):
        if (self.zero_pos % 3 == 0):
            return None
        else:
            a = self.zero_pos - 1
            list1 = self.move(a)
            return Game(list1, a, "Left",self, self.cost + 1)
        
    def move(self,num_pos):
        copy = self.list[:]
        temp = copy[self.zero_pos]
        copy[self.zero_pos] = copy[num_pos]
        copy[num_pos] = temp
        return copy
    
    def expand(self):
        """expand the node"""
        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.up()
            if up_child is not None:
                self.children.append(up_child)

            down_child = self.down()
            if down_child is not None:
                self.children.append(down_child)

            left_child = self.left()
            if left_child is not None:
                self.children.append(left_child)

            right_child = self.right()
            if right_child is not None:
                self.children.append(right_child)

        return self.children
        
		