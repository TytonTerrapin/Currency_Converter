from flask import Flask, render_template, request

app = Flask(__name__)

rates = {
    'USD': 1.0,
    'EUR': 1.18,
    'GBP': 1.38,
    'JPY': 0.0075,
    'AUD': 0.67,
    'CAD': 0.75,
    'INR': 0.012,
    'CHF': 1.09,
    'CNY': 0.14,
    'MXN': 0.050,
    'BRL': 0.18,
    'ZAR': 0.053,
    'NZD': 0.63,
    'SEK': 0.11,
    'NOK': 0.10,
    'KRW': 0.00076,
    'RUB': 0.013,
    'SGD': 0.74,
    'TRY': 0.056,
    'HKD': 0.13,
    'TWD': 0.033,
    'MYR': 0.23,
    'IDR': 0.000067,
    'PHP': 0.020,
    'THB': 0.031,
    'PKR': 0.006,
    'SAR': 0.27,
    'AED': 0.27,
    'KWD': 3.27,
    'EGP': 0.032,
    'VND': 0.000042,
    'CLP': 0.0013,
    'COP': 0.00026,
    'DZD': 0.0074,
    'QAR': 0.27,
    'OMR': 2.60,
    'BDT': 0.0094,
    'BHD': 2.65,
    'JOD': 1.41,
    'ISK': 0.0075
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_curr = request.form['from_currency']
        to_curr = request.form['to_currency']

       
        converted = round(amount * (rates[to_curr] / rates[from_curr]), 2)

        return render_template('result.html',
                               amount=amount,
                               from_curr=from_curr,
                               to_curr=to_curr,
                               result=converted,
                               currencies=rates.keys())

    return render_template('index.html', currencies=rates.keys())

if __name__ == '__main__':
    app.run(debug=True)
