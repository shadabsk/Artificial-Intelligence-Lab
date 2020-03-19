__author__ = 'Shadab Shaikh'
__title__ = 'Implementation of Uninformed Search Technique (BFS Algorithm)'
__date__ = '31-07-2019'
__version__ = '1.0'

print('Author		: ' + __author__)
print('Title		: ' + __title__)
print('Date		: ' + __date__)
print('Version		: ' + __version__)


import itertools						#for flattening a 2d list

def bfsalgo(childtree, openlist, closelist,goal):
	'''Implementation of BFS algo'''
	X=openlist[0]		#X=open list 1st element
	print("\n\n X = {}".format(X))	#printing X
	closelist.append(X)	#appending x to close list
	for i in range(len(childtree)):

		if(X==childtree[i][0]):		
			openlist.append(childtree[i][1:])	#if X matches the childtree node appending its sibling to open list (in rear end)

	openlist=list(itertools.chain(*openlist))	#flattening the list
	del openlist[0]			#removing 1st element of open list

	if(X!=goal):			#for the case when goal is reached not printing the open and close list
		print("\n OPEN {}	CLOSE {}".format(openlist,closelist))	#printing the iterations of open and close list

	if(X==goal):			#when goal is found printing succes
		print('\n SUCCESS')
	elif(len(openlist)>0):	#if openlist has some element recursively calling it
		bfsalgo(childtree, openlist, closelist,goal)
	else:					#else printing failure
		print('\n\n FAILURE')



def createTree(treearr, treelength):
	'''Creating a child's child tree'''
	try:
		for i in range(treelength):
			childtree[i].append(treearr[i+1])		#appending the child of root tree
			checkchild=input("\n Does "+treearr[i+1]+" has any child node Press n for no :	")	#asking for child's child
			if(checkchild=='n'):
				print()
			else:
				checkchildsibling=""
				while(checkchildsibling!='n'):
					childname=input("\n Enter child node :	")				#asking for siblings
					childtree[i].append(childname)							#storing into child tree
					checkchildsibling = input("\n Does "+treearr[i+1]+" has any other children Press n for no :	")
	except IndexError:
		pass

treearr=[]										#stores the root and its child
root=input("Enter the root node :	")			#asking the root node

treearr.append(root)							#appending in root tree 

checkchild=input("\n Does "+root+" has any child node Press n for no :	")	#asking if it has any child
if(checkchild=='n'):
	print(treearr)															#if not then simply printing it
else:
	checkchildsibling=""
	while(checkchildsibling!='n'):											
		childname=input("\n Enter child node :	")							#Asking the child node name
		treearr.append(childname)											#appending to root tree
		checkchildsibling = input("\nDoes "+root+" has any other child Press n for no :	") #asking for the continuity

treelength=len(treearr)						#finding the length of root tree
childtree=[[] for x in range(treelength-1)]	#creating a child tree w.r.t root child
createTree(treearr,treelength)				#calling a function for creation of child's child

print("\n\n Tree successfully created root node wtih children\n")
print(treearr)

print("\n\n Children with their children and siblings \n")
print(childtree)							#printing the root tree and child tree

goal=input("\n Enter the goal node :	")	#asking for goal node

openlist=[]
closelist=[]


X=treearr[0]							#performing 1st iteration x=root
print("\n\n X = "+X)

openlist.append(treearr[1:])			#appending root child into open list
openlist=list(itertools.chain(*openlist))	#flattening the list
closelist.append(X)						#appending root to close list
	
print("\nOPEN {}	CLOSE {}".format(openlist,closelist))	#printing the 1st iteration


bfsalgo(childtree,openlist,closelist,goal)	#calling the bfs algorithm
