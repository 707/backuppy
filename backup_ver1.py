import os
import time

print	'###########  FILE BACKUP SCRIPT ############# \n \n' 
print	'########### Created by Nadeem Shaik ######### \n'
print	'### source at www.github.com/707/backuppy ### \n \n '


print ' NOTE: When entering addresses, please use the full address  \n'
print ' Eg: Example on Windows: \n'
print " E:\ \File \n"
print ' Example on OSX/Linux: \n'
print ' /Users/swa/backup \n \n \n'
print	'############################################################################### \n \n' 

retry = True
while retry:

	s = raw_input("Enter the folder/file destination to back up: \n \n")

	source = list(s)

	#raw input needs to be changed to a list format vv"

	#source = ['/Users/Crysp/py']

	target_dir = raw_input("\n Enter the target backup directory ( If the file does not exist, one will be created): \n \n")

	#target_dir = '/Users/Crysp/py/backup1'
	#check if file is present else creates new directory

	if not os.path.exists(target_dir):
		os.mkdir(target_dir)

		


	#----------new additions

	today = target_dir + os.sep + time.strftime('%d%M%Y')


	now  = time.strftime('%H%M%S')


	target = today + os.sep + now + '.zip'

	if not os.path.exists(today):
		os.mkdir(today)
	#print "The back up directory was created on {0} :  \n",time.strftime() 

	print '\n \n '
	print 'Back up address is : ', target , " \n"

	zip_command = "zip -r {0} {1}".format(target, ''.join(source))

	#print 'zip command is:'

	print ' \n Executing ', zip_command, '\n'

#Backup execution

	#print "running:"

	if os.system(zip_command) == 0:

		print '\n \n'
		print	'############################################################ \n \n' 
		print "Back up completed. \n \n"
	else:
		print ' Back up not completed. \n Please check the format of the addresses or else report this at www.github.com/707/backuppy. Thank you'

	
#Asks user for another backup?
	again =  raw_input('Would you like to backup another file? (Y/N): ')
	

	if again == 'n':
		
		retry = False
		
		print 'Thank you for using!'

	elif again == 'N':
		
		retry = False
		
		print 'Thank you for using!'
	
	else:
		retry = True







