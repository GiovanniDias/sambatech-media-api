def test_db_connection(db):
    # For sqlite database, if it does not exist, a file 
    # with its name will be created when execute engine
    assert db.engine.execute('SELECT 1') is not None
