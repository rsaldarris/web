from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

#cultivo = [
#    {'codigo': 201811248010,'longitud':56.234,'latitud':75.0909,'producto':'Leche', 'area': 98, 'imag':'https://ichef.bbci.co.uk/news/ws/660/amz/worldservice/live/assets/images/2014/11/05/141105131956_leche_624x351_thinkstock.jpg'},
#    {'codigo': 201810328010,'longitud':45.6576,'latitud':76.090,'producto':'Cacao', 'area': 32, 'imag':'https://concepto.de/wp-content/uploads/2018/08/cacao-e1533849112880.jpg'}
#]

producto_list = ['Leche','Cacao','Carne','Flores','Hortalizas']

@app.route('/listarCultivo',methods = ['GET']) 
def listarCultivos():
    cultivos = requests.get('http://localhost:5000/tipoCultivo').json()
    return render_template('listarCultivo.html',cultivos = cultivos)

@app.route('/crearCultivo',methods= ['GET'])
def crearCultivo():
    return render_template('crearCultivo.html',variables = producto_list)


@app.route('/guardarCultivo',methods= ['POST'])
def guardarSensor():
    sensor = dict (request.values)
    sensor['codigo'] = int(sensor['codigo'])
    sensor['latitud'] = float(sensor['latitud'])
    sensor['longitud'] = float(sensor['longitud'])
    sensor['area'] = int(sensor['area'])
    requests.post('http://localhost:5000/tipoCultivo',json=sensor)
    print("GUARDAR")
    return (listarCultivos())

#app.run(port=8000,debug = True)
