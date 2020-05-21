from flask import Flask, jsonify, request
from flask_cors import CORS
import question_preprocessing 
import answer_extraction
import sys
from pymongo import MongoClient
from flask_pymongo import PyMongo
import pymongo
from collections import defaultdict
from pprint import pprint as pp
import uuid
import logging

logging.basicConfig(level=logging.DEBUG)


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'db'
app.config['MONGO_URI'] = 'mongodb+srv://dbDamisa:damisa.25@nlp-ipjo1.mongodb.net/test?retryWrites=true&w=majority'
"""CONNECTION_STRING = "mongodb+srv://dbDamisa:damisa.25@nlp-ipjo1.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db')
docs_col = pymongo.collection.Collection(db, 'docs_db')
words_col = pymongo.collection.Collection(db, 'words_db')
invertedIndex_col = pymongo.collection.Collection(db, 'invertedIndex_db')"""
mongo = PyMongo(app)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

""" Create connection to MongoDB database """
"""client = MongoClient('mongodb+srv://dbDamisa:damisa.25@nlp-ipjo1.mongodb.net/test?retryWrites=true&w=majority')

db = client.db
docs_col = db.docs_db
words_col = db.words_db
inverted_col = db.invertedIndex_db"""
# sanity check route
 #Example

#pp(extracted_keywords)
#pp(pos_question)
#Query words from mongoDB
terms = []

@app.route('/qa', methods=['GET', 'POST'])
def question_answer():

    words = {}
    for word in mongo.db.words_col.find({},{"_id":0}):
        words.update(word)
    words = [v for v in words.keys()] 
    docs = {}
    for doc in mongo.db.docs_col.find({},{"_id":0}):
        docs.update(doc)
    inverted_index = {}
    for index in mongo.db.invertedIndex_col.find({},{"_id":0}):
        inverted_index.update(index)
        
    print(words)
    question1 = []
    if request.method == 'POST':
        post_data = request.get_json()
        question1.append(post_data.get('question'))
        #question = question1['question']
        print(post_data)
        print(question1)

        extracted_keywords, pos_question = question_preprocessing.extract_keys(question1)
        
        for term in extracted_keywords:
            if term in words:
                terms.append(term)
        if not term:
            response_object ={'ans': ['Please give more informations']}
            return jsonify(response_object)
        filename_extracted = question_preprocessing.file_reranking(extracted_keywords,terms,words,docs,inverted_index)
        pos_question_check = defaultdict(list)
        for tag,value in pos_question.items():
            for v in value:
                if v in docs[filename_extracted]:
                    pos_question_check[tag].append(v)
        answer = answer_extraction.answer_extraction(str(question1), pos_question_check, filename_extracted )
        response_object ={'ans': answer}
    else:
        response_object ={'ans': ''}
    return jsonify(response_object).get_data(as_text=True)


if __name__ == '__main__':
    app.run()