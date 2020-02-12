f=open("/Users/gicheol/Downloads/lab/AnomalyDetectionCVPR2018/SampleVideos/Explosion008_x264.txt",'r')
line = f.readline()

line=line.split()

print(type(line))
print(len(line))

f.close()
