# 300英雄宅基地自动完成每日任务

token填写到config.yaml中

## 获取token的方法

1. 手机抓包（推荐，但或许需要root权限）
   这里使用了HttpCanary，点击左上角选择目标应用中选择宅基地，右下角开启抓包后打开宅基地即可抓包

   ![image.png](assets/HttpCanary01.png)

   随便选个贴子，点个赞，然后回到这里使用了HttpCanary，选择刚刚点赞抓到的包，预览，找到token

   ![36ed38cb024d2c3d22b63a10248170a8_720.jpg](assets/HttpCanary02.png)
2. PC浏览器抓包（会与手机宅基地相互挤号，因此不推荐，作为方法1无法使用时的下位）
   进入[http://300zjdclient.tygms.cn/]
   使用手机验证码登录
   ![img.png](assets/img.png)
   然后按f12，依次点击“应用”，“本地存储空间”，找到ClientToken，复制value（注意，不需要双引号）
   ![img_1.png](assets/img_1.png)
