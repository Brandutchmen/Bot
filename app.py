from flask import Flask, render_template, request, jsonify, url_for
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
    return main()

@app.route('/starter')
def starter():
    Audio.randomStarter()
    return main()

@app.route('/carrier')
def carrier():
    Audio.randomCarrier()
    return main()

@app.route('/ender')
def ender():
    Audio.randomEnder()
    return main()

    @app.route('/greeting')
    def greeting():
        Audio.randomGreeting()
        return main()

@app.route('/music')
def music():
    #Audio.playerInterface = "afplay" #Mac
    Audio.randomMusic()
    return main()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
