# 插件
## 国内镜像
- 阿里云 http://mirrors.aliyun.com/pypi/simple/
- 豆瓣http://pypi.douban.com/simple/
- 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
- 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
- 华中科技大学http://pypi.hustunique.com/

## 临时使用
``` bash
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```
## 设为默认
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
## 数据挖掘所需插件
场景           | 三方库      
--------------|------------
数据处理        |pandas   
测试           |selenium   
解析库          |xlrd      
机器学习         |sklearn   
数据可视化       |seaborn   
分词器           ｜nltk、jieba  

-------------------
# QA
1. seaborn获取数据集异常
``` bash
<urlopen error [Errno 54] Connection reset by peer>
```
解决方案
```pip3 install requests[security]```
# python3
