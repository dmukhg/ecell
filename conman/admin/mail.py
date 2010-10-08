import threading
import time
from django.core.mail import send_mail, EmailMultiAlternatives

class MailThread( threading.Thread ):

    def __init__( self, mailer, mList, lag=2):
        self.lag = lag
        self.mList = mList
        self.mailer = mailer
        super(MailThread, self).__init__()

    def run( self ):
        for emailId in self.mList:
            msg = EmailMultiAlternatives(self.mailer.subject, 
                                        "",
                                        self.mailer.from_field,
                                        [emailId])
            msg.attach_alternative(self.mailer.content, 'text/html')
            #print "ello"
            msg.send()
            time.sleep(self.lag)


if __name__ == "__main__":
    MailThread(1).start()

