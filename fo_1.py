#!/user/bin/python
fo=open("sample.fa","r")
ht=fo.readlines()
seq=[]
quality=[]
for i in range(1,len(ht),4):  # for loop to get sequence in a list
	seq.append(ht[i])
for i in range(3,len(ht),4): # for loop to get quality sequence list
	quality.append(ht[i])
length=0
for i in range(len(seq)):     # find all sequence length/toal sequences
	sequence=seq[i].replace('\t',' ').replace('\n',' ')
	tseq=(len(sequence))
	length+= len(sequence)
print("total seuqence length = ",length)
mini=[]
for i in range(len(seq)):   # minimum/maximum length of the sequence
	mini.append(len(seq[i]))
minvl=min(mini)
maxvl=max(mini)
indm=mini.index(minvl)
incm=mini.index(maxvl)
print("minimum length of the sequence: ",len(seq[indm]))
print("maximum length of the sequence: ",len(seq[incm]))

