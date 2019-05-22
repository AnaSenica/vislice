import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'u:\\UVOD V PROGRAMIRANJE\\9. Repozitorij\\vislice\\views')
# Tole smo skopirali z interneta, ker ne najde templatea spodaj v funkciji
#@bottle.get('/')
#def index():
#    return bottle.template('index.tpl')
# Poskusili smo napisati absolutno pot, kot je tale v zgornji funkciji, pa ne dela to v bottlu.
# Dela le relativna pot, torej ta index.py. Zato smo uvozili to funkcijo, da smo izpisali absolutno
# pot. Ne bo pa to delalo, če odpremo na drugem računalniku. Doma zakomentiraj tole zgoraj:
#  bottle.TEMPLATE_PATH.insert(0, 'u:\\UVOD V PROGRAMIRANJE\\9. Repozitorij\\vislice\\views')
# in bi moralo normalno delati.  


vislice = model.Vislice()
id_testne_igre = vislice.nova_igra()
vislice.ugibaj(id_testne_igre, 'N')

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.get('/igra')
def testna_igra():
    return bottle.template('igra.tpl', igra = vislice.igre[id_testne_igre][0], id_igre = id_testne_igre, poskus = vislice.igre[id_testne_igre][1])

@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    return bottle.template('igra.tpl', igra = vislice.igre[id_igre][0], id_igre = id_igre, poskus = vislice.igre[id_igre][1])

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka_za_ugib = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka_za_ugib)
    bottle.redirect('/igra/{0}/'.format(id_igre))
# getunicode da nam delajo č, š, ž na spletni strani

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root = 'u:\\UVOD V PROGRAMIRANJE\\9. Repozitorij\\vislice\\img')

bottle.run(reloader=True, debug=True)