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
app.config['MONGO_URI'] = 'mongodb+srv://dbDamisa:damisa.25@nlp-ipjo1.mongodb.net/db?retryWrites=true&w=majority'

mongo = PyMongo(app)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/qa', methods=['GET', 'POST'])
def question_answer():

    words = {}
    for word in mongo.db.words_db.find({},{"_id":0}):
        words.update(word)
    words = [v for v in words.keys()] 
    docs = {}
    for doc in mongo.db.docs_db.find({},{"_id":0}):
        docs.update(doc)
    inverted_index = {}
    for index in mongo.db.invertedIndex_db.find({},{"_id":0}):
        inverted_index.update(index)

    response_object = ''
    question1 = []
    answer = ''
    terms = []
    er = 'Please give more informations'
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
        if not terms:
            response_object = er
            print(response_object)
            return jsonify(response_object)
        filename_extracted = question_preprocessing.file_reranking(extracted_keywords,terms,words,docs,inverted_index)
        if not filename_extracted:
            answer = filename_extracted
        else:
            pos_question_check = defaultdict(list)
            for tag,value in pos_question.items():
                for v in value:
                    if v in docs[filename_extracted]:
                        pos_question_check[tag].append(v)
            answer = answer_extraction.answer_extraction(str(question1), pos_question_check, filename_extracted )
        if answer:
            response_object = answer
        else:
            response_object = 'Sorry, this program cannot answer this question'
        print(response_object)
    else:
        response_object = None
        
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()