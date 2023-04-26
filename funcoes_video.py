import cv2 as cv
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


    def default(self):
        self.coord1 = [0,0]
        self.coord2 = [0,self.h]
        self.coord3 = [self.w,0] 
        self.coord4 = [self.w,self.h]
    

video_obj = cv.VideoCapture("video.mp4")
sucess, im = video_obj.read()
h,w,l = im.shape

legenda = cv.imread("legenda.png")
legenda_resized = cv.resize(legenda, None, fx=0.5, fy=0.5)

pt1 = np.float32([[0,0], [0,h], [w,0], [w,h]])

coord = Coordenada(h,w)

pt2 = coord.get_np()

while video_obj.isOpened():

    M = cv.getPerspectiveTransform(pt1, pt2)
    out = cv.warpPerspective(im, M, (w,h))

    if sucess == True:
        cv.imshow("Imagem", out)

        k = cv.waitKey(25)

        if k == ord("o"): 
            coord.perspectiva_v_plus()
        if k == ord("i"):
            coord.perspectiva_v_minus()

        if k == ord("l"):
            coord.perspectiva_h_plus()
        if k == ord("k"):
            coord.perspectiva_h_minus()

        if k == ord("u"):
            coord.inclinacao_h_plus()
        if k == ord("y"):
            coord.inclinacao_h_minus()

        if k == ord("j"):
            coord.inclinacao_v_plus()
        if k == ord("h"):
            coord.inclinacao_v_minus()

        if k == ord("t"):
            coord.esticar_h_plus()
        if k == ord("r"):
            coord.esticar_h_minus()
        
        if k == ord("g"):
            coord.esticar_v_plus()
        if k == ord("f"):
            coord.esticar_v_minus()

        if k == ord("d"):
            coord.default()

        if k == ord("w"):
            coord.zoom_plus()
        if k == ord("q"):
            coord.zoom_minus()

        if k == ord("s"):
            coord.rotate_plus()
        if k == ord("a"):
            coord.rotate_minus()
        
        pt2 = coord.get_np()

        if k == 27:
            break
    
    else:
        break
    
    sucess, im = video_obj.read()
    cv.imshow("legenda", legenda_resized)


video_obj.release()
cv.destroyAllWindows()