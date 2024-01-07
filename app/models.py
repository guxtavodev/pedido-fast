from app import db, app


class Cliente(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  telefone = db.Column(db.String(20))
  ip = db.Column(db.String(20)) # aqui o número da mesa

  def __init__(self, nome, email, telefone, ip):
    self.nome = nome
    self.email = email
    self.telefone = telefone
    self.ip=ip

class Produto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  preco = db.Column(db.Float)
  quantidade = db.Column(db.Integer)

  def __init__(self, nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

class Pedido(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cliente = db.Column(db.Integer)
  produto = db.Column(db.Integer)
  quantidade = db.Column(db.Integer)
  valor = db.Column(db.Float)

  def __init__(self, cliente, produto, quantidade, valor):
    self.cliente = cliente
    self.produto = produto
    self.quantidade = quantidade
    self.valor = valor

class Funcionarios(db.Model):
  nome = db.Column(db.String(100))
  id = db.Column(db.Integer, primary_key=True)
  pedidos = db.Column(db.Integer)
  restaurante = db.Column(db.Integer)

  def __init__(self, nome, id, pedidos, restaurante):
    self.nome = nome
    self.id = id
    self.pedidos = pedidos
    self.restaurante = restaurante

with app.app_context():
  db.create_all()