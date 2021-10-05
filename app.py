from flask import Flask, request, jsonify
from flask_cors import CORS
import recommend
const PORT=process.env.PORT||'8080'

app = Flask(__name__)
CORS(app) 
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
        res = recommend.results(request.args.get('title'))
        return jsonify(res)

if __name__=='__main__':
        app.run(port = PORT, debug = True)
