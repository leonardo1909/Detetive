import pdb
import random

suspeitos = iter(list((
    'Charles B. Abbage',
    'Donald Duck Knuth',
    'Ada L. Ovelace',
    'Alan T. Uring',
    'Ivar J. Acobson',
    'Ras Mus Ler Dorf'
)))

locais = iter(list((
    'Redmond',
    'Palo Alto',
    'San Francisco',
    'Tokio',
    'Restaurante no Fim do Universo',
    'São Paulo',
    'Cupertino',
    'Helsinki',
    'Maida Vale',
    'Toronto'
)))

armas = iter(list((
    'Peixeira',
    'DynaTAC 8000X',
    'Trezoitão',
    'Trebuchet',
    'Maça',
    'Gládio'
)))

crime = {
    'suspeito': 'Donald Duck Knuth',
    'local': 'Tokio',
    'arma': 'Trezoitão'
}


class Testemunha:

    def RespostaCrime(crime, teoria):
        if crime == teoria:
            return 0

        erros = []
        if crime['suspeito'] != teoria['suspeito']:
            erros.append(1)
        if crime['local'] != teoria['local']:
            erros.append(2)
        if crime['arma'] != teoria['arma']:
            erros.append(3)
        # pdb.set_trace()
        return random.choice(erros)


class Detetive:

    def __init__(self, teoria, crime):
        self.teoria = teoria
        self.crime = crime

    def interrogar(self, testemunha):
        return testemunha.RespostaCrime(self.crime, self.teoria)


testemunha = Testemunha
teoria = {
    'suspeito': next(suspeitos),
    'local': next(locais),
    'arma': next(armas)
}

detetive = Detetive(teoria, crime)

solucionado = False

while not solucionado:
    resposta = detetive.interrogar(testemunha)
    try:
        if resposta == 1:
            teoria['suspeito'] = next(suspeitos)
        if resposta == 2:
            teoria['local'] = next(locais)
        if resposta == 3:
            teoria['arma'] = next(armas)
        if resposta == 0:
            print(
                "Busted!! %s assassinou uma pessoa em %s com um(a) %s",
                (teoria['suspeito'], teoria['local'], teoria['arma'])
            )
        # pdb.set_trace()
    except StopIteration:
        print("Esse crime é muito complexo para esse humilde detetive. :(")
        break


# pdb.set_trace()
