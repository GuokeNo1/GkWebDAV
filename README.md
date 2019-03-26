GkWebDAV
======================= 

## 当前功能
|功能|方法|
|---|---|
|查看当前所在目录|```cwd```|
|切换工作目录|```cd()```|
|列出当前目录内的文件|```ls()```|
|创建目录|```mkdir()```|
|递归创建目录|```mkdirs()```|
|删除目录|```rmdir()```|
|删除文件|```delete()```|
|移动文件|```move()```|
|复制文件|```copy()```|
|上传文件|```upload()```|
|下载文件|```download()```|
|检查文件是否存在|```exists()```|


## 安装方法
  
使用 pip 安装 Gkwebdav 模块  
```
pip install Gkwebdav
```  

## 简单上手
```
import Gkwebdav

# 创建Gkwebdav对象
webdav = Gkwebdav.Gkwebdav(url='webdavurl', username='username', password='password')

# 输出当前所在工作目录，默认为'/'
print(webdav.cwd)

# 切换工作目录，无返回值
webdav.cd(path='dirname')

# 返回目标目录内内容，参数缺省值为'/'
# 执行成功时的返回值为：
# {'success': True, 'result': [{'path': path, 'length': length, 'lastmodified': lastmodified, 'type': type}]}
# 执行失败时的返回值为：
# {'success': False, 'result': '失败代码'}
webdav.ls([path=''])

# 创建文件夹，无返回值
webdav.mkdir(path='newdirname')

# 递归创建一个文件夹，无返回值
webdav.mkdir(path='newdir1/newdir2/.../newdir3')

# 删除一个目录，无返回值
webdav.rmdir(path='dirname')

# 删除一个文件，无返回值
webdav.delete(path='filename')

# 移动一个文件
# 成功时的返回值为 {'success': True, 'result': ''}
# 失败时的返回值为 {'success': False, 'result': ErrorCode}
webdav.move(path='filename', new_path='newfilename')

# 复制一个文件
# 成功时的返回值为 {'success': True, 'result': ''}
# 失败时的返回值为 {'success': False, 'result': ErrorCode}
webdav.copy(path='filename', new_path='newfilename')

# 检查一个文件是否存在，返回一个 bool 值
webdav.exists(rmote_path='filename')

# 上传一个文件
# 成功时的返回值为 {'success': True, 'result': ''}
# 失败时的返回值为 {'success': False, 'result': ErrorCode}
webdav.upload(filename='local_filename', rmote_path='target_filename')

# 下载一个文件
# 成功时的返回值为 {'success': True, 'result': ''}
# 失败时的返回值为 {'success': False, 'result': ErrorCode}
webdav.download(rmote_path='rmote_filename', local_path='save_filename')
```
