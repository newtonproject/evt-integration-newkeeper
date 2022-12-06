# 集成 NewKeeper

本 Demo 演示如何从 `NewKeeper` 请求视频资源的密钥。

## 说明文档
- 申请 `app_key` 和 `app_secret`
- 创建 `NEW` 钱包，使用该钱包 `Mint` EVT.(目前由 EVT-Core mint evt 到指定地址)
- 使用上述钱包私钥，使用 `secp256r1` 算法签名请求内容
- 将请求内容按照 `key` 进行排序、拼接，使用 `md5` 签名
- 请求 `NewKeeper` 获取加密密钥.

## 接口说明