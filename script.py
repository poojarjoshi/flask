from flask import Flask, render_template, request, jsonify, Response
from forms import ContactForm
import subprocess,sys
import logging, platform, ctypes
app = Flask(__name__) 
 
app.secret_key = 'development key'
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  
  if request.method == 'POST':
     protocol = request.form["protocols"]
     
     as_dict = request.form.getlist('secgroups')
     #print(*as_dict)
     #as_dict.encode('ascii', 'ignore')
     for i in range (len(as_dict)):
      #print ("words[{}] = ".format(i), as_dict[i])
      #value=as_dict[i]
      #print ("value is ", value)      
     #print ("First list length : ", as_dict[])
      secGroupID=as_dict[i]
      #import subprocess
      #try:
      variable=subprocess.Popen(['aws', 'ec2', 'authorize-security-group-ingress', '--group-id', secGroupID, '--protocol', protocol ,'--port','443', '--cidr','203.0.113.0/25'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out = variable.communicate()
      rc = variable.returncode
      print("value is" ,rc)
      if rc != 0:
          print ('Error for ', secGroupID,out)
          result="error"
      else:
          print ('Success for', secGroupID)
          result="success"


      #out=variable.communicate()
    #  out,error = out1.communicate()
      #except:
       #variable=sys.exc_info()
      #print("output for ",out)     

     #return jsonify(out)
     #return render_template('contact.html', **jsonify(out))
     #return render_template('contact.html', out=out, error=error)
      #out = subprocess.check_output(['aws', 'ec2', 'authorize-security-group-ingress', '--group-id', secGroupID, '--protocol', protocol ,'--port','443', '--cidr','203.0.113.0/25'])
      
     return "contact"
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
if __name__=="__main__":
 #app.run()
 app.run(host='0.0.0.0',port='8099')
