from flask import Blueprint, render_template, session, request, redirect, url_for
from datetime import datetime

agua_bp = Blueprint('agua', __name__)

@agua_bp.route('/')
def index():
    hoje = datetime.now().strftime('%Y-%m-%d')

    if 'data_agua' not in session or session['data_agua'] != hoje:
        session['agua_total'] = 0
        session['data_agua'] = hoje

    if 'meta_agua' not in session:
        session['meta_agua'] = 2000  # Meta padrão: 2000 mL

    return render_template('index.html', 
                           agua_total=session.get('agua_total', 0),
                           meta_agua=session.get('meta_agua', 2000))

@agua_bp.route('/adicionar_agua', methods=['POST'])
def adicionar_agua():
    ml = request.form.get('ml')

    if not ml:
        return "Erro: campo 'ml' não enviado", 400

    try:
        ml = int(ml)
    except ValueError:
        return "Erro: valor inválido para ml", 400

    session['agua_total'] += ml
    return redirect(url_for('agua.index'))

@agua_bp.route('/definir_meta', methods=['POST'])
def definir_meta():
    meta = request.form.get('meta')

    if not meta:
        return "Erro: campo 'meta' não enviado", 400

    try:
        meta = int(meta)
    except ValueError:
        return "Erro: valor inválido para meta", 400

    session['meta_agua'] = meta
    return redirect(url_for('agua.index'))
