# MATLAB

## 安装

WINDOWS 版参见[此处](http://www.zhanshaoyi.com/12500.html)。

UBUNTU 版主要流程参见[此处](https://programtip.com/en/art-23556)。大致修改和复述：

- 新建一个挂载 ISO 的路径：`mkdir ~/minstall`。
- 挂载：`sudo mount -o loop <iso_path> ~/minstall`。注意要 `sudo`。
- 如果挂载提示 `read-only`，那么需要将挂载后的文件夹复制为新文件夹：`cp -rf ~/minstall ~/minstall_c`。后续操作中 `~/minstall_c` 为挂载路径。
- 新建安装路径：`mkdir -p ~/Matlab/R2019b/install`。注意，强烈建议不要装在 `/usr` 下，后续能省去很多麻烦。
- 把 `Crack` 里的许可复制到安装路径：`cp </path/to/license_standalone.lic> ~/Matlab/R2019b/install/`。
- `cp ~/minstall_c/installer_input.txt ~/Matlab/R2019b/install/`
- `cp ~/minstall_c/activate.ini ~/Matlab/R2019b/install/`
- 编辑刚复制的 `installer_input.txt`，注意强制写。

   ```txt
   
   destinationFolder=/home/xql/Matlab/R2019b
   
   fileInstallationKey=09806-07443-53955-64350-21751-41297
   
   agreeToLicense=yes
   
   mode=silent
   
   activationPropertiesFile=/home/xql/Matlab/R2019b/install/activate.ini
   ```

- 编辑刚复制的 `activate.ini`，注意强制写。

   ```txt
   isSilent=true

   activateCommand=activateOffline

   licenseFile=/home/xql/Matlab/R2019b/install/license_standalone.lic
   ```

- 安装：`~/minstall_c/install -inputFile ~/Matlab/R2019b/install/installer_input.txt`。
- 复制破解包里的 `.so` 文件，干脆直接复制过来：`sudo cp -r <path/to/Crack>/R2019b ~/Matlab/`。
- 破解：`~/Matlab/R2019b/bin/activate_matlab.sh -propertiesFile ~/Matlab/R2019b/install/activate.ini`。
- 编辑环境变量：`export PATH=/home/xql/Matlab/R2019b/bin:$PATH`。
- 测试，启动无桌面版：`matlab -nodesktop -nodisplay`；直接 `matlab` 也行。
- 最后清理工作：`sudo umount ~/minstall`，然后删除 `~/{minstall,minstall_c}` 以及安装包（ISO 和破解包）。

Note：

- 我只有一个 ISO 文件。
- 我安装的是 R2019b。

## 配置右键打开方式

参见[此处](https://www.zhihu.com/question/54907280/answer/147331760)。
