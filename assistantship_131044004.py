inputTable = [[5,8,7],[8,12,7],[4,8,5],[3,3,3]]
r=len(inputTable)	#number of assistant
n=len(inputTable[0]) #number of course
indexlist=[] #will hold permutations of all posible order ex: 0,2,1 or 2,1,0 etc. 
sonuc=[] #will hold result list
sum = 999999 #will hold minimum total time

#filled indexlist with indexes
for i in range(n):
	indexlist.append(i)
#added -1 for each extra assistant
for i in range(n,r):	
	indexlist.append(-1)
	
#This implementation uses the algorithm
# presented in the book Computer Algorithms by Horowitz, Sahni and Rajasekeran.
def permutation(list,length=0):
   if(length==len(list)):
      calculation(list) #calculation of time of candidate list 
   else:
      for i in range(length,len(list)):
         list[length],list[i] = list[i],list[length]
         permutation(list, length+1)
         list[length],list[i] = list[i],list[length]


		  
def calculation(lst):
	
	tempsum=0
	global sonuc
	global sum
	for k in range(r):
		if lst[k]== -1:			
			tempsum +=6 #if assitant working on other department
		else:
			tempsum += inputTable[k][lst[k]] #adding course time to total time
			
	if tempsum < sum:
		sum=tempsum
		sonuc[:]=[] #clearing old result
		for j in range(len(lst)): #copying indexes to global list
			sonuc.append(lst[j])
					
#main ---------		  
permutation(indexlist) 
print(sonuc)
print(sum)
#endo f main--------



