# MATLAB

- [MATLAB](#matlab)
  - [Arithmetic](#arithmetic)
  - [Colon operator](#colon-operator)
  - [Data type](#data-type)
    - [Cells](#cells)
    - [Char (array)](#char-array)
    - [Datetime](#datetime)
    - [Number](#number)
    - [Strings](#strings)
    - [Structs](#structs)
  - [Echo](#echo)
  - [Error-prone](#error-prone)
    - [切片范围](#切片范围)
    - [字符数组循环](#字符数组循环)
    - [循环按列操作](#循环按列操作)
    - [`length` 返回的是最大维度](#length-返回的是最大维度)
  - [File Input/Ouput](#file-inputouput)
    - [Binary files](#binary-files)
    - [Text files](#text-files)
  - [Format](#format)
    - [紧凑或加宽命令行间距](#紧凑或加宽命令行间距)
    - [调整输出显示精度](#调整输出显示精度)
    - [多行编辑](#多行编辑)
  - [Functions](#functions)
    - [I/O](#io)
    - [Polymorphism](#polymorphism)
    - [Scope](#scope)
    - [Script](#script)
    - [Subfunctions](#subfunctions)
  - [Installation](#installation)
    - [配置右键打开方式](#配置右键打开方式)
  - [Logical indexing](#logical-indexing)
  - [Matrix](#matrix)
  - [Optimization](#optimization)
    - [Preallocation](#preallocation)
  - [Random](#random)
    - [Pseudo random](#pseudo-random)
  - [Robustness](#robustness)
    - [Persistent variable](#persistent-variable)
    - [Check data type](#check-data-type)
  - [Plotting](#plotting)
  - [Selection](#selection)
    - [Relational and logical operators](#relational-and-logical-operators)
  - [Snippets](#snippets)
    - [合成路径](#合成路径)

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

## Data type

### Cells

每一个变量都存在内存里；每个 cell 存储一个内存地址。

和 struct 不同：

- 用 `{}` 访问。
- 可以索引，无需 field names。

创建：

```matlab
>> p = cell(2, 3)
p{2, 1} = pi
p =
  2×3 cell array
    {0×0 double}    {0×0 double}    {0×0 double}
    {0×0 double}    {0×0 double}    {0×0 double}
p =
  2×3 cell array
    {0×0 double}    {0×0 double}    {0×0 double}
    {[  3.1416]}    {0×0 double}    {0×0 double}
```

如果用 `()` 访问，指的是 cell 本身（内存地址），而不是地址指向的内容：

```matlab
>> class(p{2, 1})
class(p(2, 1))
ans =
    'double'
ans =
    'cell'
```

如果我们让一个 struct 等于另一个 struct，MATLAB 会复制一份，而不是让两个指针指向同一个地址：

```matlab
>> c1 = {[1,2], [3,4]};
c2 = c1;
c1{1} = [5,6];
c2{1}
ans =
     1     2
```

这种保护机制，在其他语言很少见，有利有弊。

### Char (array)

```matlab
>> for ii = 33:126
fprintf('%s', char(ii))
end
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
```

均为 ASCII 索引。33 是最小的可见的字符，而 126 最大。

实际上，我们用 `%s` 已经说明 `ii` 是指 ASCII 了，因此不需要手动用 `char` 转换：

```matlab
>> for ii = 33:126
fprintf('%s', ii)
end
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
```

字符串可以切片和索引，也可以逐项比较：

```matlab
>> a = 'MATLAB'
b = a(end:-1:1)
a =
    'MATLAB'
b =
    'BALTAM'
>> a == b
ans =
  1×6 logical array
   0   1   0   0   1   0
```

可以在 ASCII 和 char(s) 之间转换：

```matlab
>> b = double(a)
char(b)
b =
    77    65    84    76    65    66
ans =
    'MATLAB'
```

我们可以创建字符串数组，但对应长度必须相同：

```matlab
>> ['MATLAB'; 'BALTEM']
['MATLAB'; 'B']
ans =
  2×6 char array
    'MATLAB'
    'BALTEM'
Error using vertcat
Dimensions of arrays being concatenated are not consistent.
```

如图，实际上 array 存的是 char，因此要求对齐。因此可以对 char 转置：

```matlab
>> ['MATLAB'; 'BALTEM']'
ans =
  6×2 char array
    'MB'
    'AA'
    'TL'
    'LT'
    'AE'
    'BM'
```

常用的函数有：

```matlab
>> findstr('MATLAB', 'A')
ans =
     2     5
>> findstr('MATLAB', 'a')
ans =
     []

>> str = 'MATLAB';
>> strcmp(str(1:3), 'MAT')
ans =
  logical
   1
>> strcmpi(str(1:3), 'mat')  % ignoring case
ans =
  logical
   1

>> str2num('3.1415')
ans =
    3.1415
>> num2str(pi)
ans =
    '3.1416'

>> str = sprintf('hello, %s!', 'ryan')
str =
    'hello, ryan!'
```

### Datetime

```matlab
>> datetime
ans = 
  datetime
   2021-10-19 02:05:17
>> datetime('yesterday')
ans = 
  datetime
   2021-10-18
>> datetime('tomorrow')
ans = 
  datetime
   2021-10-20
>> datetime('now')
ans = 
  datetime
   2021-10-19 02:05:54
```

### Number

默认的数据类型是 double（64比特，8字节存储）：

```matlab
>> x = 23;
class(x)
ans =
    'double'

>> y = rand(3,4);
class(y)
ans =
    'double'

>> whos
  Name      Size            Bytes  Class     Attributes

  ans       1x6                12  char                
  x         1x1                 8  double              
  y         3x4                96  double              

```

大致分为 signed 和 unsigned，各 4 个。4 个元素分别用 8、16、32、64 比特表示。

例如，`int8` 的范围从 `-2^7` 到 `2^7 - 1`，而 `uint8` 就是从 `0` 到 `2^8 - 1`。

PS：关于数据范围的合理性，参见[博客](https://blog.csdn.net/fenzang/article/details/53500852)。

特别的，single 和 double 都有 `Inf` 和 `NaN`。

数据转换时，数据会被转为最近的合法结果，而不会报错：

```matlab
>> uint8(-1)
ans =
  uint8
   0
```

还有一些有用的函数：

```matlab
>> intmax('uint8')
ans =
  uint8
   255
>> intmin('uint8')
ans =
  uint8
   0
>> realmax('double')
ans =
  1.7977e+308
```

### Strings

从 2017a 版本开始引入。

```matlab
>> char_str = 'MATLAB';
class(char_str)
size(char_str)

real_str = "MATLAB";
class(real_str)
size(real_str)
ans =
    'char'
ans =
     1     6
ans =
    'string'
ans =
     1     1

>> char_str(end:-1:1)
real_str(end:-1:1)  % 纹丝不动；要先用char函数转换
ans =
    'BALTAM'
ans = 
    "MATLAB"
```

和 char(s) 比较：

- 打印方式是相同的。
- `strfind` 等函数工作方式相同。即都是 polymorphic 函数，可处理 char 和 string 类型。
- char 可以用矩阵拼接方式，而 string 应该用加。

```matlab
>> ['MAT', 'LAB']
["MAT", "LAB"]
'MAT' + 'LAB'
"MAT" + "LAB"
ans =
    'MATLAB'
ans = 
  1×2 string array
    "MAT"    "LAB"
ans =
   153   130   150
ans = 
    "MATLAB"
```

其他类型转 string 很方便，会转换为默认数据格式（double，显示精度 4 位小数）：

```matlab
>> string(3e3)
string(3.1415926)
string('hello')
string(true)
string(2>1)
ans = 
    "3000"
ans = 
    "3.1416"
ans = 
    "hello"
ans = 
    "true"
ans = 
    "true"
```

但反过来会存在歧义，因此大多数数据类型都不能被转换，默认的只有 double。例如，`logical("true")` 或 `double("pi")` 是无效的。

### Structs

和数组的区别：

- fields，不是 elements。
- field names，而不是索引。
- fields 可以具有不同数据类型，而 array 的 elements 必须是同一类型。

直接定义：

```matlab
>> r.ssn = 123456
class(r)
class(r.ssn)
r = 
  struct with fields:

    ssn: 123456
ans =
    'struct'
ans =
    'double'
```

Struct 可以作为数组，其第一层由于是数组，结构是一样的；但第二层可以不一样：

```matlab
>> company.number = 1;
company.owner.name = 'Jane';
company.owner.age = 23;

company(2).number = 2;  % 创建struct array；之前的即company(1)
company(2)
ans = 
  struct with fields:

    number: 2
     owner: []
```

可见，为保证 struct array 元素的一致性，struct 的 fields 是一样的，因此 owner 被自动创建，为空 array。

常用函数：

```matlab
>> isfield(company(1).owner, 'age')
isfield(company(2).owner, 'age')
company(1).owner = rmfield(company(1).owner, 'age')  % 必须要赋值
ans =
  logical
   1
ans =
  logical
   0
company = 
  1×2 struct array with fields:
    number
    owner
>> company(2)
ans = 
  struct with fields:

    number: 2
     owner: []
```

## Echo

```matlab
>> x = 1; y = 2;

>> x = 1, y = 2;
x =
     1
```

## Error-prone

### 切片范围

假设要从长宽为 `h` 和 `w` 的图像中遍历抽取边长为 `patch_sz` 的 patch；则程序为：

```matlab
start_h = 1;
while start_h + patch_sz - 1 <= h

     start_w = 1;
     while start_w + patch_sz - 1 <= w
          img_patch = img_raw(start_h:start_h+patch_sz-1, start_w:start_w+patch_sz-1, :);

          start_w = start_w + patch_sz;
     end

     start_h = start_h + patch_sz;
end
```

几点注意：

1. 用 while 语句要比 for 语句简单很多。
2. 每个 patch 的范围是从 `start_h` 到 `start_h + patch_sz - 1`，注意 `-1`。
3. 千万不要把 `start_w=1` 放到最外面。

### 字符数组循环

```matlab
for charr = ['qp22', 'qp37']
    fprintf('%s\n', charr);
end

>> Untitled
q
p
2
2
q
p
3
7
```

实际上：

1. `'qp22'` 本身即字符数组，是一个数组！
2. `['qp22', 'qp37']` 就是把两个字符数组拼接了。长度可不是 2。

正确做法：使用字符串数组，即双引号。

### 循环按列操作

```matlab
a = zeros(7,1);
count = 0;
for ia = a
    count = count + 1;
end
disp(count);

>> Untitled
     1
```

即，只循环了一次。

### `length` 返回的是最大维度

```matlab
a = zeros(7,1);
b = zeros(1,7);
disp(length(a));
disp(length(b));

>> demo
     7
     7
```

## File Input/Ouput

首先要获取和修改工作路径：

```matlab
>> pwd
ans =
    'C:\Users\XING\Desktop'
>> ls

.                 caesar.asv        
..                caesar.m          
.picasaoriginals  desktop.ini       

>> cd ../
>> cd Desktop\
>> save

Saving to: C:\Users\XING\Desktop\matlab.mat

>> clear
>> load 

Loading from: C:\Users\XING\Desktop\matlab.mat
```

### Binary files

不属于 text files 的，都可以看作是 binary files。

```matlab
fid = fopen(filename, 'r');  % 不需要rt
%fid = fopen(filename, 'w+');
if fid < 0
    error('error opening file %s\n', filename)
end

A = fread(fid, inf, 'double');
fwrite(fid, A, 'double')

fclose(fid);  % 一定要关，否则其他程序可能无法访问这个文件
```

A 是一个 `nx1` 的 double 数组。如果想保持维度，需要在存储时保存维度信息。

### Text files

编码格式可以多种多样；MATLAB 会解决 encoding 和 decoding 问题。

```matlab
fid = fopen(filename, 'rt');  % 对text文件启动读权限，定义一个指针
if fid < 0
    error('error opening file %s\n', filename)
end

oneline = fgets(fid);  % 一次读一行，每行都是一个string
while ischar(oneline)
    fprintf('%s', oneline);
    oneline = fgets(fid);
end

fprintf('\n');
fclose(fid);
```

## Format

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

### 多行编辑

```matlab
>> x = 1*...
2
x =
     2
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

### I/O

```matlab
function a = one_more
x = input('Give me one number: ');
a = x + 1;
end

>> one_more
Give me one number: pi/2
ans =
    2.5708
```

重复特殊字符两次，即可输出该特殊字符：

```matlab
>> fprintf('12.5%%; %.1f\n', 0.1*0.1)
12.5%; 0.0
>> fprintf('This is a backslash: \\\n')
This is a backslash: \
>> fprintf('This is a single quote: ''\n')
This is a single quote: '
```

当参数不足时，会自动截断：

```matlab
>> fprintf('1: %d; 2: %d; 3: %d; end\n', 1, 2)
1: 1; 2: 2; 3: >> %连\n也被截断了
```

当参数过多时，会自动循环：

```matlab
>> fprintf('1: %d; 2: %d; 3: %d; end\n', 1, 2, 3, 4)
1: 1; 2: 2; 3: 3; end
1: 4; 2: >> 
```

这个性质可以帮助我们快速打印向量：

```matlab
>> fprintf('%4.1f\n', [1,2,3,4])
 1.0
 2.0
 3.0
 4.0
```

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

具体编程案例，输入和输出参数的数量都是可变的：

```matlab
function [table, summa] = multable(n, m)
if nargin < 2
    m = n;
end

table = (1:n)' * (1:m);

if nargin == 2
    summa = sum(table(:));
end
end

>> tab = multable(2)
tab =
     1     2
     2     4
>> tab = multable(2, 1)
tab =
     1
     2
>> [tab, summa] = multable(2, 1)
tab =
     1
     2
summa =
     3
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

### Subfunctions

多个函数可以放在一个 M 文件（又称为 script）里。第一个函数是主函数，可以在外部调用；之后的函数都是子函数，只能在文件内被调用。

```matlab
function [a, s] = myRand(low, high)
a = low + rand(3, 4) * (high - low);
s = mySum(a);


function s = mySum(matrx)
s = sum(matrx(:));
```

## Installation

Windows 版参见[此处](http://www.zhanshaoyi.com/12500.html)。

Ubuntu 版大致流程：

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

## Logical indexing

基本用法：

```matlab
>> l1 = logical([-2, 1, 0])
l2 = [2>1, 2<1, ~(3<2)]
tmp = [0, -1, 2];
l3 = tmp > 1
l4 = tmp(tmp > 1)

a = 1:3
a(l1)
a(l2)
a(l3)
a(l4)  % 注意是a的第二个元素
l1 =
  1×3 logical array
   1   1   0
l2 =
  1×3 logical array
   1   0   1
l3 =
  1×3 logical array
   0   0   1
l4 =
     2
a =
     1     2     3
ans =
     1     2
ans =
     1     3
ans =
     3
ans =
     2
```

可以修改元素：

```matlab
>> a = 1:3
a(a<2) = 0

a = 1:3
a(a<2) = a(a<2) + 10

A = [1 2 3;4 5 6]
B = A(A>2)  % 类似于先用A(:)把列向量取出来，然后再执行逻辑取值
a =
     1     2     3
a =
     0     2     3
a =
     1     2     3
a =
    11     2     3
A =
     1     2     3
     4     5     6
B =
     4
     5
     3
     6
```

当然，我们也可以保持 A 的形态：不新建 B，而是直接修改 A：

```matlab
>> A = [5 3 1;2 0 4]
A(A<3) = -3:-1
A =
     5     3     1
     2     0     4
A =
     5     3    -1
    -3    -2     4
```

具体而言，当逻辑取值在左侧时，就是按列操作，逐个找符合逻辑的项，分别执行赋值操作（因此要求维度相同，即元素数目相同）。

如果两侧同时执行，那么就是先执行右侧，再执行左侧。

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

## Optimization

### Preallocation

假设要给一个矩阵赋值。若矩阵没有初始化，而是边赋值边扩容，那么消耗的时间可能是初始化后再赋值耗时的 100 倍。

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

### Pseudo random

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

## Robustness

增加注释和输入判断：

```matlab
function [table, summa] = multable(n, m)

%MULTABLE multiplication table.
% xxx.
% xxx.

if nargin < 2
    error('too few arguments!')
end

table = (1:n)' * (1:m);

if nargin == 2
    summa = sum(table(:));
end
end
```

### Persistent variable

少定义全局变量，多使用 persistent variable：

```matlab
function total = accumulate(n)
persistent summa;
if isempty(summa)
    summa = n;
else
    summa = summa + n;
end
total = summa;
end

>> accumulate(1)
ans =
     1
>> accumulate(2)
ans =
     3
>> accumulate(3)
ans =
     6
```

可见，`summa` 变量一直在保持。有 3 种方式初始化 persistent 变量：

1. 重新保存函数。
2. 清除函数：`clear accumulate`。
3. 重启 MATLAB。

### Check data type

例如一个日期格式检查函数：

```matlab
function isvalid = valid_date(y, m, d)
   % Check if the inputs are valid
   % Check that they are scalars
   if ~(isscalar(y) && isscalar(m) && isscalar(d))
       isvalid = false;
   % Check that inputs are positive
   elseif ~all([y, m, d] > 0)
       isvalid = false;
   % Check that inputs are integers (not the data type)
   elseif any(rem([y, m, d], 1))
       isvalid = false;
   % Check that m and d are below the max possible
   elseif (m > 12) || (d > 31)
       isvalid = false;
   % The inputs could be a valid date, let's see if they actually are
   else
       % Vector of the number of days for each month
       daysInMonth = [31 28 31 30 31 30 31 31 30 31 30 31];
       % If leap year, change days in Feb
       if isequal(rem(y, 4), 0) && (~isequal(rem(y, 100), 0) || isequal(rem(y, 400), 0))
            daysInMonth(2) = 29;
       end
       maxDay = daysInMonth(m);
       if d > maxDay
           isvalid = false;
       else
           isvalid = true;
       end

   end
end
```

## Plotting

```matlab
>> x1 = 0:0.1:2*pi;
>> x2 = pi/2:0.1:3*pi;
>> y1 = sin(x1);
>> y2 = cos(x2);
>> figure  % 新建图像
>> plot(x1,y1,'r',x2,y2,'k:')  % 类似hold on；k是黑色
```

如果选择已有图像绘制，会覆盖原图像，除非 `hold on`。

```matlab
figure(1)
plot(x1,y1,'r')
```

## Selection

### Relational and logical operators

如果逻辑正确，则返回 `1`，否则返回 `0`。

```matlab
>> x = (16*64 > 1000) + 9
x =
    10
```

`0` 和任意非零值可以用于逻辑判断：

```matlab
function if_test(x)
if x
    fprintf('%d is true!\n', x);
else
    fprintf('%d is false!\n', x);
end

>> if_test(-1)
-1 is true!
>> if_test(0)
0 is false!
>> if_test(1)
1 is true!
>> if_test(1e-12)
1.000000e-12 is true!
```

数组可以用于逻辑判断：

```matlab
>> [4 -1 7] > [5 -9 6]
ans =
  1×3 logical array
   0   1   1

>> [4 -1 7] > 5
ans =
  1×3 logical array
   0   0   1

>> ~[1 pi 0 -2]
ans =
  1×4 logical array
   0   0   1   0
```

与或非用于数组和标量的形式不同：

```matlab
>> [1 2 -3] && [3 2 -1]
Operands to the || and && operators must be convertible to logical scalar values.

>> [1 2 -3] & [3 2 -1]
ans =
  1×3 logical array
   1   1   1

>> 2 & [0 1; 2 3]
ans =
  2×2 logical array
   0   1
   1   1
```

输入 `help precedence` 查看运算符优先级。

## Snippets

### 合成路径

这里要用到一个函数 `dir`；输入参数是文件夹路径，输出参数是一个 struct array，每个 struct 都记录了一个文件的属性（即，每个 struct 都有 6 个field，记录了文件名、路径等）。如果不指定返回参数，则显示所有文件名。

```matlab
all_files = dir(fullfile('./test', '*.m'));
i = 0;
for file = all_files'  % 是7x1的array，需要转置，否则按列遍历，只有1列
    i = i + 1;
    disp(file)
end

>> Untitled
       name: 'test1.m'
     folder: 'C:\Users\XING\Downloads\test'
       date: '26-10月-2021 14:23:16'
      bytes: 0
      isdir: 0
    datenum: 7.3846e+05
       name: 'test2.m'
     folder: 'C:\Users\XING\Downloads\test'
       date: '26-10月-2021 14:23:20'
      bytes: 0
      isdir: 0
    datenum: 7.3846e+05
```
