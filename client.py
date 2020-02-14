# run this program on each client to send a labelled image stream
import socket
import time

import cv2

from imutils.video import VideoStream
import imagezmq


sender = imagezmq.ImageSender(connect_to='tcp://210.119.146.213:5555')

client_name = socket.gethostname() # send client hostname with each image
# cam = VideoStream(-1).start()
cam = cv2.VideoCapture(-1)
time.sleep(2.0) # allow camera sensor to warm up

print("Start sending...")
start_time = time.time()

while True: # send images as stream until Ctrl-C
    ret, image = cam.read()
    sender.send_image(client_name, image)
    
