import smtplib
server=smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login("kamyarachel1303@gmail.com","Krsrrlll")
msg="hello!!!"
server.sendmail("kamyarachel1303@gmail.com","ikhlaasrasib@gmail.com",msg)
server.quit()