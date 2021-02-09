# MATLAB

- **WINDOWS 版安装**：参见[此处](http://www.zhanshaoyi.com/12500.html)。
- **WINDOWS 版配置右键打开方式**：参见[此处](https://www.zhihu.com/question/54907280/answer/147331760)。

<details>
<summary><b>UBUNTU 版安装</b></summary>
<p>

- 新建用来挂载 ISO 的文件夹：`mkdir ~/minstall`。
- 新建 MATLAB 的安装路径：`mkdir -p ~/Matlab/R2019b/install`。
- 将ISO文件挂载；需要 `sudo`。
- 编辑 `installer_input.txt` 和 `activate.ini` 时，需要强制写。
- 将 `Crack` 里的 `R2019b` 文件夹复制到安装路径时（本质是要里面的 `.so` 文件），要 `sudo`。
- `-propertiesFile` 是单杠。
- 环境变量，应 `vim ~/.bashrc`，然后 `source ~/.bashrc`。
- 启动无桌面版：`matlab -nodesktop -nodisplay`；直接 `matlab` 也行。
- 最后清理工作：先 umount，然后可以删除 log，安装文件夹以及安装包。

参考[此处](https://programtip.com/en/art-23556)。

</p>
</details>
