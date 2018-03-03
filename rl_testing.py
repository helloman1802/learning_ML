import time
import cv2
import mss
import numpy
import pyautogui as pygui

for i in range(5):
    print(i)
    time.sleep(1)

pygui.keyDown('w')
time.sleep(2)
pygui.keyUp('w')

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGRA2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return(processed_img)



with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 30, 'left': 0, 'width': 800, 'height': 600}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        screen = numpy.array(sct.grab(monitor))
        new_screen = process_img(screen)

        # Display the picture
        cv2.imshow('OpenCV/Numpy normal', new_screen)
        
        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break