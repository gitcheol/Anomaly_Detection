import cv2
import numpy as np
import glob
import shutil
import os



def save_video(video_path,frame_num):
	#Open the Video file
	cap=cv2.VideoCapture(video_path)

	#Get the Frame number and extract Frames
	i=0
	#we can get the frame number by using the I variable.
	time=30*3
	#make the output folder
	os.makedirs("./temp_img")

	while(cap.isOpened()):
		ret,frame=cap.read()
		if ret == False:
			break
		if i >= frame_num-time and i<=frame_num+time:
			cv2.imwrite('./temp_img/R'+str(i).zfill(13)+'.jpg',frame)
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

	out=cv2.VideoWriter('./result/Extracted_Video.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,size)

	for i in range(len(img_array)):
		out.write(img_array[i])
	out.release()

	#remove the outpit folder && Image files in output folder 
	shutil.rmtree(r"./temp_img")

