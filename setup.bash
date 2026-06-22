if [ -d /FreenovePiCar ]; then
  sudo rm /FreenovePiCar -rf
fi

sudo mv ./FreenovePiCar /
echo 'export PYTHONPATH="/FreenovePiCar:${PYTHONPATH}"' >> ~/.bashrc
source ~/.bashrc

cp /FreenovePiCar/samples ~ -r

sudo python /FreenovePiCar/Code/setup.py

sudo raspi-config nonint do_i2c 0
echo "you will need to reboot to enable i2c*