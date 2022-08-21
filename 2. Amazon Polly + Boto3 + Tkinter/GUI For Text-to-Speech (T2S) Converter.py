# GUI For Text-to-Speech (T2S) Converter

import tkinter as tk        # python GUI tool
import boto3 
import os                   
import sys                  
from tempfile import gettempdir
from contextlib import closing

root = tk.Tk()   
root.geometry("800x500")   
root.title("T2S Converter: Amazon Polly")    
textExample = tk.Text(root,height=10)     
textExample.pack()   

def getText():
    aws_mag_console = boto3.session.Session(profile_name="your_iam_user")        
    client = aws_mag_console.client(service_name="polly", region_name='us-east-1')       
    result=textExample.get("1.0", "end")
    print(result)
    response=client.synthesize_speech(VoiceId="Joey", OutputFormat='mp3', Text=result, Engine='neural')   
    print(response)

    if "AudioStream" in response:               
        with closing(response['AudioStream']) as stream:
            output=os.path.join(gettempdir(),"speech.mp3")      
                        
            try:
                with open(output, "wb") as file:        
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)

    else:
        print("Cloud not find the stream!")
        sys.exit(-1)

    if sys.platform == 'win32':     
        os.startfile(output)

btnRead = tk.Button(root, height=1, width=20, text="Read",command= getText)
btnRead.pack()

root.mainloop()     