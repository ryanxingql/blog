# MATLAB

- [MATLAB](#matlab)

<details>
<summary><b>WINDOWS下安装</b></summary>

[[ref]](http://www.zhanshaoyi.com/12500.html)

配置右键打开方式：[[ref]](https://www.zhihu.com/question/54907280/answer/147331760)

</details>

<details>
<summary><b>UBUNTU下安装</b></summary>

[[ref]](https://programtip.com/en/art-23556)

- `mkdir ~/minstall`，用来挂载ISO。
- `mkdir -p ~/Matlab/R2019b/install`，作为安装路径。
- 将ISO文件挂载，需要`sudo`
- 编辑`installer_input.txt`和`activate.ini`时，需要强制写。
- 将Crack里的R2019b文件夹复制到安装路径时（本质是要里面的`.so`文件），要`sudo`
- `-propertiesFile`是单杠。
- 环境变量，应`vim ~/.bashrc`，然后`source ~/.bashrc`
- `matlab -nodesktop -nodisplay`
- 最后清理工作：先umount，然后可以删除log，安装文件夹以及安装包；或者挪到Downloads以备后患。

</details>
