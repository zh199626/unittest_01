import unittest

# 使用TestCase
from login import get_username,get_password

class TestLogin(unittest.TestCase):

    def test_login_username(self):
        expect_username = 'test01' # 预期结果 ： 自己登录的账号
        acutl_username = get_username() # 实际结果 ： 显示在页面上的账号
        self.assertEqual(expect_username,acutl_username)
        # assert expect_username == acutl_username

    def test_login_password(self):
        expect_password = 'test02' # 预期结果 ：自己登录的密码
        acutl_password = get_password() # 实际结果 ：显示在页面上的密码
        self.assertEqual(expect_password,acutl_password)
        # assert expect_password == acutl_password

# unittest.main()

# y = TestLogin
# 1.通过TestSuite中的addTest去添加测试用例 （创建一个套件对象）
# x = unittest.TestSuite()

# 添加一条测试用例 ：addTest
# x.addTest(y('test_login_username'))x
# x.addTest(y('test_login_password'))

# 添加多条测试用例
# lst = [y('test_login_username'),y('test_login_password')]
# x.addTests(lst)


# 2.使用TestLoader中的discover来执行测试用例 （创建一个套件对象）
suite = unittest.TestLoader().discover('.',pattern='test*.py')

x = unittest.TextTestRunner()
x.run(suite)



