# Using Flask to host a web-app, specifically via APIs

Flask is a simple to use web framework. This walkthrough will quickly go over a way you can stand up a REST API using Flask. For a more in-depth tutorail, feel free to check out other sources, such as [this one](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask).

## First step -- stand up a small flask app 

Say you want to host a static website

```python
from flask import Flask, render_template

app = Flask(__name__)

"""
---------------static hosting ----------------------------
first just load (i.e. render) the default main.html 
"""
@app.route('/')
def homepage():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug = True, passthrough_errors=True)
```

Running this in the console with the following [main.html](/templates/main.html) page will render a very simple static webpage.

## Second step -- prepare some data that can be queried

For instance, as part of a project to mine the candiates of the election, you saved them to a database, and you want to use the API to extract information live from the database. This follows the classic client-server model:

![server-client](/imgs/client-server-db.png)

When the client browser will query the flask app, the app will either render the static HTML page (as per above), or query the database to extract the information needed.

To demo extracting some data from the database, see the [get_data.py](get_data.py) script. Now we have 3 functions we can use to get data:
* `get_ridings()`
* `get_riding_info(riding_id=)`
* `get_riding_candidates(riding_id=)`

Lets make 3 APIs to use these data functions

## Third step -- setting up APIs

The same way you route endpoints of a URL, you can specify APIs

```python
@app.route('/api/v1/get_ridings', methods=['GET'])
def get_ridings():
    """
    very basic API endpoint with no input
    """
    return jsonify(DG.get_ridings())
```

Notice we just `jsonified` the output of the `get_ridings()` function when the "GET" call was used. Using the `methods=` argument allows your app to filter the type of requests you should get.

Take a look at the full [__init__.py](__init__.py) to see how all of them work