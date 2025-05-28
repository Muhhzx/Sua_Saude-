from flask import Flask
from extensions import db
from controllers.agua_controller import agua_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
app.config['SECRET_KEY'] = 'chave_super_segura'

db.init_app(app)  # inicializa o db aqui

app.register_blueprint(agua_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
