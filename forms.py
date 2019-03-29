from wtforms  import Form, TextField, TextAreaField, SubmitField, SelectField, SelectMultipleField
 
class ContactForm(Form):
       name = TextField("Name")
       email = TextField("Email")
       subject = TextField("Subject")
       message = TextAreaField("Message")
       submit = SubmitField("Send")
       #secgroups = SelectMultipleField( 'SecGroups',choices=[('sg-5dfea124', 'sg-5dfea124'), ('sg-d3c39caa', 'sg-d3c39caa'), ('text', 'Plain Text')] )
       protocols = SelectField( 'Protocols',choices=[('tcp','tcp'), ('udp', 'udp'), ('all', 'all')] )
       cidr = TextField("CIDR")
       with open ("list.txt", "r") as myfile:
                           data=myfile.readlines()
                           print(data)
       #f = open("list.txt")
       #lines = f.readlines()
       #lines = line.replace(" ", "\n")
       with open("list.txt") as f:
               lines = f.read().splitlines()
               print("lines are" ,lines)
               secgroups = SelectMultipleField('SecGroups',choices=[lines])
