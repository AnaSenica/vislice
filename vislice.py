import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'u:\\UVOD V PROGRAMIRANJE\\9. Repozitorij\\vislice\\views')

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')


bottle.run(reloader=True, debug=True)