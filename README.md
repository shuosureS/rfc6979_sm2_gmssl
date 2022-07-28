# rfc6979_sm2_gmssl
# Project: impl sm2 with RFC6979

### 刘硕-202000460043-shuosureS

## 简介

本项目主要实现了RFC6979生成伪随机数k，对于sm2直接调用了gmssl。通过对RFC6979文档的阅读，了解了RFC6979生成伪随机数k的过程，并用python进行了实现。

## 代码说明

项目的实现变量都按照RFC6979文档来命名。

```python
q=164662474442864913204610293692179443533679901685075671686168943558347871758383
qlen=256
rlen=256
```

这里q是使用sagemath随机生成的256大素数，所以qlen为256，由于25是8的倍数所以rlen也为256。

```python
def int2octets(x):
    
def bits2octets(string):
    
def bits2int(string):
  
```

函数int2octets为将int类型的变量转换为32个8bit，返回一个字符串

函数bits2octets为将字符串转换为32个8bit，即先将字符串转换为int再调用int2octets

函数bits2int为将字符串转换为int类型

```python
def gen_k(data,x):
```

gen_k就是生成k的函数里面根据RFC文档中的步骤依次实现。

其中hash函数选择了sm3

## 运行结果

经验证对于不同的data，其生成的k也是不同的

|data|k|
|--|--|
|1111|31338491022916135759812321691097177620246|
|111|56088773151934583287914657276110050933269961|

![截图](attachment:b77d5e899b8f6044d6f2162fe9cbd4ad)

![截图](attachment:e9a15212ae8636281d8ecd272fb7530c)

## 参考文献

[https://datatracker.ietf.org/doc/html/rfc6979](https://)

[https://rfc2cn.com/rfc6979.html](https://)

[https://www.jianshu.com/p/0c27e5b51cdd](https://)
