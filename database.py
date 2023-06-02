from sqlalchemy import create_engine,text

db_connection_string={  create_engine("mysql+pymysql://uk7bg6n6qjx5s9g379h5:pscale_pw_Ftzy7UhC3xGlM13jXrFR0pSOZJhXLcBK2S6wSEaFBx2@aws.connect.psdb.cloud/okaracareer?charset=utf8b4")
             }

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "etc/ssl/cert.perm"
    }
  }
)


with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())



