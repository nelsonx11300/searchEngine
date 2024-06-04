from flask import Flask, request, render_template
import os

app = Flask(__name__)

# 定义txt文件的目录
TXT_DIR = r''

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            results = search_files(keyword.lower())  # 将关键字转换为小写
    return render_template('index.html', results=results)

def search_files(keyword):
    result_list = []
    for filename in os.listdir(TXT_DIR):
        if filename.endswith('.txt'):
            filepath = os.path.join(TXT_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read().lower()  # 将文件内容转换为小写
                if keyword in filename.lower() or keyword in content:  # 检查文件名和文件内容
                    result_list.append({
                        'filename': filename,
                        'content': content
                    })
    return result_list

if __name__ == '__main__':
    print(f"TXT_DIR: {TXT_DIR}")
    for filename in os.listdir(TXT_DIR):
        print(f"File found: {filename}")
    app.run(debug=True)
