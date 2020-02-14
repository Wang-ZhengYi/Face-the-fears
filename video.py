#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	Created on Sept 2019
	
	@author
	'''

from def_import import *

fps = 60 
save_path = './videos/saveVideo0.mp4'
img_path='./figures0/'
frames = len(os.listdir(img_path))
time = frames/fps
music_start = 0

clip_top = ''
clip_bottom = ''

def veditor(clip_bottom,clip_top,fps,save_path):
	fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
	FONT_URL = fm.FontProperties(fname=fpath)
	img_list=os.listdir(img_path)
	image = Image.open('./figures/' + img_list[0])

	# audio_clip = AudioFileClip('./music/DIDIDI.mp3').subclip(music_start,music_start+time)

	background_clip1 = VideoFileClip(save_path,target_resolution=(2400,3200)).subclip(0,10)

	text_clip1 = TextClip(clip_top, fontsize = 100, color = 'black',font = FONT_URL)
	text_clip1 = text_clip1.set_position('bottom')
	text_clip1 = text_clip1.set_duration(time)
	# .set_audio(audio_clip)

	text_clip0 = TextClip(clip_bottom, fontsize = 100, color = 'black',font = FONT_URL)
	text_clip0 = text_clip0.set_position('top')
	text_clip0 = text_clip0.set_duration(time)
	# .set_audio(audio_clip)
	
	CompositeVideoClip([background_clip1,text_clip1,text_clip0]).write_videofile(save_path,codec = 'libx264', fps = fps)

def vmker(fps,save_path,img_path,frames):
	img_list=os.listdir(img_path)
	img_list.sort()
	img_list.sort(key = lambda x: int(x[3:-4]))
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	image = Image.open(img_path + img_list[0])
	videoWriter = cv2.VideoWriter(save_path,fourcc,fps,image.size)
	print(image.size)
	for i in range(frames):
	    img_name=img_path+img_list[i]
	    frame = cv2.imread(img_name)
	    videoWriter.write(frame)
	videoWriter.release()

if __name__ == '__main__':
	vmker(fps,save_path,img_path,frames)