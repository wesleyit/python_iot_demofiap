from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from iron_cache import IronCache
app = Flask(__name__)
Bootstrap(app)
cache = IronCache(project_id="57e7006d1e0aa6000858dc32",
                  token="Dcc5Bq9UWP1qtQuERZXF")
cache.name = 'IoT_Demo'


@app.route('/', methods=['GET'])
def ler_estado():
    try:
        item = cache.get(key="estado")
        print("Item %s obtido via API") % item
        estado = item.value
    except:
        estado = "estado_verde"
    return render_template('index.html', estado=estado)


@app.route('/', methods=['POST'])
def gravar_estado():
    estado = request.form['estado']
    cache.put(key="estado", value=estado)
    return redirect(url_for('ler_estado'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
