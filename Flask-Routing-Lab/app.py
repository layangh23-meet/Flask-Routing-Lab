from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
@app.route('/')
def mainpage():
    return render_template("home.html")

@app.route('/product')
def product():
    return render_template("product.html")



if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
