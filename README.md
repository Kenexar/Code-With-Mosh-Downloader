# Code-With-Mosh-Downloader
[![CodeFactor](https://www.codefactor.io/repository/github/kenexar/code-with-mosh-downloader/badge)](https://www.codefactor.io/repository/github/kenexar/code-with-mosh-downloader)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## ☁ Installation
#### Prerequisites
- #### Install Python Python3 (Installing Python 3 on Debian 9)
```shell
sudo apt-get update && sudo apt-get upgrade
python --version
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
curl -O https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz  
tar -xf Python-3.8.0.tar.xz  
cd Python-3.8.0
./configure --enable-optimizations
make
sudo make altinstall
python3.8 --version
```
[source of installation](https://cloudwafer.com/blog/installing-python-3-on-debian-9/)

#### ⚡ How to run
1. Clone the Repository
2. Install packages
    ```shell
    sudo pip install -r req.txt
    ```
4. Get you auth cookie:
    - go to https://codewithmosh.com
    - login in to your account
    - open https://codewithmosh.com/courses/enrolled
    - open DevTools
    - go to Network tab
    - open enrolled and then go to Header
    - copy the value of cookie:

5. Create a .env file, like in the example, and paste the cookie
    ```env
    # .env example
    AUTH_COOKIE: 
    ```
4. Last step run is to run __main__.py
    ```shell
    sudo python3 __main__.py
    ```
## License
[MIT License](https://github.com/Kenexar/Code-With-Mosh-Downloader/blob/master/LICENSE)
