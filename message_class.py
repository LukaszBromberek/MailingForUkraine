import imp
from typing import List
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

class Message:
    def __init__(self, subject : str, short_name : str) -> None:
        self.short_name : str = short_name
        self.message : MIMEMultipart = MIMEMultipart()
        self.message['Subject'] = subject
        
    def add_text(self, text : str) -> None:
        self.message.attach(MIMEText(text))
        
    def add_image(self, image_file_path : str) -> None:
        if(os.path.exists(image_file_path)):
            image = open(image_file_path, 'rb').read()
            self.message.attach(MIMEImage(image, 
                        name=os.path.basename(image_file_path)))
        else:
            raise FileNotFoundError(f"File {os.path.basename(image_file_path)} not found.")
        