跳板机
ssh -p 52015 team27@124.16.75.116
mUFtIr3BJuNXs7zMv#M(

主机IP
10.200.79.55
wslIP
172.31.25.1ifconfig

scp文件传送
scp armin@172.31.25.1:/home/armin/work/github/2025-spring-CTF/exam/topo/fscan <>@<>
scp armin@172.31.25.1:/home/armin/work/github/2025-spring-CTF/exam/topo/fscan team27@124.16.75.116:/home/team27


fscan爆破
./fscan -h 192.168.1.0/24 -userf ./dictionary/username- -pwdf ./dictionary/passwd-

fscan替换 .tmuxconfig


rdp连接windows服务器
ssh -L 16657:<Windows服务器IP>:3389 <ubuntu用户名>@<跳板机IP> -N
mstsc
ssh连接linux服务器
ssh 目标用户名@目标主机IP

WSL转发流量
ssh -4 -L 0.0.0.0:52000:<windows服务器IP>:<开放端口(3389)> <跳板机用户名test>@<跳板机IP> -N -f
mstsc
填<跳板机IP>:<52000> <用户名手猜>