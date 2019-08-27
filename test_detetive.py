import pytest
from detetive import Detetive, Testemunha

suspeitos = iter(list(
    'Charles B. Abbage',
    'Donald Duck Knuth',
    'Ada L. Ovelace',
    'Alan T. Uring',
    'Ivar J. Acobson',
    'Ras Mus Ler Dorf'
))

locais = iter(list(
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
))

armas = iter(list(
    'Peixeira',
    'DynaTAC 8000X',
    'Trezoitão',
    'Trebuchet',
    'Maça',
    'Gládio'
))


crime = {
    'suspeito': 'Donald Duck Knuth',
    'local': 'Tokio',
    'arma': 'trezoitão'
}

testemunha = Testemunha
teoria = {
    'suspeito': next(suspeitos),
    'local': next(locais),
    'arma': next(armas)
}

detetive = Detetive(teoria, crime)


def test_answer():
    assert detetive.interrogar(testemunha) == 0
