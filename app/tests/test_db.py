from flask_sqlalchemy import SQLAlchemy

def test_db_connection(app):
    db = SQLAlchemy(app)
    
    # For sqlite database, if it does not exist, a file 
    # with its name will be created when execute engine
    assert db.engine.execute('SELECT 1') is not None
