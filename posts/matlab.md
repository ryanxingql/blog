# MATLAB

## WINDOWS 版安装

参见[此处](http://www.zhanshaoyi.com/12500.html)。

## WINDOWS 版配置右键打开方式

参见[此处](https://www.zhihu.com/question/54907280/answer/147331760)。

## UBUNTU 版安装

主要流程参见[此处](https://programtip.com/en/art-23556)。几点补充或修改：

- 我用的是只有一个 ISO 的 MATLAB R2019b。
- 新建用来挂载 ISO 的文件夹：`mkdir /home/xql/minstall`。
- 新建 MATLAB 的安装路径：`mkdir -p /home/xql/Matlab/R2019b/install`。
- 将ISO文件挂载时，需要 `sudo`。
- 如果挂载提示 `read-only`，需要将挂载后的文件夹复制：`cp -rf /home/xql/minstall /home/xql/minstall_c`，然后将 `/home/xql/minstall_c` 视为挂载路径。
- 编辑 `installer_input.txt` 和 `activate.ini` 时，需要强制写 `wq!`。
- 将 `Crack` 里的 `R2019b` 文件夹复制到安装路径时（本质是要里面的 `.so` 文件），要 `sudo`。
- `-propertiesFile` 是单杠。
- 环境变量，应 `vim ~/.bashrc`，然后 `source ~/.bashrc`。
- 启动无桌面版：`matlab -nodesktop -nodisplay`；直接 `matlab` 也行。
- 最后清理工作：先 umount，然后可以删除 log，安装文件夹以及安装包。
