# MATLAB

## 安装

Windows 版参见[此处](http://www.zhanshaoyi.com/12500.html)。

Ubuntu 版主要流程参见[此处](https://programtip.com/en/art-23556)。大致修改和复述：

- 新建一个挂载 ISO 的路径：`mkdir ~/minstall`。
- 挂载：`sudo mount -o loop <iso_path> ~/minstall`。注意要 `sudo`。
- 如果挂载提示 `read-only`，那么需要将挂载后的文件夹复制为新文件夹：`cp -rf ~/minstall ~/minstall_c`。后续操作中 `~/minstall_c` 为挂载路径。
- 新建安装路径：`mkdir -p ~/Matlab/R2019b/install`。注意，强烈建议不要装在 `/usr` 下，后续能省去很多麻烦。
- 把 `Crack` 里的许可复制到安装路径：`cp </path/to/license_standalone.lic> ~/Matlab/R2019b/install/`。
- `cp ~/minstall_c/installer_input.txt ~/Matlab/R2019b/install/`
- `cp ~/minstall_c/activate.ini ~/Matlab/R2019b/install/`
- 编辑刚复制过来的 `~/Matlab/R2019b/install/installer_input.txt`，注意强制写。

   ```txt

   destinationFolder=/home/xql/Matlab/R2019b

   fileInstallationKey=09806-07443-53955-64350-21751-41297

   agreeToLicense=yes

   mode=silent

   activationPropertiesFile=/home/xql/Matlab/R2019b/install/activate.ini
   ```

- 编辑刚复制过来的 `~/Matlab/R2019b/install/activate.ini`，注意强制写。

   ```txt
   isSilent=true

   activateCommand=activateOffline

   licenseFile=/home/xql/Matlab/R2019b/install/license_standalone.lic
   ```

- 安装：`~/minstall_c/install -inputFile ~/Matlab/R2019b/install/installer_input.txt`。
- 复制破解包里的 `.so` 文件；干脆直接把文件夹复制过来：`sudo cp -r <path/to/Crack>/R2019b ~/Matlab/`。
- 破解：`~/Matlab/R2019b/bin/activate_matlab.sh -propertiesFile ~/Matlab/R2019b/install/activate.ini`。
- 编辑环境变量：`export PATH=/home/xql/Matlab/R2019b/bin:$PATH`。
- 测试，启动无桌面版：`matlab -nodesktop -nodisplay`；直接 `matlab` 也行。
- 最后清理工作：`sudo umount ~/minstall`，然后删除 `~/{minstall,minstall_c}` 以及安装包（ISO 和破解包）。

Note：

- 我只有一个 ISO 文件。
- 我安装的是 R2019b。

### 配置右键打开方式

参见[此处](https://www.zhihu.com/question/54907280/answer/147331760)。

## 使用

### 合成路径-记录单元-循环

```matlab
png_struct = dir(fullfile(png_dir, '*.png));
png_name_cell = {png_struct.name};

png_path_cell = {};
for ii = 1:length(png_name_cell)
   png_path_cell = fullfile(png_dir, png_name_cell(ii));
   png_path = png_path_cell{1};
   png_path_cell{ii} = png_path;
end
```

### 字符串拼接

```matlab
str2 = strcat('file_' + int2str(num) + '.txt');
```

### 紧凑、加宽命令行间距

```matlab
format compact
format loose

help format
```

### 调整输出显示精度

```matlab
format short  % 默认，4位小数
format long  % single显示7位，double显示15位
```

### echo和换行

```matlab
>> x = 1; y = 2;
>> x = 1, y = 2;
x =
     1
>> x = 1*...
2
x =
     2
```

### Colon operator

operator本质上是一个函数，但用某个特殊的符号表示。

```matlab
>> x = 1:3:7
x =
     1     4     7
>> x = 1:4
x =
     1     2     3     4
>> size(x)
ans =
     1     4
>> x = 7:-3:1
x =
     7     4     1
>> x = 7:3:1
x =
  空的 1×0 double 行向量
>> size(x)
ans =
     1     0
>> size([])
ans =
     0     0
```

### Matrix

基本的访问和扩展：

```matlab
>> x = [1:4; 5:8; 9:12]
x =
     1     2     3     4
     5     6     7     8
     9    10    11    12
>> x(2,3)
ans =
     7
>> x(2,3) = 0  % 会返回整个x
x =
     1     2     3     4
     5     6     0     8
     9    10    11    12
>> y(2,3) = 1  % 会新建一个满足要求的最小矩阵，未定义项为0
y =
     0     0     0
     0     0     1
>> x(4,5) = -1  % 同理，可用于扩展矩阵
x =
     1     2     3     4     0
     5     6     0     8     0
     9    10    11    12     0
     0     0     0     0    -1
>> x(end, end)
ans =
     -1
>> x(end, end-1)
ans =
     0
>> x(end, end+1) = -2
x =
     1     2     3     4     0     0
     5     6     0     8     0     0
     9    10    11    12     0     0
     0     0     0     0    -1    -2
>> x(1:end, 2:3) = [10 20; 30 40; 50 60; 70 80]
x =
     1    10    20     4     0     0
     5    30    40     8     0     0
     9    50    60    12     0     0
     0    70    80     0    -1    -2
```

`end`是一个保留关键字，用户无法定义`end`变量。

根据子数组访问或修改：

```matlab
>> x = [1 2 3; 4 5 6]
x =
     1     2     3
     4     5     6
>> x(2, [1 3])
ans =
     4     6
>> x(2, 1:3)
ans =
     4     5     6
```

合并矩阵：

```matlab
>> A1 = ones(2,3)
A1 =
     1     1     1
     1     1     1
>> A2 = 2 * ones(2,3)
A2 =
     2     2     2
     2     2     2
>> A3 = 3 * ones(2,3)
A3 =
     3     3     3
     3     3     3
>> [A1 A2 A3]
ans =
     1     1     1     2     2     2     3     3     3
     1     1     1     2     2     2     3     3     3
>> [A1; A2; A3]
ans =
     1     1     1
     1     1     1
     2     2     2
     2     2     2
     3     3     3
     3     3     3
```

### Arithmetic

```matlab
>> x = [1 2; 3 4]
x =
     1     2
     3     4
>> y = [5 6; 7 8]
y =
     5     6
     7     8
>> x .* y  % array multiplication
ans =
     5    12
    21    32
>> x * y  % matrix multiplication
ans =
    19    22
    43    50

>> x ./ y  % array divison
ans =
    0.2000    0.3333
    0.4286    0.5000
>> x .\ y  % array division
ans =
    5.0000    3.0000
    2.3333    2.0000

>> x .^ 3  % array multiplication
ans =
     1     8
    27    64
>> x ^ 3  % matrix multiplication
ans =
    37    54
    81   118
```
