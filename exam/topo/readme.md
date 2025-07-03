fscan爆破
./fscan -h 192.168.1.0/24 -userf ./dictionary/username- -pwdf ./dictionary/passwd-

rdp连接windows服务器
ssh -L 16657:<Windows服务器IP>:3389 <ubuntu用户名>@<跳板机IP> -N
mstsc /v:127.0.0.1:16657

ssh连接linux服务器
ssh 目标用户名@目标主机IP