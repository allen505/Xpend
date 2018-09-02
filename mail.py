import smtplib
import time
import imaplib
import email
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "atulmb99" + ORG_EMAIL
FROM_PWD    = "@atul_Bharadwaj"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id-1,latest_email_id-2, -1):
            typ, data = mail.fetch(str(i), '(RFC822)' ) 
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_date = msg['date']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    print('Date : '+ email_date + '\n')
                    if msg.is_multipart():
                        for payload in msg.get_payload():
                        # if payload.is_multipart(): ...
                            print(payload.get_payload())
                        #else:
                         #   print(msg.get_payload())

    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    read_email_from_gmail()