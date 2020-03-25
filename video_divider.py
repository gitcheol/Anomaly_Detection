import cv2
import numpy as np
import glob
import shutil
import os



def divide_video(video_path):
	#Open the Video file
	cap=cv2.VideoCapture(video_path)

	#Get the Frame number and extract Frames
	i=0
	#make the output folder
	temp_img="./temp_img"
	result_video='./divided_video'
	if not os.path.isdir(temp_img):
		os.mkdir(temp_img)	
	if not os.path.isdir(result_video):
		os.mkdir(result_video)
	
	Total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	#print(Total_frames)	
	while(cap.isOpened()):
		ret,frame=cap.read()
		if ret == False:
			break
		cv2.imwrite('./temp_img/R'+str(i).zfill(10)+'.jpg',frame)
		i+=1

	#print("frame num : " + str(i))
	cap.release()
	cv2.destroyAllWindows()

	#Making the Video from Images 

	img_array=[]
	for filename in sorted(glob.glob('./temp_img/*.jpg')):
		img=cv2.imread(filename)
		height,width,layers=img.shape
		size=(width,height)
		#print('aasdsd : '+ type(size))
		img_array.append(img)
	##print(len(img_array)//32)
	out=[]
	for i in range(32):
		out.append(cv2.VideoWriter(result_video+'/videoSegments'+str(i+1)+'.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,size))
	for i in range(32):
		for j in range(len(img_array)//32):
			out[i].write(img_array[j+i*(len(img_array)//32)])
	
	for i in range(32):	
		out[i].release()

	#remove the outpit folder && Image files in output folder 
	shutil.rmtree(r"./temp_img")


divide_video('/Users/gicheol/Downloads/lab/experiments/Example.mp4')
