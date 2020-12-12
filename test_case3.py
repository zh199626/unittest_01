import unittest

# 使用TestCase
from login import get_username,get_password

version = 2.0
class TestLogin(unittest.TestCase):
    # 类的初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print('执行类之前调用一次')
    # 类的清空方法
    @classmethod
    def tearDownClass(cls) -> None:
        print('执行类之后调用一次')


    # 初始化方法
    def setUp(self) -> None:
        print('每次执行测试用例前执行')
    # 清空方法
    def tearDown(self) -> None:
        print('每次执行测试用例后执行')


    def test_login_username(self):
        print('获取用户名测试用例')
        # 预期结果 ： 自己登录的账号
        expect_username = 'test01'
        # 实际结果 ： 显示在页面上的账号
        acutl_username = get_username()
        self.assertEqual(expect_username,acutl_username)
        # assert expect_username == acutl_username

    @unittest.skipIf(version>3.0,'执行此用例')
    def test_login_password(self):
        print('获取密码测试用例')
        # 预期结果 ：自己登录的密码
        expect_password = 'test02'
        # 实际结果 ：显示在页面上的密码
        acutl_password = get_password()
        self.assertEqual(expect_password,acutl_password)
        # assert expect_password == acutl_password

# unittest.main()

y = TestLogin
# 1.通过TestSuite中的addTest去添加测试用例 （创建一个套件对象）
# x = unittest.TestSuite()

# 添加一条测试用例 ：addTest
# x.addTest(y('test_login_username'))
# x.addTest(y('test_login_password'))

# 添加多条测试用例
# lst = [y('test_login_username'),y('test_login_password')]
# x.addTests(lst)


# 2.使用TestLoader中的discover来执行测试用例 （创建一个套件对象）
suite = unittest.TestLoader().discover('.',pattern='test*.py')

z = unittest.TextTestRunner()
z.run(suite)









