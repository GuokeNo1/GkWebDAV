import os
import urllib
import urllib3
import base64
import xml.etree.cElementTree as xml

urllib3.disable_warnings()
def getattr(e, name, default=None):
    child = e.find('.//{DAV:}' + name)
    if child is None:
        return default
    else:
        return child.text


def element2fileinfo(e):
    return {
        'path': urllib.parse.unquote(getattr(e, 'href')),
        'length': int(getattr(e, 'getcontentlength', 0)),
        'lastmodified': getattr(e, 'getlastmodified', ''),
        'type': getattr(e, 'getcontenttype', ''),
    }

class webHelper:
    def __init__(self, headers={}):
        self.headers = headers
    def httpRequest(self, method, url, data=None, headers=None):
        theaders = self.headers.copy()
        if headers != None:
            for key in headers:
                theaders[key] = headers[key]
        manager = urllib3.PoolManager()
        response = manager.request(method, url, headers=theaders, body=data)
        return response

class Gkwebdav:
    def __init__(self, url, username, password):
        self.author = self.__toAuthor(username, password)
        self.username = username
        self.url = url.rstrip('/')
        self.webdev = webHelper(headers={"Authorization": self.author, 'Accept': 'application/json'})
        self.cwd = '/'

    def cd(self, path):
        path = path.strip()
        if not path:
            return
        newpath = '/'.join(part for part in path.split('/') if part) + '/'
        if newpath == '/':
            self.cwd = newpath
        elif path.startswith('/'):
            self.cwd = '/' + newpath
        else:
            self.cwd += newpath

    def __getRequestUrl(self, path):
        path = str(path).strip()
        if path.startswith('/'):
            return self.url + urllib.parse.quote(path)
        return "".join((self.url, urllib.parse.quote(self.cwd), urllib.parse.quote(path))).rstrip('.')

    def ls(self, path='.'):
        response = self.webdev.httpRequest('PROPFIND', url=self.__getRequestUrl(path))
        if len(response.data) == 0:
            return {'success': False, 'result': ''}
        tree = xml.fromstring(response.data)
        if response.status < 250:
            return {'success': True, 'result': [element2fileinfo(e) for e in tree.findall('{DAV:}response')]}
        else:
            return {'success': True, 'result': 'HTTP_STATUS_' + str(response.status)}

    def mkdir(self, path):
        self.webdev.httpRequest('MKCOL', url=self.__getRequestUrl(path))

    def mkdirs(self, path):
        paths = [p for p in path.split('/') if p]
        if not paths:
            return
        if path.startswith('/'):
            paths[0] = '/' + paths[0]
        oldcwd = self.cwd
        try:
            for p in paths:
                try:
                    self.mkdir(p)
                except:
                    pass
                finally:
                    self.cd(p)
        finally:
            self.cd(oldcwd)

    def rmdir(self, path):
        path = str(path).rstrip('/') + '/'
        self.webdev.httpRequest('DELETE', url=self.__getRequestUrl(path))

    def delete(self, path):
        self.webdev.httpRequest('DELETE', url=self.__getRequestUrl(path))

    def upload(self, filename, rmote_path):
        if not os.path.exists(filename):
            return {'success': False, 'result': 'File is not exist'}
        with open(filename, 'rb') as readfile:
            response = self.webdev.httpRequest('PUT', url=self.__getRequestUrl(rmote_path), data=readfile.read())
            if len(response.data) == 0:
                return {'success': True, 'result': ''}
            elif response.status == 403:
                return {'success': False, 'result': 'The operation is not allowed on this location'}
            elif response.status == 404:
                return {'success': False, 'result': 'The resource of this location does not exist'}
            else:
                return {'success': False, 'result': 'Unknown'}

    def download(self, rmote_path, local_path):
        response = self.webdev.httpRequest('GET', url=self.__getRequestUrl(rmote_path))
        if response.status == 200:
            with open(local_path, 'wb') as writer:
                writer.write(response.data)
            return {'success': True, 'result': ''}
        else:
            return {'success': True, 'result': 'HTTP_STATUS_'+str(response.status)}

    def exists(self, rmote_path):
        response = self.webdev.httpRequest('HEAD', url=self.__getRequestUrl(rmote_path))
        return True if response.status != 404 else False

    def copy(self, path, new_path):
        response = self.webdev.httpRequest('COPY', url=self.__getRequestUrl(path), headers={'Destination': self.__getRequestUrl(new_path)})
        if response.status < 250:
            return {'success': True, 'result': ''}
        else:
            return {'success': True, 'result': 'HTTP_STATUS_'+str(response.status)}

    def move(self, path, new_path):
        response = self.webdev.httpRequest('MOVE', url=self.__getRequestUrl(path), headers={'Destination': self.__getRequestUrl(new_path)})
        if response.status < 250:
            return {'success': True, 'result': ''}
        else:
            return {'success': True, 'result': 'HTTP_STATUS_'+str(response.status)}

    def __toAuthor(self, username, password):
        aut = "{0}:{1}".format(username, password)
        aut = base64.b64encode(aut.encode())
        aut = 'Basic ' + aut.decode()
        return aut



