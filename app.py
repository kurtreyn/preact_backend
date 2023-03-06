from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time
from convert_pdf import create_pdf
from create_email import create_email

app = Flask(__name__)

cors = CORS(app)


@app.route("/", methods=["GET", "POST"])
def posts():
    post_req = request.get_json()
    if post_req:
        create_pdf(post_req)

        sender = post_req["company_name"]
        sender_email = post_req["email"]
        file_name = post_req["form_id"]
        absolute_path = os.path.dirname(__file__)
        relative_path = "sent-pdf/"
        full_path = os.path.join(absolute_path, relative_path)
        file_ref = f"{full_path}{file_name}.pdf"

        def delete_file():
            try:
                time.sleep(10)
                print(f'DELETING FILE: {file_ref}')
                os.remove(file_ref)
            except Exception as err:
                print(f"Error deleting file: {err}")

        try:
            create_email(file_name, full_path, sender, sender_email)
            delete_file()

        except OSError as error:
            print(f"error: {error}")
            return error

        data = {'responding_with': 'post complete'}
        return jsonify(data), 200


@app.route("/wakeup", methods=["GET", "POST"])
def responder():
    print('WAKING UP SERVER')

    data = {'responding_with': 'server is good to go'}
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)