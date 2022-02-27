# Mailing for Ukraine

To do something good -> send some emails to Russian people and let them know what happens in Ukraine.
Feel free to use any emails you have, and send people the real images from Ukraine.

## Configuration
1. Prepare google account
2. Follow IMAP enable part of  https://support.google.com/mail/?p=BadCredentials
3. Authorize access of less secure apps https://kb.synology.com/en-global/SRM/tutorial/How_to_use_Gmail_SMTP_server_to_send_emails_for_SRM
4. Paste emails list to mails.txt
5. Paste your credendials, and emails address to send messages

Run with `python send_mails.py`

By default script sends random message from MESSAGES list, but you can uncomment part that gets the arg in send mail, and then use `python send_mails.py <message_short_name>`
