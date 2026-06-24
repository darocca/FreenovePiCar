if [ -d /FreenovePiCar ]; then
  sudo rm /FreenovePiCar -rf
fi

sudo mv ./FreenovePiCar /
echo 'export PYTHONPATH="/FreenovePiCar/Code/Server:${PYTHONPATH}"' >> ~/.bashrc
source ~/.bashrc

cp /FreenovePiCar/samples ~ -r

sudo python /FreenovePiCar/Code/setup.py

# ir setup
sudo echo "dtoverlay=gpio-ir,gpio=16" >> /boot/firmware/config.txt
sudo echo "ir-keytable -p all" >> /etc/rc.local


sudo raspi-config nonint do_i2c 0
echo "you will need to reboot to enable i2c"