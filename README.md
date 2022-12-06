# 集成 NewKeeper

本 Demo 演示如何从 `NewKeeper` 请求视频资源的密钥。

## 简述
- 申请 `app_key` 和 `app_secret`
- 创建 `NEW` 钱包，使用该钱包 `Mint` EVT.(目前由 EVT-Core mint evt 到指定地址)
- 使用上述钱包私钥，使用 `secp256r1` 算法签名请求内容
- 将请求内容按照 `key` 进行排序、拼接，使用 `md5` 签名
- 请求 `NewKeeper` 获取加密密钥.
- 将该密钥和播放链接传入 `NewPlayer` 进行播放。

## 环境配置:
- NewKeeper 测试网: https://gateway.testnet.newkeeper.org/api/v1/evt/check/
- NewKeeper 正式网: https://gateway.newkeeper.org/api/v1/evt/check/

## Demo 环境要求:
- python3, pip

## Demo 演示:

```
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
python demo.py
```

## API 
[API说明](api.md)
