# Text-to-Speech (T2S) Converter using Amazon Polly + Boto3 + Tkinter

*Before run project in Visual Studio Code make sure that pip3 & boto3 is installed on it.*

*Or you can use below commands to install them.*
```
sudo apt-get -y install python3-pip
```
```
pip install boto3
```

## 1. Import Python GUI Tool (Tkinter) and create a window.

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/1.%20Import%20python%20GUI%20Tool.png?raw=true)

## 2. Create a text area and insert button to read text.

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/2.%20Create%20a%20text%20area%20and%20insert%20button%20for%20run%20commands.png?raw=true)


## 3. Making Read Button Functional

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/3.%20Making%20Read%20Button%20Functional.png?raw=true)


## 4. Install & Configure your AWS CLI
	pip install awscli
	aws configure --profile iam_user
provide AccessKey, Secret Access Key, Region Name, Output Format

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/4.%20Install%20&%20Configure%20your%20AWS%20CLI.png?raw=true)


## 5. Connect your code with AWS Management Console & get response from Polly, also provide parameters for the speech (you can refer it from boto3 documentation)

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/5.%20Connect%20your%20code%20with%20AWS%20account%20and%20Polly.png?raw=true)


## 6. Import some libraries that will help us to connect with our system files and software

* import library for extract audiostream and open file, extract stream, close file

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/6.%20Importing%20some%20libraries.py.png?raw=true)
 
* Extract AudioStream and play it on media player, from response as a stream and in output you can give a path of temporary directory of speech which you brought from polly.

* *sys.platform* will understood by system module, connect output of code with win32 (windows media player) to get the speech with voice

* After running the code Windows Media Player will open and you will hear your text or message.

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/7.%20Text%20gets%20converted%20to%20Speech%20.png?raw=true)

##

![](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/2.%20Text%20to%20Speech%20Converter%20using%20Amazon%20Polly%20+%20Boto3%20+%20Tkinter/8.%20You%20can%20hear%20message%20on%20Windows%20Media%20Player.png?raw=true)

