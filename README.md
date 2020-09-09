HIDPyToy - A simple tool to play with USB HID devices
====================
<img src="./docs/screenshot1a.png">

Written in Python3 with [PyQt5](https://build-system.fman.io/pyqt5-tutorial)
and built with [fbs](https://github.com/mherrmann/fbs-tutorial).

**Download**

Pre-build executables are available on the [hidpytoy releases page](https://github.com/todbot/hidpytoy/releases) for:

- [Mac OS X](https://github.com/todbot/hidpytoy/releases)
- [Windows x64](https://github.com/todbot/hidpytoy/releases)

**Requirements**

To install for development (until I get setup.py up):
```shell
git clone https://github.com/todbot/hidpytoy
cd hidpytoy
```

***Windows***
```shell
py -3.6 -m venv venv
.\venv\scripts\activate.ps1
pip install -r requirements.txt
```

***Linux***
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Running**

***Linux***
```shell
fbs run
```

Hint: If you are running this from a non root user, run instead this command
```shell
fbspath=$(whereis fbs | cut -d ":" -f2)
sudo $fbspath run
```

**Building**

fbs freeze

**UI Customisation**

***Requirements***

1. Install Qt Designer from https://build-system.fman.io/qt-designer-download
2. Save .UI file and run
```shell
pyuic5 HIDToyWindow.ui -o HIDToyWindow.py
```

If you are working from another location
```
cp ~/Desktop/HIDToyWindow.ui src/main/python/ && pyuic5 src/main/python/HIDToyWindow.ui -o src/main/python/HIDToyWindow.py
```

Be sure to check [fbs troubleshooting page](https://build-system.fman.io/troubleshooting)
