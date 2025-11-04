from flask import Flask, render_template, jsonify
import random

# 确保 Flask 实例名是 'app'
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

# 首页路由：渲染主页面
@app.route('/')
def index():
    return render_template('index.html')

# API 路由：提供随机提示数据给前端 JavaScript
@app.route('/get_tip')
def get_tip():
    tip = random.choice(TIPS)
    bg = random.choice(BG_COLORS)
    return jsonify({'tip': tip, 'bg': bg})

<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == '__main__':
    app.run(debug=True)
=======
    # 提示文字列表（已添加新内容）
    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
        '梦想成真', '期待下一次见面', '金榜题名',
        '顺顺利利', '早点休息', '愿所有烦恼都消失',
        '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服'
    ]
    tip = random.choice(tips)

    # 多样的背景颜色
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)

    # 创建标签并显示文字
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()

    # 窗口置顶显示
    window.attributes('-topmost', True)
    window.mainloop()

# 创建线程列表
threads = []
# 窗口数量（根据屏幕大小可调整）
for i in range(300):
    t = threading.Thread(target=show_warm_tip)
    threads.append(t)
    time.sleep(0.005)  # 快速弹出窗口
    threads[i].start()
>>>>>>> be3a8e38da73c2ed99b8fa7f5b53cb6338e2ac37
=======
if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 73b7b631ca46f659fc6ac8613df37dd2af5e8b06
