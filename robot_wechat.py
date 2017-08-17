from wxpy import *
api_key = '9e0c5ed86ecb4f50a2cd04d8eb22dc43'
#微信登录
robot = Bot()
#信息注册
@robot.register()
def Reply(msg):
    reply = Tuling(api_key=api_key).reply_text(msg,to_member=True)
    return reply
#监听
robot.start()