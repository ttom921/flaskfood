import hashlib,base64

class UserService():
    @staticmethod
    def genePwd(pwd,salt):
        # 啟動md5
        m= hashlib.md5()
        str="%s-%s"%( base64.encodebytes(pwd.encode("utf-8")),salt)
        # 產生md5
        m.update(str.encode("utf-8"))
        return m.hexdigest()