stack=[]
def push(stack,i):
	x=len(stack)-1
	if x==-1:
		stack.append(i)
	else:	
		stack.append(0)
		while x>=0:
			stack[x+1]=stack[x]
			x-=1
		stack[0]=i
	print stack
	
def pop(stack):
	if len(stack)==0:
		print "Underflow!!"
	else:
		for i in range(len(stack)-1):
			stack[i]=stack[i+1]
		del stack[len(stack)-1]
		print stack

def disp(stack):
	#print "fn reached"
	if len(stack)==0:
		print "Stack Empty"
	else:
		for i in range(len(stack)):
			if i==0:
				print "-->",
			print stack[i]
ch=0
while ch!=4:
	ch=int(raw_input("1.Push\n2.Pop\n3.Display\n4.Exit\nEnter choice:"))
	if ch==1:
		push(stack,raw_input("Enter new element:"))
	elif ch==2:
		pop(stack)
	elif ch==3:
		disp(stack)
	else:
		break
	print "\n"
