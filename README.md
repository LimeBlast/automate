# Automate

Using Amazon Dash buttons to control Sonos speakers

### Installing

This is designed to be run on a Raspberry Pi 2 (or greater) running Raspbian. It has been tested using Raspbian installed via NOOBs 2.3.0, but may well work for other operating systems.

After the usual set-up of Raspbian, you'll need to install libpcap-dev and tcpdump.

```bash
sudo apt-get install libpcap-dev
sudo apt-get install tcpdump
```

Then you can clone the repo:

```
mkdir ~/Code/
cd ~/Code/
git clone git@github.com:LimeBlast/automate.git
```

And install the required packages (for both npm and pip):

```
cd automate/
npm install
pip3 install -r requirements.txt
```

Before testing it works by manually running the script:

wip

## Start on boot

wip

## Authors

* **Daniel Hollands** - *Initial work* - [LimeBlast](https://github.com/LimeBlast)
* **SoCo Team** - *SoCo* - [SoCo](https://github.com/orgs/SoCo/people)
