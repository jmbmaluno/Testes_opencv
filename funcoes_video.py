import cv2 as cv
from coordenada import *

video_obj = cv.VideoCapture("v1.dav")
sucess, im = video_obj.read()
h,w,l = im.shape

legenda = cv.imread("legenda.png")
legenda_resized = cv.resize(legenda, None, fx=0.5, fy=0.5)

pt1 = np.float32([[0,0], [0,h], [w,0], [w,h]])

coord = Coordenada(h,w)

pause = False

while video_obj.isOpened():
    pt2 = coord.get_np()
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
        
        if k == ord("p"):
            pause = not(pause)
        
        if k == 53:
            coord.move_up()
                    
        if k == 50:
            print("down")
            coord.move_down()
        
        if k == 49:
            coord.move_left()
        
        if k == 51:
            coord.move_right()

        if k == 27:
            break
        
        
    
    else:
        break
    
    if not(pause):
        sucess, im = video_obj.read()

    #cv.imshow("legenda", legenda_resized)


print("COORDENADAS FINAIS DA TRANSFORMAÇÂO")
print(pt2)

video_obj.release()
cv.destroyAllWindows()