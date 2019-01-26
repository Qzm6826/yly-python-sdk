<h1 align="center">yly-python-sdk</h1>
<p align="center">


# Requirement  
```
python >= 2.7 
```

# Installation  
```shell
pip install yly-python-sdk
```

# Usage or Instructions
 1. 接口类Lib/Api/yly_*.py，集成了所有的易联云接口
 2. 配置类Lib/Config/config.py
 3. 授权类Lib/Oauth/oauth.py，获取调用凭证AccessToken，每日上限次数２０次，２４小时后更新次数
 4. 接口调用类Lib/Protocol/rpc_client.py，包括了md5工具函数，Sign工具函数，uuid函数，可以直接用这个类直接进行接口调用
 5. 若觉的好用，大佬们请在<a href= 'https://github.com/Qzm6826/yly-python-sdk'>GitHub</a>上给子陌一个Star，在此子陌先感谢各位大佬，抱拳！子陌也会时长更新接口的，为大佬们提供方便！  

#### 第一步 安装sdk包 sudo pip install yly-python-sdk 并且引入模块
```python
from Lib.Config.config import Config
from Lib.Oauth.oauth import Oauth
from Lib.Protocol.rpc_client import RpcClient
```

#### 第二步 实例化config对象，实例化一个oauth2.0客户端授权模式的授权对象  
```python
config = Config('应用id', '应用密钥')
oauth_client = Oauth(config)
```
#### 第三️步 获取token对象,此步获取到的token对象可在有效期内一直使用，不用每次调用前都去获取一次，建议应用授权一次后存放到全局缓存中，开放型应用请在get_token('code')中传入授权码code!!!
```python
token_data = oauth_client.get_token()
access_token = token_data['body']['access_token']
```
#### 第四步 实例化远程调用的client对象
```python
rpc_client = RpcClient(config, access_token)
```
#### 第五步 实例化一个Api对象，调用api方法，获取资源数据
```python
print_service = YlyPrint(rpcClient)
print_service.index('机器码', '打印内容', '商户系统内部订单号，要求32个字符内，只能是数字、大小写字母')
```
