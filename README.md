### HUAWEI TOOLS SCRIPT
***is a tool that can be used to send sms, read sms and others on the huawei modem, thanks to the api documentation made using python in my opinion it is very complicated to run, by making it using a shell script it becomes easy and only requires bash and curl to run this code.***
* Installation
  ```
  opkg update && opkg install wget
  ```
  
  ```
  opkg install libxml2 bash curl
  ```
  
  ```
  wget -O /usr/bin/ht https://raw.githubusercontent.com/ahmadqsyaa/hw-tools-script/main/ht
  ```
  
  ```
  chmod +x /usr/bin/ht
  ```
### USAGE
* `-r` get all sms or get sms with count `ht -r 1`
* `-s` send sms with the format `ht -s [number] [message]`
* `-d` deleted sms with id `ht -d 1000`
* `-c` view the conten of sms inbox, outbox, unread etc
* `-b` change the status of unread to read with id `ht -b 1`
* `-m` change mobile data `ht -m [0/1] 0 = OFF 1 = ON`
* `-ms` view the mobile data status
* `-o` reboot the modem
* `-i` network information & modem information
* `-a` renew wan ip address
### TESTED
* e5577
* e3372
### REPOSITORY LIST
* [**source copas**](https://github.com/Haris131/e3372)
* [**documentasi api**](https://github.com/Salamek/huawei-lte-api)
* [**inspired by**](https://github.com/satriakanda/mmsms)
### CONTACT
* [**telegram**](https://t.me/rickk1kch)
* [**email**](mailto:itsme@rick.biz.id)
