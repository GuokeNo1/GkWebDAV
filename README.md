New webdav client for Python3+  
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
  
  
使用方法
=======================  
  
安装Gkwebdav模块  
`pip install Gkwebdav`  
  
**创建Gkwebdav对象**
```
import Gkwebdav

webdav = Gkwebdav.Gkwebdav(url='webdavurl', username='username', password='password')
```  
  
  
**cwd** `当前所在目录`
```
print(webdav.cwd)
#返回当前所在目录位置默认'/'
```  
  
  
**cd()** `进入到目录`
```
webdav.cd(path='dirname')
#无返回值
```  
  
  
**ls()** `遍历文件目录`
```
webdav.ls([path=''])
#成功返回值{'success': True, 'result': [{'path': '路径', 'length': 文件大小 , 'lastmodified': '最后的修改日期', 'type': '文件类型'}]}
#失败返回值{'success': False, 'result': '失败代码'}
```  
  
  
**mkdir()** `创建单层文件夹`
```
webdav.mkdir(path='newdirname')
#返回None,调用ls()查看是否生效
```  
  
  
**mkdirs()** `创建多层目录`
```
webdav.mkdir(path='newdirname/newdirname/...')
#返回None,调用ls()查看是否生效
```
**rmdir()** `删除目录`
```
webdav.rmdir(path='dirname')
#返回None,调用ls()查看是否生效
```  
  
  
**delete()** `删除文件`
```
webdav.delete(path='filename')
#返回None,调用ls()查看是否生效
```  
  
  
**move()** `移动文件`
```
webdav.move(path='filename', new_path='newfilename')
#成功返回值{'success': True, 'result': ''}
#失败返回值{'success': False, 'result': '失败代码'}
```  
  
  
**copy()** `复制文件`
```
webdav.copy(path='filename', new_path='newfilename')
#成功返回值{'success': True, 'result': ''}
#失败返回值{'success': False, 'result': '失败代码'}
```  
  
  
**exists()** `检查文件是否存在`
```
webdav.exists(rmote_path='filename')
#返回bool值
```  
  
  
**upload()** `文件上传`
```
webdav.upload(filename='local_filename', rmote_path='target_filename')
#成功返回值{'success': True, 'result': ''}
#失败返回值{'success': False, 'result': '失败代码'}
```  
  
  
**download()** `文件下载`
```
webdav.download(rmote_path='rmote_filename', local_path='save_filename')
#成功返回值{'success': True, 'result': ''}
#失败返回值{'success': False, 'result': '失败代码'}
```
