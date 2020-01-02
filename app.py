from flask import Flask, render_template, request, jsonify, url_for, redirect
app = Flask(__name__)

from audio import Audio

@app.route('/')
def main():
   return render_template('index.html')

@app.route('/insult')
def insult():
    Audio.randomInsult()
    return main()

@app.route('/greeting')
def greeting():
    Audio.randomGreeting()
    return redirect("/")

@app.route('/question')
def question():
    Audio.randomQuestion()
    return redirect("/")

@app.route('/carrier')
def carrier():
    Audio.randomCarrier()
    return redirect("/")

@app.route('/ender')
def ender():
    Audio.randomEnder()
    return redirect("/")

@app.route('/music')
def music():
    #Audio.playerInterface = "afplay" #Mac
    Audio.randomMusic()
    return redirect("/")

@app.route('/american')
def american():
    Audio.accent = "american"
    return redirect("/")

@app.route('/indian')
def indian():
    Audio.accent = "indian"
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
