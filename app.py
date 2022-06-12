from flask import Flask
from flask_restful import Api, request
import urllib.request
from flask_cors import CORS, cross_origin
import spacy

nlp = spacy.load('my_custom_model')

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def extract_exp(text):
    exp_dict = {}
    doc = nlp(text)
    i = 0
    for ent in doc.ents:
        exp_dict[i] = ent.text
        i = i+1
    return exp_dict


@app.route('/get-exp', methods=['GET'])
@cross_origin()
def res_parser():
    args = request.args
    text = args.get('text', type=str)
    return extract_exp(text)

if __name__ == '__main__':
    app.run(debug=True)