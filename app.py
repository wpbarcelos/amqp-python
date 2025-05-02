import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
import init_db

app =  Flask(__name__, instance_path= os.path.abspath('./'))

from routes import *

if __name__ == '__main__':
    
    init_db.init_db()    
    print('Server is running...')
    app.run()