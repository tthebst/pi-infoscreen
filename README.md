# pi-infoscreen


## SETUP PI

Mount NAS storage to raspberry:

```
apt-get install nfs-common
sudo mount -t nfs 192.168.1.124:/volume1/raspberry-sql ~/pi-sqlto
sudo chown pi pi-sql
sudo chmod 0755 pi-sql 
```

## Running Data Collection

```
nohup python3 pi-infoscreen/roomdata-saver.py </dev/null >/dev/null 2>&1 &

```