a = input("请输入内部测试人员密码：")
#如果你不是测试人并看到了这串注释文字，
#说明你正在使用非法手段查看我的代码
#请你立刻退出！
#此网站版权归属于赵墨轩同学所有，
#赵墨轩的指导教师以及亲人享有查看权
#盗版必究刑事责任！！！
#盗版必究刑事责任！！！
#盗版必究刑事责任！！！
if a == "20240409":
    from flask import Flask,render_template,request,redirect
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run()
else:
    print("您的密码不正确，请您修改密码并从新登陆或联系工作人员解决")
    print("Your password is incorrect. Please change your password and log in again or contact the staff to resolve the issue")
    print("请您拨打服务热线：13661372247")
    print("If you have question，please call working personnel at: +86 13661372247
    
#©2024-2025北京BITR工作室
