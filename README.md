# Automate

Using Amazon Dash buttons to control Sonos speakers

### Installing

This is designed to be run on a Raspberry Pi 2 (or greater) running Raspbian. It has been tested using Raspbian installed via NOOBs 2.3.0, but may well work for other operating systems.

After the usual set-up of Raspbian, you'll need to install libpcap-dev, npm and node, and update the latter two to more recent versions ([these instructions courtesy Dasher](https://github.com/maddox/dasher#raspberry-pi)):

```bash
sudo apt-get install libpcap-dev

sudo apt-get install npm
sudo apt-get install node

wget http://node-arm.herokuapp.com/node_latest_armhf.deb
sudo dpkg -i node_latest_armhf.deb
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

```
sudo npm start
```

## Start on boot

Add additional notes about how to deploy this on a live system

## Authors

* **Daniel Hollands** - *Initial work* - [LimeBlast](https://github.com/LimeBlast)
* **Alex Hortin** - *node-dash-button* - [hortinstein](https://github.com/hortinstein)
* **SoCo Team** - *SoCo* - [SoCo](https://github.com/orgs/SoCo/people)
