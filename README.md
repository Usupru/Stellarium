<h1>🛰️ Stellarium</h1>

This project connects the open-source digital planetarium software <b>Stellarium</b>, with an Arduino microcontroller, responsible
of afterwards controlling the dome. The microcontroller receives the azimuth and altitude of the selected object in Stellarium.

This program was written to act as an interface between a computer running Stellarium with its web interface open, and the Arduino
microcontroller responsible of controlling my school's dome. However, this program can be used in any enviroment as long as the host
has Stellarium with its remote control plugin enabled.

<h2>📦 Installation</h2>

<h3>Make sure you have Python 3.8+ and git installed on your system.</h3>

First, clone the repository:
````
git clone https://github.com/Usupru/Stellarium.git
cd Stellarium
````

(Optional but recommended) Create and activate a virtual environment:
````
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
````

Install dependencies:

Windows
````
pip install requests
pip install pybluez
````

Linux
````
sudo apt install bluetooth libbluetooth-dev
pip3 install pybluez
pip3 install requests
````

<h3>⚙️ Usage</h3>

Simply run controller.py and follow futher instructions prompted in the terminal.

<h3>⚠️ Known issues</h3>

This project utilizes the <b>Pybluez</b> python module to communicate with the bluetooth device, up to this date Pybluez has many issues
concerning installation and compatiblity with newer Windows OS systems. Therefore, it is adviced to use this program only on Linux machines
to avoid any problems. If you still decide to use Windows and have no will to live, be aware that Pybluez can only be used up Python 3.9 in Windows OS.
