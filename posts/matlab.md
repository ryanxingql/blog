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

## Snippets

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

## 调整输出

### 紧凑或加宽命令行间距

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

## echo 和换行编辑

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

## Colon operator

Operator 本质上是一个函数，但用某个特殊的符号表示。以下为基础用法：

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
  1×0 empty double row vector
>> size(x)
ans =
     1     0
>> size([])
ans =
     0     0
```

## Matrix

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

`end` 是一个保留关键字，用户无法定义 `end` 变量。

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

特殊创建：

```matlab
>> diag([1 2 3 4])
ans =
     1     0     0     0
     0     2     0     0
     0     0     3     0
     0     0     0     4
```

## Arithmetic

基础算术操作符：

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

## Functions

输入 `edit` 进入编辑页面。

基础定义：

```matlab
function [a, s] = myRand(low, high)
a = low + rand(3, 4) * (high - low);
s = sum(a(:));
end

>> myRand(2,5)  % 只捕捉第一个参数作为ans
ans =
    4.0362    3.1767    4.1181    2.1385
    4.2732    3.9664    2.0955    2.2914
    4.2294    2.5136    2.8308    4.4704
>> [a, s] = myRand(2,5)
a =
    4.0845    2.1033    4.2966    3.4693
    2.9513    3.3162    4.3856    3.3368
    4.8507    3.1447    2.5606    3.9389
s =
   42.4385
```

以下均为合格的定义：

```matlab
function func
function func(in1, in2)
function out1 = func
function out1 = func(in1, in2)
function [out1, out2] = func
function [out1, out2] = func(in1, in2)
```

不要用 built-in 函数的名字，例如 `sqrt`。否则，自定义函数会置顶。用 `exist sqrt` 查询，返回 `5` 即为 built-in 函数。

### Subfunctions

多个函数可以放在一个 M 文件（又称为 script）里。第一个函数是主函数，可以在外部调用；之后的函数都是子函数，只能在文件内被调用。

```matlab
function [a, s] = myRand(low, high)
a = low + rand(3, 4) * (high - low);
s = mySum(a);


function s = mySum(matrx)
s = sum(matrx(:));
```

### Scope

假设我们有一个全局变量 `a`。我们令函数输出名为 `a`，即 `function a = myFunc`。在外部执行函数，即输入 `myFunc`。执行完毕后，`a` 不变。这是因为，函数中的 `a` 是一个局部变量，当函数执行完毕时，该变量就消失了。除非进行赋值：`a = myFunc`。

在函数内部访问全局变量：

```matlab
function func
global a;
a = 1;
end
```

慎用，少用。

### Script

Script 就是写在 M 文件里的一系列指令。和函数不同，script 的 scope 就是 command window 所访问的 scope。因此，script 可以访问和修改全局变量空间。

### Polymorphism

函数的输入形式是可变的。相对应地，函数的输出格式也会发生变化：

```matlab
>> sum([1 2 3])
ans =
     6
>> sum([1 2;3 4])
ans =
     4     6
```

此外，有些函数的输出格式也是可变的：

```matlab
>> a = max([3 2 1 0])  % 返回最大值
a =
     3
>> [a, b] = max([3 2 1 0])  % 返回最大值和索引
a =
     3
b =
     1
```

## Random

```matlab
>> 1 + rand(5, 4) * 11  % 返回一个5x4矩阵，范围是1到12
ans =
    9.9571    3.7619    7.4379    9.2910
    3.6788    7.7765    7.0470    5.1849
   11.2219    6.2062   11.0891    7.2460
    4.8498    4.8683    4.1442    1.8344
    3.1625   10.1391    9.3292    1.5935

>> randi(12, 5, 4)  % 也是1到12；要求整数
ans =
     7     6     4     8
    10     1     7     9
    12     5     2     9
     2     2     8     6
     7    10     4     2

>> randi(12, 3)  % 方阵
ans =
     3    10     1
    11     7     6
     2    12     2

>> randi([5, 6], 3)  % 给定范围5至6
ans =
     6     6     5
     5     6     5
     6     5     6

>> randn(2)  % 服从标准正态分布
ans =
   -0.2779   -2.0518
    0.7015   -0.3538
```

### 伪随机

每一次重启 MATLAB，得到的第一个随机数总是 `0.8147`。事实上，MATLAB 使用的是由 RNG 控制的伪随机发生器：

```matlab
>> rng(0)
>> rand(1, 3)
ans =
    0.8147    0.9058    0.1270
>> rand(1, 3)
ans =
    0.9134    0.6324    0.0975
>> rng(0)
>> rand(1, 3)
ans =
    0.8147    0.9058    0.1270
```

如果想获得一个独一无二的随机种子，输入 `rng('shuffle')`；此时，当前的系统时钟将作为随机种子。
