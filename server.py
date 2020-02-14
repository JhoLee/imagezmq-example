# run this program on the Mac to display image streams from multiple RPis
import cv2
import imagezmq
image_hub = imagezmq.ImageHub()

print("Start waiting...")

client_list = []

while True:  # show streamed images until Ctrl-C
    client_name, image = image_hub.recv_image()

    if client_name not in client_list:
        print("New Client!! '{}'".format(client_name))
        client_list.append(client_name)

    cv2.imshow(client_name, image) # 1 window for each client
    cv2.waitkey(1)
    image_hub.send_reply(b'OK')

