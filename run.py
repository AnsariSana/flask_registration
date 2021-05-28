from registration import app

# app.run()
if __name__ == '__main__':
    #app.jinja_env.cache = {}
    app.run(debug = True, host='0.0.0.0', threaded=True)
