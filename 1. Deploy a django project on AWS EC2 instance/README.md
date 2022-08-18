
# Deploy Django App on Amazon EC2
Copy a project from GitHub and Deploy it on Amazon EC2 Instance

##  Launch an Amazon EC2 Instance

**Step 1 :** Login to your AWS Management Console

**Step 2 :** Search for Amazon EC2

**Step 3 :** Go to Instances --> Click on Launch Instances

**Step 4 :** Give a name or tag to your Instance


![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/01.%20Give%20a%20tag%20to%20your%20instance.jpg?raw=true)


**Step 5 :** Select Ubuntu Server AMI

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/02.%20Select%20Ubuntu%20Server%20AMI.png?raw=true)


**Step 6 :** Select your existing key pair or Create a new one.

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/03.%20Select%20your%20existing%20key%20or%20create%20new%20one.png?raw=true)


**Step 7 :** Create Security Group

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/04.%20Create%20a%20security%20group.png?raw=true)

**Step 8 :** Click on launch Instance

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/05.%20Click%20on%20Launch%20Instance.png?raw=true)

**Step 9 :** Go to your Instance page, refresh it  ---> You see your instance is running. 

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/06.%20Refresh%20your%20Instance%20page%20and%20your%20instance%20is%20running%20.png?raw=true)

## Connect with SSH Client (Putty) and Install Python and Django

**Step 10 :** Open your SSH client (Putty) and paste your Public IP from your Instance

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/07.%20Open%20Putty%20and%20paste%20your%20Public%20IP%20from%20Instance.png?raw=true)

**Step 11 :** Browse your ppk file (generated while creating key pair) ---> Click Open

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/08.%20Browse%20your%20ppk%20file%20and%20Click%20Open.png?raw=true)


**Step 12 :** 

Login as : ubuntu 

```
sudo apt update 
```
```
sudo apt upgrade
```
```
sudo apt-get install python3
```
```
sudo apt install pip
```
```
sudo pip install django
```
To check the versions,
```
pip --version
```
```
python3 --version
```
```
django-admin --version
```

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/09.%20Accept%20and%20Login%20as%20ubuntu.png?raw=true)

**Step 13 :** Copy your project repository url (or any other project repository url) from GitHub

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/10.%20copy%20project%20url%20from%20github.png?raw=true)

## Try to run django project on web browser 

**Step 14 :** 

Initialise Git
```
git init
```
Make clone of your remote project repository into your local repository 
```
git clone <project_url>
```
*Follow the README.md file, if any instructions are given.*

According to this project's README.md file, we have to run command

```
python3 manage.py runserver
```


![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/11.%20If%20you%20will%20see%20error%20try%20to%20resolve%20that%20error.png?raw=true)

**Step 15 :**

If you get ValueError for Incorrect Timezone Setting, go to todoApp --> settings.py

```
cd todoApp
```
```
vi settings.py
```
*Make corrections :*

ALLOWED_HOSTS = []	        --->     ALLOWED_HOSTS = ['your_public_IP']

TIME_ZONE = 'Asia/kolkata'	--->     TIME_ZONE = 'Asia/Kolkata'


```
cd ..
```

Try again:
```
python3 manage.py runserver
```


**Step 16 :** 
Now, copy your Public IP address and paste it on Chrome Web Browser.
```
http://your_public_IP:8000
```
If page is showing error, it means you have not allow port no. 8000 from EC2

**Step 17 :** Go to the security group you have created & allow 8000 port.

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/13.%20Goto%20the%20security%20group%20you%20have%20created%20&%20allow%208000%20port.png?raw=true)

**Step 18 :** 
Edit Inbound Rules and allow 8000 port


![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/14.%20Edit%20inbound%20Rules%20and%20allow%208000%20port.png?raw=true)


**Step 19 :**  Paste your Public IP address from EC2 on Chrome

```
http://<your_public_ip>:8000
```

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/15.%20now%20your%20page%20is%20visible%20and%20you%20can%20use%20that%20app%20now.png?raw=true)

Now your project will work on Chrome Browser.


**Step 20 :** Now you can terminate your Instance, if you want.

![App Screenshot](https://github.com/GIRISHBELANI/AWS-MiniProjects/blob/master/1.%20Deploy%20a%20django%20project%20on%20AWS%20EC2%20instance/16.%20You%20can%20terminate%20EC2%20instance%20If%20you%20want.png?raw=true)
