# Zotero

## 递归显示分类

参见[豆瓣](https://www.douban.com/group/topic/29374494/)。

## 改变 ZotFile 存储路径

假设搬动了名为 papers 的文件夹，再改 ZotFile 设置的路径，文件仍然找不到。这是因为路径和文件是绑定的，而不随设置改变而改变。

正确姿势：

- 不要删除原 papers 文件夹，不要删移任何文件。
- 改 ZotFile 设置路径。
- 然后在库中全选 entry，用 ZotFile rename，文件会自动迁移至新指定文件夹。

该方法还可以用来清理重名或错误命名的文件。

## Markdown Here 插件

注：非常不好用，经常崩溃，而且无法在 Markdown 基础上编辑，必须转回文本重新编辑。不推荐。

安装参考这篇[博客](https://www.cnblogs.com/Jay-CFD/p/10968876.html)。

使用：先编辑笔记，然后 `ctrl + s` 保存笔记，最后 `ctrl + alt + m` 转换为 Markdown。
