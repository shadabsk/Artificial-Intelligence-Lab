__author__ = 'Shadab Shaikh'
__title__ = 'Implementation of A* Search algorithm'
__date__ = '13-08-2019'
__version__ = '3.0'
__availability__ = 'https://github.com/shadabsk'

print('Author		: ' + __author__)
print('Title		: ' + __title__)
print('Date		: ' + __date__)
print('Version		: ' + __version__)
print('Availability	: ' + __availability__)



import itertools						#for flattening a 2d list


def astarsearch(unique_heuristic,openlist,pathlist,weight,treearr,X,childtree,gn,goal):
	'''Implementation of A* Search algorithm'''
	olist=[]							#will store the next traversal element
	for i in range(len(pathlist)):
		olist.append(pathlist[i][-1])	#storing next traversal
	for i in range(len(olist)):
		calculatefn(unique_heuristic,X,weight,olist[i],pathlist[i],gn,0)	#calling to calculate fn

	pathfn.sort()						#sorting on the basis of resultant addition value
	curweig=""							#previous weight for gn
	curpath=[]							#wll store the current path
	openlist=[]							#opening of current path list

	for i in pathfn[0]:
		if i.isnumeric():
			curweig+=i 					#seperating number from path traversed
		if i.isalpha() or i=='-':
			curpath.append(i)			#seperating alphabet
	
	for i in range(len(childtree)):
		if(childtree[i][0]==curpath[2]):
			openlist.append(childtree[i][1:])			#new open list with new traversed child element
	openlist=list(itertools.chain(*openlist))			#flattening the list
	curpaths=''							#for joining of new path

	X=curpath[-1]						#updated value of X for next iteration
	print("\n\n\nPATH {} is selected	".format(curpaths.join(curpath)))	#printing the path iteration'''				
	
	for x in range(len(weight)):
		if(weight[x][0]==curpath[0] and weight[x][5]==curpath[2]):
			gn=int(weight[x][9])			#updating gn if previous traversed
	
	print("\nOPEN {}	".format(openlist))	#printing the open path iteration'''

	pathlist=[]								#reinitializing with empty open list
	for i in range(len(openlist)):
		pathlist.append(root+"-"+curpath[2]+"-"+openlist[i])	#creating new traversed path list

	
	pathfn.pop(0)							#removing the resultant open path list

	try:
		if(len(pathfn)>=0):					#if pathfn has any element calling recursively
			astarsearch(unique_heuristic,openlist,pathlist,weight,treearr,X,childtree,gn,goal)
	except IndexError:
		optimized_solution=[]						#will store the final result
		print('\n')
		print('Solutions obtained are	')
		for i in finalanswer:
			for j in i:
				if j==goal:
					optimized_solution.append(i)	#storing in list to compute best solution
					print(i)						#printing the goal traversal result

		numbercompare=[]							#will store index of best solution

		try:
			for i in range(len(optimized_solution)):
				for j in range(len(optimized_solution[i])):
					if optimized_solution[i][j].isnumeric():
						numbercompare.append(int(optimized_solution[i][j:]))	#getting the number from list
		except:
			pass

		numbercompare.pop(-1)						#if found any 0 for non two digit removal
		
		optimized_index=numbercompare.index(min(numbercompare))					#getting the list of best solution

		print('\n\nThe best solution is	')
		print(optimized_solution[optimized_index])								#printing the best solution


def calculatefn(unique_heuristic,X,weight,oelem,pathlistelem,gn,hn):
	''' Function to calculate f(n)=g(n)+h(n)'''
	fn=0
	for i in range(len(unique_heuristic)):
		if(oelem==unique_heuristic[i][0]):
			hn=unique_heuristic[i][4]				#if found any oelem from heuristic list appending value to hn

	for j in range(len(weight)):
		if (X==weight[j][0] and weight[j][5]=="-"):
			gn=0									#for the intitial case of computing root's fn
		elif(X==weight[j][0] and weight[j][5]==oelem):
			gn+=int(weight[j][9])					#for the following iteration case


	fn=int(gn)+int(hn)								#applying a* formula
	print("\n\n("+str(pathlistelem)+")f = "+" g(n) = "+str(gn)+" + h(n) = "+str(hn)+" => "+str(fn))		#printing the resultant iteration
	finalanswer.append("("+str(pathlistelem)+")f => "+str(fn))	#storing for best and optimized solution computation
	if(gn!=0 and hn!=0):
		pathfn.append(str(fn)+str(pathlistelem))	#updating pathfn for making the stack list

	


def createTree(treearr, treelength):
	'''Creating a child's child tree'''
	try:
		for i in range(treelength):
			childtree[i].append(treearr[i+1])		#appending the child of root tree
			checkchild=input("\n Does "+treearr[i+1][0]+" has any child node Press n for no :	")	#asking for child's child
			if(checkchild=='n'):
				print()
			else:
				checkchildsibling=""
				while(checkchildsibling!='n'):
					childname=input("\n Enter child node :	")				#asking for siblings
					childtree[i].append(childname)							#storing into child tree
					weightval=input("Enter weight value from "+str(childtree[i][0])+" to "+childname+" :	")			#asking weight value for internal nodes
					weight.append(childtree[i][0]+" -> "+childname+" = "+weightval)
					heurval=input("Enter heuristic value of "+childname+" :	")	#asking heuristic value for root
					heuristic.append(childname+" = "+heurval)
					checkchildsibling = input("\n Does "+treearr[i+1][0]+" has any other children Press n for no :	")
	except IndexError:
		pass


treearr=[]										#stores the root and its child
heuristic=[]									#stores the heuristic values
weight=[]										#stores the weight values
root=""											#stores root
root=input("Enter the root node :	")			#asking the root node
weight.append(root+" -> "+"-"+" = "+str(0))		#appending to weight list and root value to 0
heurval=input("Enter heuristic value of "+root+" :	")	#asking heuristic value for root
heuristic.append(root+" = "+heurval)			#appending to heuristic list with root value

treearr.append(root)							#appending in root tree 

checkchild=input("\n Does "+root+" has any child node Press n for no :	")	#asking if it has any child
if(checkchild=='n'):
	print(treearr)															#if not then simply printing it
else:
	checkchildsibling=""
	while(checkchildsibling!='n'):											
		childname=input("\n Enter child node :	")							#Asking the child node name
		weightval=input("Enter weight value from "+root+" to "+childname+" :	")						#asking heuristic value for root
		treearr.append(childname)
		weight.append(root+" -> "+childname+" = "+weightval)											#appending to root tree
		heurval=input("Enter heuristic value of "+childname+" :	")			#asking heuristic value for root
		heuristic.append(childname+" = "+heurval)
		checkchildsibling = input("\nDoes "+root+" has any other child Press n for no :	") #asking for the continuity

treelength=len(treearr)						#finding the length of root tree
childtree=[[] for x in range(treelength-1)]	#creating a child tree w.r.t root child
createTree(treearr,treelength)				#calling a function for creation of child's child'''


print("\n\n Tree successfully created root node wtih children\n")
print(treearr)

print("\n\n Children with their children and siblings \n")
print(childtree)							#printing the root tree and child tree

goal=input("\n Enter the goal node :	")	#asking for goal node

heuristic_set=set(heuristic)				#getting unique element from heuristic list
unique_heuristic=(list(heuristic_set))		#typecasting set to list

for i in range(len(unique_heuristic)):
	try:
		if(goal==unique_heuristic[i][0]):
			unique_heuristic.remove(unique_heuristic[i])	#removing goal
	except IndexError:
		pass


print("\n\n The heuristic values are")
print(*unique_heuristic, sep ='\n')			#printing heuristic list

print("\n\n The Weight values are")
print(*weight, sep ='\n')					#printing weight values

X=treearr[0]								#performing 1st iteration x=root

openlist=[]									#declaration of open list
pathlist=[]									#will store the path traversed
pathfn=[]									#will store the resultant of A* computation
finalanswer=[]								#for computing best and obtained solutions

olist=[]									#new obtained open element

print("\n\n X = "+X)
calculatefn(unique_heuristic,X,weight,X,X,0,0)	#calling calculatefn for the 1st iteration

openlist.append(treearr[1:])					#appending root child into open list
openlist=list(itertools.chain(*openlist))		#flattening the list
	
print("\nOPEN {}	".format(openlist))			#printing the 1st iteration'''


for i in range(len(openlist)):
	pathlist.append(root+"-"+openlist[i])		#appending to path list

astarsearch(unique_heuristic,openlist,pathlist,weight,treearr,X,childtree,0,goal)	#calling of a* search algo






