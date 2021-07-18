A="ATGCNNGTGT"
B="ATGGCCCTTG"
C="ATGCTGCAAT"
print("\n"+A+"\n"+B+"\n"+C)

TQS=0
CT=0

for i in range(len(A)):
		CA=(A[i])
		print(type(CA))
		CB=(B[i])
		CC=(C[i])
		CL=[CA,CB,CC]
		print("\n",CL)
		CT=CT+1
		for j in CL:
			if j == "A":
				QS=32
			elif j == "T":
				QS=34
			elif j == "G":
				QS=36
			elif j == "C":
				QS=38
			else:
				QS=0
			TQS=TQS+QS
		print("Per base seq quality of base",CT,"is:",TQS)
		TQS=0

