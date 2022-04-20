#o init é o arquivo de inicialização, caso precisasse de outro bastava escrever: from siteprojeto.nomedoarquivo
 
from siteprojeto import app

if __name__ == '__zmain__':
    app.run(debug=True)
