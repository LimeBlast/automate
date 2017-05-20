# Automate

Using Amazon Dash buttons to automate my life.

### Installing

This is designed to be run on a Raspberry Pi 2 (or greater) running Raspbian. It has been tested using Raspbian installed via NOOBs 2.3.0, but may well work for other operating systems.

After the usual set-up of Raspbian, you'll need to install libpcap-dev, tcpdump, and python-yaml.

```bash
sudo apt-get install libpcap-dev
sudo apt-get install tcpdump
sudo apt-get install python-yaml
```

Then you can clone the repo:

```
mkdir ~/Code/
cd ~/Code/
git clone git@github.com:LimeBlast/automate.git
```

And install the required packages:

```
cd automate/
pip3 install -r requirements.txt
```

Then tests it works by manually running the script:

```
sudo amazon-dash run
```

## Start on boot

I tried a few methods of making the script run on boot, but none of them worked. In the end, I added the following line to `/etc/rc.local`, which appears to have done the job, but I'm not sure is the best approach.

```
su pi -c 'cd /home/pi/Code/automate && sudo amazon-dash run < /dev/null &'
```

## Authors

* **Daniel Hollands** - *Initial work* - [LimeBlast](https://github.com/LimeBlast)
* **SoCo Team** - *SoCo* - [SoCo](https://github.com/orgs/SoCo/people)
* **Nekmo** - *amazon-dash* - [amazon-dash]https://github.com/Nekmo/amazon-dash
