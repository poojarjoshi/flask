import subprocess
subprocess.run(['aws', 'ec2', 'authorize-security-group-ingress', '--group-id', 'sg-5dfea124', '--protocol', 'tcp' ,'--port','443', '--cidr','203.0.113.0/25'])
