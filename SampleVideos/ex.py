import numpy as np
	
f=open("/Users/gicheol/Downloads/lab/AnomalyDetectionCVPR2018/SampleVideos/Explosion025_x264.txt",'r')
words = f.read().split()
num_feat = len(words) / 4096
print(len(words))
print(type(words))

X=np.array(words)
print(X.shape)

for i in range(0,10):
	print(words[i], end=' ')

print(num_feat)



