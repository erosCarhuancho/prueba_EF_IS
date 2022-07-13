from flask import Flask, jsonify
from mensajes import topicos
# create the Flask app
app = Flask(__name__)

@app.route('/mensaje', methods=['GET'])
def getMensajes():
    return jsonify({'mensajes': topicos})

@app.route('/mensaje/<string:mensaje_topico>')
def getMensaje(mensaje_topico):
    mensajes = [x for x in topicos if x['topico'] == mensaje_topico.lower()]
    if (len(mensajes) > 0):
        return jsonify({'Mensaje': mensajes})
    return jsonify({'Mensaje': 'El mensaje no se obtuvo'})

if __name__ == '__main__':

    app.run(debug=True, port=5000)