# from erpapi import create_app
from PSIOT import create_app
app = create_app()


if __name__ == '__main__':
    
    # app.run(debug=True,port=app.config['PORT'])
    app.run(debug=True, host='0.0.0.0')