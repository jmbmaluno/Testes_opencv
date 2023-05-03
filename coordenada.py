import numpy as np

class Coordenada:
    coord1 = [0,0]
    coord2 = [0,0]
    coord3 = [0,0] 
    coord4 = [0,0]

    def __init__(self,h,w):
        self.h = h
        self.w = w
        self.coord2[1] = h
        self.coord3[0] = w
        self.coord4[0],self.coord4[1] = w,h

    
    def get_np(self):
        return np.float32([self.coord1,self.coord2,
                           self.coord3,self.coord4])
    

    def perspectiva_v_plus(self):
        if self.coord2[0] < 0:
            self.coord1[0] += 1
            self.coord3[0] -= 1
        else:
            self.coord2[0] -= 1
            self.coord4[0] += 1 
        
    def perspectiva_v_minus(self):
        if self.coord1[0] < 0:
            self.coord2[0] += 1
            self.coord4[0] -= 1 
        else:
            self.coord1[0] -= 1
            self.coord3[0] += 1

    def perspectiva_h_plus(self):
        if self.coord1[1] < 0:
            self.coord3[1] += 1
            self.coord4[1] -= 1
        else:
            self.coord1[1] -= 1
            self.coord2[1] += 1
    
    def perspectiva_h_minus(self):
        if self.coord3[1] < 0:
            self.coord1[1] += 1
            self.coord2[1] -= 1
        else:
            self.coord3[1] -= 1
            self.coord4[1] += 1
    
    def inclinacao_h_plus(self):
        self.coord1[0] += 1
        self.coord3[0] += 1
        self.coord2[0] -= 1
        self.coord4[0] -= 1
    
    def inclinacao_h_minus(self):
        self.coord1[0] -= 1
        self.coord3[0] -= 1
        self.coord2[0] += 1
        self.coord4[0] += 1
    
    def inclinacao_v_plus(self):
        self.coord1[1] += 1
        self.coord2[1] += 1
        self.coord3[1] -= 1
        self.coord4[1] -= 1

    def inclinacao_v_minus(self):
        self.coord1[1] -= 1
        self.coord2[1] -= 1
        self.coord3[1] += 1
        self.coord4[1] += 1

    def esticar_h_plus(self):
        self.coord1[0] -= 1
        self.coord2[0] -= 1
        self.coord3[0] += 1
        self.coord4[0] += 1
    
    def esticar_h_minus(self):
        self.coord1[0] += 1
        self.coord2[0] += 1
        self.coord3[0] -= 1
        self.coord4[0] -= 1
    
    def esticar_v_plus(self):
        self.coord1[1] -= 1
        self.coord2[1] += 1
        self.coord3[1] -= 1
        self.coord4[1] += 1

    def esticar_v_minus(self):
        self.coord1[1] += 1
        self.coord2[1] -= 1
        self.coord3[1] += 1
        self.coord4[1] -= 1
    
    def zoom_plus(self):
        self.coord1[0] -= 1
        self.coord1[1] -= 1

        self.coord2[0] -= 1
        self.coord2[1] += 1

        self.coord3[0] += 1
        self.coord3[1] -= 1
        
        self.coord4[0] += 1
        self.coord4[1] += 1
    
    def zoom_minus(self):
        self.coord1[0] += 1
        self.coord1[1] += 1

        self.coord2[0] += 1
        self.coord2[1] -= 1

        self.coord3[0] -= 1
        self.coord3[1] += 1
        
        self.coord4[0] -= 1
        self.coord4[1] -= 1

    def rotate_plus(self):
        self.coord1[0] += 1
        self.coord1[1] -= 1
        
        self.coord2[0] -= 1
        self.coord2[1] -= 1

        self.coord3[0] += 1
        self.coord3[1] += 1

        self.coord4[0] -= 1
        self.coord4[1] += 1
    
    def rotate_minus(self):
        self.coord1[0] -= 1
        self.coord1[1] += 1
        
        self.coord2[0] += 1
        self.coord2[1] += 1

        self.coord3[0] -= 1
        self.coord3[1] -= 1

        self.coord4[0] += 1
        self.coord4[1] -= 1

    def move_down(self):
        self.coord1[1] -= 1
        self.coord2[1] -= 1
        self.coord3[1] -= 1
        self.coord4[1] -= 1

    
    def move_up(self):
        self.coord1[1] += 1
        self.coord2[1] += 1
        self.coord3[1] += 1
        self.coord4[1] += 1

    
    def move_right(self):
        self.coord1[0] -= 1
        self.coord2[0] -= 1
        self.coord3[0] -= 1
        self.coord4[0] -= 1

    
    def move_left(self):
        self.coord1[0] += 1
        self.coord2[0] += 1
        self.coord3[0] += 1
        self.coord4[0] += 1

    def default(self):
        self.coord1 = [0,0]
        self.coord2 = [0,self.h]
        self.coord3 = [self.w,0] 
        self.coord4 = [self.w,self.h]