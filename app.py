from flask import Flask
from extensions import db
from controllers.agua_controller import agua_bp
from controllers.plano_controller import plano_bp
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
app.config['SECRET_KEY'] = 'chave_super_segura'

db.init_app(app) 

app.register_blueprint(agua_bp)
app.register_blueprint(plano_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
