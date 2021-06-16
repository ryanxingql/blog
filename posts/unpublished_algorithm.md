# ALGORITHM

## 数据结构

<details>
<summary><b>逆向求和（LEETCODE 1#）</b></summary>
<p>

在数组中，找出和为 target 的两个数的位置。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a_dict = {}
        for i, k in enumerate(nums):
            if target - k in a_dict:
                return  [a_dict[target-k], i]
            a_dict[k] = i
```

</p>
</details>

<details>
<summary><b>查重（LEETCODE 217#）</b></summary>
<p>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """too slow
        # 思路：逐个与前面的比较
        for ii, i in enumerate(nums):
            for j in nums[:ii]:
                if i == j:
                    return True
        return False
        """

        # 思路：制作字典，自动去重，然后比较长度
        len_ori = len(nums)
        nums = set(nums)
        if len(nums) != len_ori:
            return True
        return False
```

</p>
</details>

## 递归

<details>
<summary><b>递归剖析（LEETCODE 38#）</b></summary>
<p>

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        str_ = "1"
        if n == 1:
            return str_
        else:
            str_ = self.func_recur("11", 2, n)
            return str_

    def func_recur(self, str_, m, n):
        """
        m: execution times; n: required times
        """
        if m != n:
            str_ = self.func_parse(str_)
            str_ = self.func_recur(str_, m+1, n)
        return str_
    
    def func_parse(self, str_):
        return_str = ""
        start = 0
        while start < len(str_):
            item_start = str_[start]
            count = 1
            for pos, item in enumerate(str_[start+1:]):
                if item == item_start:
                    count += 1
                else:
                    break
            return_str += f"{count}{item_start}"
            start += count
        return return_str

solution = Solution()
print(solution.countAndSay(4))
```

</p>
</details>

<details>
<summary><b>生成全排列</b></summary>
<p>

```c
// 输入正整数1<=N<=10，生成1到N的全排列，从小到大排序。
// 输入例：3
// 输出例：
// 1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1

// 思路：递归。
// 设置两个数组，一个是候选数组，一个是完成数组。
// 候选数组不断减小，完成数组不断扩充。
// 当候选数组减完时，就可以打印完成数组了，停止递归（即返回）。
// 否则，继续递归。

#include <stdio.h> 
#include <stdlib.h> 

void printf_array(int* arr, int len_arr) {
    int i = 0;
    for (i=0; i<len_arr-1; i++) {
        printf("%d ", *(arr+i));
    }
    printf("%d\n", *(arr+i));
}

void copy_array(int* a, int* b, int len) {
    for(int i=0; i<len; i++) {
        *b++ = *a++;
    }
}

void del_array(int* arr, int len_arr, int pos) {
    for (int i=pos; i<len_arr-1; i++) {
        *(arr + i) = *(arr + i + 1);
    }
}

void func_recur(int len_shuffle, int* shuffle_array, int len_done, int* done_array) {
    for (int i=0; i<len_shuffle; i++) {
        // 深复制，以免影响原数组
        int* shuffle_array_copy = (int*) malloc(sizeof(int) * len_shuffle);
        copy_array(shuffle_array, shuffle_array_copy, len_shuffle);

        *(done_array + len_done) = *(shuffle_array_copy + i);
        if (len_shuffle == 1) {
            printf_array(done_array, len_done+1);
            free(shuffle_array_copy);  // 无返回，结束递归
        }
        else {
            del_array(shuffle_array_copy, len_shuffle, i);
            func_recur(len_shuffle-1, shuffle_array_copy, len_done+1, done_array);  // 继续递归
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    
    int *shuffle_array = (int *) malloc(sizeof(int) * N);  // 待排列的候选数组。注意这是个指向数组的指针
    int *done_array = (int *) malloc(sizeof(int) * N);  // 排列完、待打印的数组。注意这是个指向数组的指针
    for (int i=0; i<N; i++) {
        *(shuffle_array + i) = i + 1;  // 生成最小全排列，作为待排列数组
        *(done_array + i) = 0;
    }
    
    func_recur(N, shuffle_array, 0, done_array);

    free(shuffle_array);
    free(done_array);
    return 0;
}
```

</p>
</details>
