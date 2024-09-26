from flask import Flask, render_template, jsonify, request
from get_data import DataGetter

app = Flask(__name__)

"""
---------------static hosting ----------------------------
first just load (i.e. render) the default main.html 
"""
@app.route('/')
def homepage():
    return render_template("main.html")


"""
---------------create API endpoints ----------------------
"""
@app.route('/api/v1/get_ridings', methods=['GET'])
def get_ridings():
    """
    very basic API endpoint with no input
    """
    return jsonify(DG.get_ridings())

@app.route('/api/v1/get_riding_info', methods=['GET'])
def get_riding_info():
    if 'riding_id' in request.args:
        riding_id = int(request.args['riding_id'])
        return jsonify(DG.get_riding_info(riding_id))
    else:
        return "Error: no riding_id field provided"

@app.route('/api/v1/get_riding_candidates', methods=['GET'])
def get_riding_candidates():
    if 'riding_id' in request.args:
        riding_id = int(request.args['riding_id'])
        return jsonify(DG.get_riding_candidates(riding_id))
    else:
        return "Error: no riding_id field provided"




if __name__ == "__main__":
    DG = DataGetter()
    app.run(debug = True, passthrough_errors=True)
