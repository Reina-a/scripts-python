import imageio
import os
image_base_path = 'out/frame'
suffix = '.jpg'

i = 0
gif_frames = []
frame_filename = image_base_path + "{:0>4d}".format(i) + suffix
while os.path.exists(frame_filename): 
    gif_frames.append(imageio.imread(frame_filename))
    i+=1
    frame_filename =  image_base_path + "{:0>4d}".format(i) + suffix

imageio.mimsave("test.gif", gif_frames, fps=20)