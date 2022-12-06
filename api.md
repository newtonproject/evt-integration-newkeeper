# NewKeeper Api 


**请求地址**:

 `https://gateway.testnet.newkeeper.org/api/v1/evt/check/`


**请求说明**:

> 生成随机字符串作为  `message`,   建议使用`evt + 时间戳`，使用 newton 钱包进行签名，生成 `r s v` 



**header** 

| 名称          | 类型   | 说明                     |
| ------------- | ------ | ------------------------ |
| content-type  | string | application/json         |
| Authorization | string | 对 post 参数进行排序签名 |

#### params

| 参数             | 类型   | 说明                                             |
| ---------------- | ------ | ------------------------------------------------ |
| contract_address | string | EVT 合约地址                                     |
| sign_r           | string | 签名结果 r                                       |
| sign_s           | string | 签名结果 s                                       |
| sign_v           | string | 签名结果 v                                       |
| sign_message     | string | 使用`app_secret` 对 `message` 进行`aes` 加密结果 |
| app_key          | string | 申请访问 `newkeeper` 的 app_key                  |
| timestamp        | int    | 请求时间戳，单位秒                               |

#### response

| 参数        | 类型   | 说明                            |
| ----------- | ------ | ------------------------------- |
| csm_version | string | CSM 版本号                      |
| private_key | string | 用app_secret aes加密后的加密key |



