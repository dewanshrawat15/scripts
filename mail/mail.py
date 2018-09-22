import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("dewanshrawat15@gmail.com", "477FF945de")
 
msg = "BHSDK!"
server.sendmail("dewanshrawat15@gmail.com", "dewanshrawat15@gmail.com", msg)
server.quit()