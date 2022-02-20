import random
from domain.loja import Loja

class Cliente(object):

  _HORA = "hora"
  _DIA = "dia"
  _SEMANA = "semana"
  _MODALIDADES = {_HORA:3600, _DIA:24*3600, _SEMANA:7*24*3600}

  def __init__(self, nome):
    self._id = random.randint(1,999) #simulando a geraçao de id único para loja
    self.nome = nome
    self.hora_aluguel = None
    self.quantidade = None
    self.modalidade = None
    self._base_locacao = None
    self._duracao_locacao = None

    print(f"Classe Cliente | Metodo Construtor | Cria instância de cliente\n{self}\n")

  def __repr__(self)->str:
    return f"[Cliente -> id:{self._id}|nome:{self.nome}|quantidade:{self.quantidade}|duracao_locacao:{self._duracao_locacao}|modalidade:{self.modalidade}|hora alguel:{self.hora_aluguel}]"

  def alugar(self, quantidade, modalidade, loja:d.Loja):
    if not isinstance(loja, d.Loja):
      raise ValueError(f'Erro | Classe Cliente | Metodo alugar | parametro loja inválido. Tipo {type(loja)}')

    print(f"Classe Cliente | Metodo alugar | Cliente {self.nome} solicita o aluguel de {quantidade} de bicicletas na modalidade {modalidade} a loja {loja.nome}\n{self}\n")

    if modalidade not in self._MODALIDADES:
      raise ValueError(f"Erro | Classe Locacao | Metodo Construtor | Modalidade Inválida")
    else:
      self.modalidade = modalidade
      self._base_locacao = self._MODALIDADES.get(modalidade)
    self.quantidade = quantidade
    return loja.locar(self)

  def devolver(self, loja:d.Loja)->float:
    print(f"Classe Cliente | Metodo devolver | Cliente {self.nome}  devolve os produtos a {loja.nome}\n{self}\n")
    valor_locacao = loja.receber(self)
    print(f"Classe Cliente | Metodo devolver | Cliente {self.nome}  recebe da {loja.nome} o valor total da locação R${valor_locacao}\n{self}\n")
    return valor_locacao

  def ler_estoque(self, loja:d.Loja)->int:
    if not isinstance(loja, d.Loja):
      raise ValueError(f'Erro | Classe Cliente | Metodo ler_estoque | parametro loja inválido. Tipo {type(loja)}')
    print(f"Classe Cliente | Metodo ler_estoque | Cliente {self.nome} vê o estoque da loja {loja.nome}\n{self}\n")
    return loja.mostrar_estoque()

  @property
  def duracao_locacao(self):
    return self._duracao_locacao

  @duracao_locacao.setter
  def duracao_locacao(self, duracao):
    self._duracao_locacao = duracao
