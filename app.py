from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/genre', methods=['GET','POST'])
def genre():
    return render_template('genre.html')

@app.route('/comedy', methods=['GET','POST'])
def comedy():
    return render_template('comedy.html')

@app.route('/drama', methods=['GET','POST'])
def drama():
    return render_template('drama.html')

@app.route('/horror', methods=['GET','POST'])
def horror():
    return render_template('horror.html')

@app.route('/romance', methods=['GET','POST'])
def romance():
    return render_template('romance.html')

@app.route('/history', methods=['GET','POST'])
def history():
    return render_template('history.html')

@app.route('/mangal', methods=['GET','POST'])
def mangal():
    test = "The sentiment of your review displays here."
    if request.method == 'POST':
        try:
            res = request.form['text1']
            blob = TextBlob(res)
            v,s = blob.sentiment
            if res != " ":
                if v < 0:
                    test = "Negative"
                else:
                    test = "Positive"
            else:
                test = "Please enter the review!"

            return render_template('mangal.html', result = test)

        except Exception as e:
            return render_template('mangal.html', result = e)
    else:
        try:
            res = request.args.get('text1')
            blob = TextBlob(res)
            v,s = blob.sentiment
            if res != " ":
                if v < 0:
                    test = "Negative"
                else:
                    test = "Positive"
            else:
                test = "Please enter the review!"
  	
            return render_template('mangal.html', result = test)

        except Exception as e:
            return render_template('mangal.html', result = e)
            

@app.route('/kabir', methods=['GET','POST'])
def kabir():
    test = "The sentiment of your review displays here."
    if request.method == 'POST':
        try:
            res = request.form['text1']
            blob = TextBlob(res)
            v,s = blob.sentiment
            if res != " ":
                if v < 0:
                    test = "Negative"
                else:
                    test = "Positive"
            else:
                test = "Please enter the review!"

            return render_template('kabir.html', result = test)

        except Exception as e:
            return render_template('kabir.html', result = e)
    else:
        try:
            res = request.args.get('text1')
            blob = TextBlob(res)
            v,s = blob.sentiment
            if res != " ":
                if v < 0:
                    test = "Negative"
                else:
                    test = "Positive"
            else:
                test = "Please enter the review!"
  	
            return render_template('kabir.html', result = test)

        except Exception as e:
            return render_template('kabir.html', result = e)


if __name__=='__main__':
    app.run(debug=True)
