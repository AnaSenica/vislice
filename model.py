import random
import json

STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'O'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'S'

class Igra:

    def __init__(self, geslo, crke = None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
    
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    
    def pravilne_crke(self):
        return [c for c in self.crke if  c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
            else:
                pass
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        delni = ''
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

#with open('u:\\UVOD V PROGRAMIRANJE\\9. Repozitorij\\vislice\\besede.txt', 'r', encoding = 'utf-8') as datoteka_z_besedami:
#    bazen_besed = [vrstica.strip().upper() for vrstica in datoteka_z_besedami]

#originalno smo napisali samo with open('besede.txt', ...), pa ni delalo. Zato smo potem
# napisali celo pot do te datoteke in je delalo (nekaterim je že prej)

#def nova_igra():
#    return Igra(random.choice(bazen_besed))

class Vislice:

    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_z_besedami = datoteka_z_besedami

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding = 'utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre) : (Igra(igre[id_igre]['geslo'], igre[id_igre]['crke']), igre[id_igre]['poskus']) for id_igre in igre}
        return

    def zapisi_igro_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding = 'utf-8') as f:
            igre = ({id_igre :  {'geslo': igra.geslo, 'crke': igra.crke, 'poskus': poskus} for id_igre, (igra, poskus) in self.igre.items()})
            json.dump(igre, f)
        return
    
    #za zgornji dve funkciji moramo importati json
    # ne moremo kar dati igro v json, moramo najprej zapisati 
    # tisto, kar bo json znal shraniti: torej slovar

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
        
    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        with open(self.datoteka_z_besedami, 'r', encoding = 'utf-8') as f:
            bazen_besed = [vrstica.strip().upper() for vrstica in f]
        igra = Igra(random.choice(bazen_besed))
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igro_v_datoteko()
        return id_igre
    


    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)
        self.zapisi_igro_v_datoteko()
        return


#vislice = Vislice()
#moj_id_igre = vislice.nova_igra()
#print(vislice.igre[moj_id_igre])
#vislice.ugibaj(moj_id_igre, 'A')
#print(vislice.igre[moj_id_igre])
#print(vislice.igre)




# testno_geslo = 'požrtvovalnost'.upper()
# testne_crke = ['A', 'E', 'O', 'P']
# igra = Igra(testno_geslo, testne_crke)
# print(igra.napacne_crke())
# print(igra.pravilne_crke())
# print(igra.stevilo_napak())
# print(igra.zmaga())
# print(igra.poraz())
# print(igra.pravilni_del_gesla())
# print(igra.nepravilni_ugibi())
# print(' ')

# zmagovalne_crke = [x for x in testno_geslo]
# zmagna_igra = Igra(testno_geslo, zmagovalne_crke)
# print(zmagna_igra.zmaga())
# print(zmagna_igra.poraz())
# print(zmagna_igra.pravilni_del_gesla())
# print(' ')

# poskus = igra.ugibaj('r')
# print(poskus)
# print(igra.pravilni_del_gesla())


