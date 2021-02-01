from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def bmi_cal():
    bmi = ''
    bmi_total = ''
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = cal_bmi(weight, height)
        bmi_total = check_bmi(weight, height,bmi_total)
    return render_template("bmi_.html",bmi=bmi,bmi_total=bmi_total)

def cal_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

def check_bmi(weight, height,bmi_total):
        bmi_c = cal_bmi(weight, height)
        if bmi_c < 15:
            bmi_detail = "Very severely underweight"
        elif bmi_c >= 15 and bmi_c < 16:
            bmi_detail = "Severely underweight"
        elif bmi_c >= 16 and bmi_c < 18.5:
            bmi_detail = "Underweight"
        elif bmi_c >= 18.5 and bmi_c < 25:
            bmi_detail = "Normal (healthy weight)"
        elif bmi_c >= 25 and bmi_c < 30:
            bmi_detail = "Overweight"
        elif bmi_c >= 30 and bmi_c < 35:
            bmi_detail = "Moderately obese"
        elif bmi_c >= 35 and bmi_c < 40:
            bmi_detail = "Severely obese"
        else:
            bmi_detail = "Very severely obese"
        return bmi_detail

app.env="development"
app.run(debug=True)