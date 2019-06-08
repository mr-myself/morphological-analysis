from flask import Flask, request, render_template
import MeCab

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
  mecab = MeCab.Tagger ('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

  default_text = "Let's type a sentence you would like to analyze."
  target = request.form['text'] if request.form['text'] else default_text

  mecab.parse('') # avoid GC
  node = mecab.parseToNode(target)

  result = []
  while node:
    word = node.surface
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word, pos))
    result.append([word, pos])

    node = node.next

  return render_template('index.html', result=result, target=target)
