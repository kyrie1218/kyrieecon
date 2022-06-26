# Linux基础
## 1. 常用命令
### 1.1 解压压缩包
每个压缩包具有自己的压缩算法，对应不同的压缩包格式，因此，需要使用不同的解压缩命令。
- `.tar.gz`格式：这是在

给定一个`test.tar.gz`压缩包到指定目录`/home/kyrie/files`，可使用如下命令解压缩：
```terminal
tar -zxvf test.tar.gz -C /home/kyrie/files
```
其中，重点关注参数`-zxvf`: 
- `z`代表使用gzip算法解压缩
- `x`代表从压缩的文件中提取文件
- `v`代表显示操作过程
- `f`代表制定压缩文件