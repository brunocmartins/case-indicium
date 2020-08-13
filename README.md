# Case Indicium Tech

Resolução da primeira etapa do processo seletivo da Indicium Tech. 

## Objetivo

Aplicação de ETL em inputs relacionados às negociações, setores, contatos e empresas para obter insumos para a preparação de dados referentes à negociação por setor, por mês e por contato.

## TODOs

- Avaliar se tem algum problema de encoding (evidenciar quantidade)

## Configuração de Ambiente

Será necessário ter instalado [Python 3](https://www.python.org/downloads/) e [pip](https://pip.pypa.io/en/stable/installing/). É indicada a utilização de um ambiente virtual, assim como a instalação dos arquivos presentes em `requirements.txt`.

Linux e MacOS
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 case.py
```

Windows
```
$ pip3 install virtualenv
$ virtualenv ..\venv
$ ..\venv\Scripts\activate
$ pip install -r requirements.txt
$ python3 case.py
```

Quando finalizado, basta desativar o ambiente virtual com:
```
$ deactivate
```

## Observações

- Existem diferentes IDs de empresas que possuem o mesmo nome, mas setores diferentes. As linhas foram mantidas pelos diferentes IDs serem referenciados em outros arquivos.
- Existem diferentes IDs de contato que possuem todas as mesmas informações, com exceção das colunas employersId e contactsResponsible. As duplicatas foram removidas e essas duplicatas não referenciavam nenhum outro arquivo fornecido, totalizando 8 linhas removidas.