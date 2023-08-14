ssh -p 52973 root@connect.westb.seetacloud.com
6Avh3YGcPC


/                ║系 统 盘║一般║实例关机数据不会丢失，可存放代码等。会随保存镜像一起保存
/root/autodl-tmp ║数 据 盘║ 快 ║实例关机数据不会丢失，可存放读写IO要求高的数据。但不会随保存镜像一起保存
/root/autodl-fs  ║文件存储║一般║可以实现多实例间的文件同步共享，不受实例开关机和保存镜像的影响。 

/ 放镜像，不操作
/root/autodl-tmp 放模型，对接阿里云盘。新盘在阿里云里面下载模型
/root/autodl-fs 放代码，每次不需要重新传文件