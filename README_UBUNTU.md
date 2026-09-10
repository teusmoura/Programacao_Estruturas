# Programação I no Ubuntu

Este guia prepara o ambiente do curso no Ubuntu. Os exemplos usam Python, MySQL e o banco didático `lojas_rede`.

## 1. Instalar os requisitos

Atualize os pacotes e instale Python, criação de ambientes virtuais e o cliente do MySQL:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip mysql-client
```

Você pode usar o MySQL do XAMPP ou um servidor MySQL/MariaDB instalado no Ubuntu.

### Opção A: MySQL do XAMPP para Linux

Depois de instalar o XAMPP, inicie o MySQL:

```bash
sudo /opt/lampp/lampp startmysql
```

O padrão esperado pelo curso é:

- Host: `localhost`
- Porta: `3306`
- Usuário: `root`
- Senha: vazia

### Opção B: MySQL ou MariaDB do Ubuntu

Para MySQL:

```bash
sudo apt install mysql-server
sudo systemctl enable --now mysql
```

Para MariaDB:

```bash
sudo apt install mariadb-server
sudo systemctl enable --now mariadb
```

Confira se o servidor está respondendo na porta esperada:

```bash
sudo ss -ltnp | grep 3306
```

O projeto usa as credenciais definidas pelas variáveis `MYSQL_*`. Em uma instalação local com senha diferente da padrão, configure-as no terminal:

```bash
export MYSQL_USER="root"
export MYSQL_PASSWORD="sua_senha"
export MYSQL_HOST="localhost"
export MYSQL_PORT="3306"
```

Se o usuário `root` do MySQL/MariaDB usar autenticação por socket, crie um usuário para as atividades ou use um usuário que aceite autenticação por senha. Por exemplo, dentro do cliente administrativo do MySQL:

```sql
CREATE USER 'curso'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON lojas_rede.* TO 'curso'@'localhost';
FLUSH PRIVILEGES;
```

Depois use esse usuário:

```bash
export MYSQL_USER="curso"
export MYSQL_PASSWORD="sua_senha"
```

## 2. Entrar na pasta do projeto

```bash
cd ~/caminho/para/Programacao_I
```

Substitua o caminho pelo local onde o projeto foi salvo.

## 3. Criar a venv e instalar as dependências

No Ubuntu, o arquivo `preparar_ambiente.cmd` não é executável. Faça os mesmos passos pelo terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Quando a venv estiver ativa, o prompt normalmente começa com `(.venv)`.

## 4. Criar o banco didático

Com o MySQL/MariaDB em execução e a venv ativa:

```bash
python database/criar_banco.py
```

A mensagem esperada é:

```text
Banco lojas_rede criado e populado com sucesso.
```

Esse comando cria as tabelas e insere os dados iniciais usados nos exemplos e exercícios.

## 5. Usar os exemplos e exercícios

- `exemplos/`: códigos prontos para estudo;
- `exercicios/`: atividades para resolver;
- `database/`: scripts e arquivos SQL do banco.

Execute um exemplo com a venv ativa:

```bash
python exemplos/01_tuplas/06_fetchone_retorna_tupla.py
```

## 6. Reiniciar o banco

Para apagar e recriar o banco no estado inicial do curso:

```bash
python database/reiniciar_banco.py
```

Atenção: esse comando apaga as alterações feitas no banco `lojas_rede`.

## 7. Sair da venv

Quando terminar:

```bash
deactivate
```

Para voltar a trabalhar no projeto, entre na pasta e ative novamente:

```bash
source .venv/bin/activate
```
