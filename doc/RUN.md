# 执行步骤

1. 检测环境
2. 执行

## 检测环境

1. 检测 JAVA_HOME
2. 检测 JMeter 是否正常
3. 检测 Host 是否存在


### 检测 JAVA_HOME 

### 检测 JMeter

参考：[Jmeter以non-gui模式进行分布式测试](http://www.cnblogs.com/qianyiliushang/p/4381639.html)
1.关闭防火墙
2.所有的客户端都在同一个子网内
3.server也必须在同一子网内如果使用192.x.x.x或者10.x.x.x这样的IP地址，如果server没有使用192或者10这样的IP地址，（server同client不在同一子网内）将不会有任何问题
4.确保Jmeter可以访问到server
5.确保各系统的Jmeter版本保持一致，不同版本的Jmeter将不能很好的工作

### 检测 Host

### 检测 JMX 文件

1. 不能出现结果树等