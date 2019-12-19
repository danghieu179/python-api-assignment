# config
DB_NAME = 'demo'
DB_USER = 'demo'
DB_PWD = 'demo'
DB_HOST = 'localhost'

DATABASE_URL = 'postgresql+psycopg2://%s:%s@%s/%s' % (
    DB_USER, DB_PWD, DB_HOST, DB_NAME)
print('=================> DATABASE_URL: ', DATABASE_URL)

PAGE_SIZE = 10