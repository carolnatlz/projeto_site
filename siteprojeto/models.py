from enum import unique
from siteprojeto import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) #get pode ser usado ao invés de filter_by pois é a PK

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String(32), nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)

#lazy é para passar todos os parâmetros do usuário ao chamá-lo usando o backref

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.Integer, nullable=False)
    descricao = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable= False)

#ao fazer a referência da FK na classe post é necessário passar o parâmetro com letra minúscula (classe.atributo)
#escrevendo datetime.utcnow() com parênteses ele iria pegar o valor do deploy do site e não entender como uma função

'''
Para realizar todo o processo de criação do bd, abra o terminal:
$ python
>> from siteprojeto import database
>> from siteprojeto.models import Usuario, Post
>> database.create_all()

    >> usuario = Usuario(usuario='Carol',email='carolina@gmail.com',senha='Carol@senha')
    >> database.session.add(usuario)

    >> usuario2 = Usuario(usuario='Carol2',email='carolina2@gmail.com',senha='Carol2@senha')
    >> database.session.add(usuario2)

>> database.session.commit()
>> Usuario.query.all()

armazenando a query numa variável é possível consultar seus parâmetros:
    >> usuario_teste = Usuario.query.first()
    >> usuario_teste.email

para fazer uma consulta com base em algum parâmetro:
    >> usuario_teste2 = Usuario.query.filter_by(email='carolina@gmail.com')
    >> usuario_teste2.first()

criando um post:
    >> post1 = Post(titulo='primeiro post',descricao='aqui esta a descricao do post', id_usuario=1)
    >> database.session.add(post1)
    >> database.session.commit()
'''
