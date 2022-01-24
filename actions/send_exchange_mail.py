import os
from st2common.runners.base_action import Action
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody, FileAttachment, Configuration, NTLM,IMPERSONATION


__all__ = [
    'SendExchangeMailAction'
]

class SendExchangeMailAction(Action):
    def run(self, userName,Server,email, emailpw, to_list, subject, message):
        try:
            credentials = Credentials(username=userName, password=emailpw)
            config = Configuration(server=Server, credentials=credentials)
            account = Account(primary_smtp_address=email, config=config,
                              autodiscover=False, access_type=DELEGATE)
            # m=None
            m = Message(
                account=account,
                subject=subject,
                body=HTMLBody(message),
                to_recipients=to_list)
            m.send()
        except Exception as e:
            raise