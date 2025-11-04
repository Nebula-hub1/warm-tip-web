from flask import Flask, render_template, jsonify
import random

# 确保 Flask 实例名是 'app'，这是 Render 和 Gunicorn 约定的名称
app = Flask(__name__)

# 提示文字列表
TIPS = [
    '多喝水哦~', '保持微笑呀', '每天都要元气满满',
    '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
    '梦想成真', '期待下一次见面', '金榜题名',
    '顺顺利利', '早点休息', '愿所有烦恼都消失',
    '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服'
]

# 多样的背景颜色
BG_COLORS = [
    'lightpink', 'skyblue', 'lightgreen', 'lavender',
    'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
    'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
]

# 首页路由：渲染主页面 (Web 界面)
@app.route('/')
def index():
    return render_template('index.html')

# API 路由：提供随机提示数据给前端 JavaScript
@app.route('/get_tip')
def get_tip():
    tip = random.choice(TIPS)
    bg = random.choice(BG_COLORS)
    return jsonify({'tip': tip, 'bg': bg})

# ----------------------------------------------------
# 仅在本地开发环境中运行，Render 和 Gunicorn 会忽略这部分
# ----------------------------------------------------
if __name__ == '__main__':
    # 启用调试模式，方便本地测试
    app.run(debug=True)
