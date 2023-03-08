import os
from sqlalchemy import create_engine, text

db_connection_str = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from docs"))
  list = []
  for row in result.all():
    print(type(row[2]))
