import threading
import time
from django.core.mail import send_mail, EmailMultiAlternatives

class MailThread( threading.Thread ):

    def __init__( self, mailer, f, lag=2):
        self.lag = lag
        self.f = f 
        self.mailer = mailer
        super(MailThread, self).__init__()

    def run( self ):
        email = ""
        number_of_emails = 0
        f = open('conman/admin/mailLists/'+self.f+'.csv') 
        for char in f.read():
            if char not in (',', ' ', '\'', '\"'):
                email += char
            else:
                if email is not "":
                    msg = EmailMultiAlternatives(self.mailer.subject, 
                                                 "",
                                                 self.mailer.from_field,
                                                 [email])
                    msg.attach_alternative(self.mailer.content, 'text/html')
                    print email 
                    #msg.send()
                    time.sleep(self.lag)
                email = ""
                number_of_emails += 1
        print number_of_emails


if __name__ == "__main__":
    MailThread(None, '3', 0.001).start()

