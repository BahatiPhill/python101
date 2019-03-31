import smtplib


def send_email(host, subject, to_addr, from_addr, body_text):
    '''
    send mail
    '''

    BODY = "\r\n".join((
        'From: %s' %from_addr,
        'To: %s' %to_addr,
        'Subject: %s' %subject,
        "",
        body_text
        ))

    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], BODY)
    server.quit()


if __name__ == '__main__':

    HOST = 'MYSMTP.server.com'
    SUBJECT = 'Test mail from Python SMTPLIB'
    TO = "addres@address.address"
    FROM = 'sender@sender.sender'
    TEXT = 'Still got long way to Go!'


    send_email(HOST, SUBJECT, TO, FROM, TEXT)