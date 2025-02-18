## selenium-on-ec2
***BUYER BEWARE!!***
## Installation

```shell
# install { chromedriver, git } and create a symbolic link

sudo yum update -y

wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

sudo yum install ./google-chrome-stable_current_x86_64.rpm git -y

sudo ln -s /usr/bin/google-chrome-stable /usr/bin/chromium

# install dependencies for selenium

git clone https://github.com/doorcs/selenium-on-ec2.git

cd s[tab] # cd selenium-on-ec2/

pip3 install -r requirements.txt

# done!

python3 main.py
```
