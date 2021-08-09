import smtplib as s 
#smtplib is an inbuilt library in python, No need to install it.

ob=s.SMTP('smtp.gmail.com',587) 
#ob is a variable= s is the SMTP library, mail address, port number
ob.starttls()
ob.login("shrutigoyal1201@gmail.com","dbsymbdvlzoykcre")
subject="Email Sending Functionality using Python"
body="This is a mail to check the SMTP mail transfer!"
message ="Subject:{}\n\n{}".format(subject,body)
listofaddress=["shivadantare@gmail.com ","rashishrivastava16@gmail.com","shrutigoyal1201@gmail.com","shrutipui@gmail.com"]
ob.sendmail("shrutigoyal1201@gmail.com",listofaddress,message)
print("Mail sent successfully!")
ob.quit()

# PORT NUMBER- 587
# When an email client or outgoing server is submitting an email to be routed by a proper mail server, 
# it should always use SMTP port 587 as the default port. This port, coupled with TLS encryption,
# will ensure that email is submitted securely and following the guidelines set out by the IETF.

# (TLS) -Transport Layer Security 
# TLS is a protocol that encrypts and delivers mail securely, 
# for both inbound and outbound mail traffic. 
# It helps prevent eavesdropping between mail servers keeping your messages private while they're moving between email providers.
# TLS is being adopted as the standard for secure email.

