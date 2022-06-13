from flask import Flask,request,render_template
import pickle


app=Flask(__name__)

@app.route('/hi')
def helllo():
    return 'Working till now'
@app.route('/pre',methods=["GET","POST"])
def predictions():
    if request.method=="POST":
        N=request.form["Ni"]
        P=request.form['Ph']
        K=request.form['Po']
        temperature=request.form["temp"]
        humidity=request.form['hu']
        ph=request.form['ph']
        rainfall=request.form['rf']
        model=model1 = open('C:\\Mba notes\\novels\\AWS\\Harvest\\models\\m1.pkl', "rb")
        model=pickle.load(model)
        predict=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
        print(predict)
    else:
        predict=None
    return render_template('happy crops.html',best=predict)

if __name__=="__main__":
    app.run(debug=True)