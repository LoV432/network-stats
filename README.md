### Installing

Frist turn on network logging from OpenWRT

```
https://openwrt.org/docs/guide-user/base-system/log.essentials#network_logging
```
(Also make sure DNS Log queries is on in OpenWRT)

Then run this on your host device

```
ncat -u -4 -l 5555 >> logs.txt 2>&1
```

Then you need to install python and install matplotlib on python

```
https://www.python.org/downloads/
```

```
pip install matplotlib
```

Finally use this to run the server

```
python -m http.server --cgi 8080
```