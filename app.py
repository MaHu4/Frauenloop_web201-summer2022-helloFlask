import os
from flask import Flask, render_template, request, redirect, url_for
from forms import SampleForm

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder="static")

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    # Routes defined for this app / website
    @app.route('/hello')
    def hello():
        return 'Hello World from Python Flask!'

    @app.route('/')
    def helloRoot():
        return render_template(
            'hello.html'
        )   

    @app.route('/say-my-name') # add "?name=xx" in URL in browser to maka name appear. 
    def helloName():
        nameParam = request.args.get('name') #args hold the parameters from the URL (if they came)
                                            # the param to get()  is the name of the URL param you want to get the value of, in our example name, after the ? --> http://127.0.0.1:5000/say-my-name?name=Maria
        return render_template(
            'hello_name.html',
            personName= nameParam #statt nameParam, kann Name als String angegeben werden
        )    

    @app.route('/hello-all')
    def helloList():
        allPeople = ['July', 'Ron', 'Sandra', 'Maria']
        return render_template(
            'hello_name_list.html',
            personNamesList=allPeople #personNameList is a keyword argument so an argument/parameter to the function render_template that was given a name, personNameList is the name, the value is the list that was stored as allPeople
        )  

    @app.route('/form', methods=['GET', 'POST'])
    def form():
        form = SampleForm()  # every form needs a class which holds the data that is going to come in the form; class SampleForm links to forms.py
        if form.validate_on_submit():
            return redirect(url_for('hello'))

        return render_template(
            'sample_form.html',
            form=form
        )                        

    # @app.route('/map')
    # def map_func():
    #     return render_template('map.html')
    # if __name__ == '__main__':
    #     app.run(debug = True)    
    # End Routes

    # Return the fully initialized app
    return app


app = create_app()
if __name__ == '__main__':
    port = int(os.environ.get("PORT",8000))
    app.run(host='127.0.0.1',port=port,debug=True)