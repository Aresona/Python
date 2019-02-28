# ffmpeg

## ffmpeg 转码原理

既然是转码，那整理流程就是，先把一个源文件，比如input.mp4，拆包（DEMUX），获得编码过的数据packet，然后把packet送给decoder解码，获得audio/video的原始数据frame(YUV/RGB/PGM音频对应)，再把frame送给encoder编码，又变成编码过的数据packet，然后把packet打包(MUX)成另一种格式，比如output.ts

![](https://img-blog.csdn.net/20160628193241123)

## PTS
在AVStream的阶段，也就是还没解码之前的原始数据，假设是mp4文件，FPS = 15，那么 time_base={1， 15}，从第一帧到开始，每一ES packet的PTS就是1， 2， 3，。。。。 为何呢？ 

```
简单啊，比如第一帧，packet.pts=1，实际的packet.pts = 1/15 = 0.0666s 
同理第二帧，packet.pts=2，实际的packet.pts = 2/15 = 0.1333s 
到第15帧，packet.pts=15，实际的packet.pts = 15/15 = 1s 
```

## Filter 基本原理
### 线性属性


## Filter 使用方法

## 错误解决
1. DemuxException: type = CodecUnsupported, info = Flv: Unsupported codec in video frame: 2

```shell
ffmpeg -stream_loop -1 -i 20190215121503425_0.flv -f flv rtmp://localhost/koh/first  
```

2. [Transmuxer] > Error while initialize transmuxing worker, fallback to inline transmuxing

```shell
ffmpeg -stream_loop -1 -i 20190215121503425_0.flv -f flv -c copy rtmp://localhost/koh/first
```