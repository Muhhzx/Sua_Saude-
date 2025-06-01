from flask import Blueprint, request, render_template
from planner import gerar_plano_simples 

plano_bp = Blueprint('plano', __name__)

@plano_bp.route('/resultado', methods=['POST'])
def resultado():
    objetivo = request.form['objetivo']
    plano = gerar_plano_simples(objetivo)
    return render_template('resultado.html', objetivo=objetivo, plano=plano)
