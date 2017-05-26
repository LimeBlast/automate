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
sudo amazon-dash --config ./amazon-dash/amazon-dash.yml run
```

## Start on boot

This script uses systemd to start on boot. I might be able to automate this at some point, but right now the following steps are required:

1. Copy `amazon-dash/amazon-dash.service` to `/etc/systemd/system/amazon-dash.service`.
2. Copy `amazon-dash/amazon-dash.yml` to  `/etc/amazon-dash.yml`.
3. Enable the service with `sudo systemctl enable amazon-dash`
4. Start the service with `sudo systemctl start amazon-dash`

If you run into any problems with this, the following command will give you the logs for the service:

```
sudo journalctl -u amazon-dash
```

## Authors

* **Daniel Hollands** - *Initial work* - [LimeBlast](https://github.com/LimeBlast)
* **SoCo Team** - *SoCo* - [SoCo](https://github.com/orgs/SoCo/people)
* **Nekmo** - *amazon-dash* - [amazon-dash](https://github.com/Nekmo/amazon-dash)
