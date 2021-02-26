import hashlib,base64

class UserService():

    # 產生auth code
    @staticmethod
    def geneAuthCode(user_info):
        m = hashlib.md5()
        str = "%s-%s-%s-%s"%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        # 產生md5
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def genePwd(pwd,salt):
        # 啟動md5
        m= hashlib.md5()
        str="%s-%s"%( base64.encodebytes(pwd.encode("utf-8")),salt)
        # 產生md5
        m.update(str.encode("utf-8"))
        return m.hexdigest()