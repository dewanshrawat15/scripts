import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("emailaddress", "pwd") # (emailID, password)

arr = ["shashankkarmakar2000@gmail.com", "dewanshrawat15@gmail.com", "dewanshrawat1501@gmail.com", "lucifer15jan@gmail.com"];

msg = "I'm a web designer at Converge Clan, which is a prestigious group of highly talented people. I've been practising my skills for quite some time. I first analyse then proceed on a problem. I've included some of my work below. I'm your best shot for any work that has to be done." #Custom Message
for x in arr:
	server.sendmail("emailaddress", x, msg)
server.quit()