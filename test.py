#import subprocess
#subprocess.run(['aws', 'ec2', 'authorize-security-group-ingress', '--group-id', 'sg-5dfea124', '--protocol', 'tcp' ,'--port','443', '--cidr','203.0.113.0/25'])



import subprocess

#with open("output.txt", "wb") as f:
 #       subprocess.check_call(["python3", "test1.py"], stdout=f)

variable=subprocess.Popen(['aws', 'ec2', 'authorize-security-group-ingress', '--group-id', 'sg-5dfea124', '--protocol','tcp' ,'--port','443', '--cidr','203.0.113.0/25'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = variable.communicate()
secGroupID='sg-5dfea124'
result= "Error for %s is : %s" %(secGroupID,output)

print(result, file=open("output.html", "a"))


f = open('templates/output.html', 'r+')
f.truncate(0)
