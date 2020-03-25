f=open("/Users/gicheol/Downloads/lab/AnomalyDetectionCVPR2018/SampleVideos/Explosion025_x264.txt",'r')
#1줄 출력
line = f.readline()

print(type(line))
print(line)
line=line.split()

for i in range(0,10):
	print(line[i], end='	')

'''
print(len(line[0][1]))
for i in range(len(line[1])):
	print(line[1][i],end=' ')
'''
print(type(line))
print(len(line))

f.close()
