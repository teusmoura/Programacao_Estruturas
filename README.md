# Programação — Estruturas de Dados com Python e MySQL

## Comece aqui

O curso usa o padrão XAMPP:

- Host: `localhost`
- Porta: `3306`
- Usuário: `root`
- Senha: vazia

### 1) Preparar o ambiente

No Windows, execute:

```powershell
.\preparar_ambiente.cmd
```

Esse comando cria o ambiente virtual e instala as dependências do projeto.

### 2) Verificar o MySQL

Certifique-se de que o MySQL do XAMPP está rodando.

Se a senha do seu ambiente for diferente da padrão, use:

```powershell
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "sua_senha"
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
```

### 3) Criar o banco didático

Execute:

```powershell
python database\criar_banco.py
```

Isso cria o banco `lojas_rede` com os dados iniciais das atividades.

### 4) Começar a usar

- `exemplos/`: veja exemplos prontos
- `exercicios/`: faça as atividades
- `database/`: scripts de criação e reinício do banco

### 5) Reiniciar o banco quando necessário

```powershell
python database\reiniciar_banco.py
```

Esse comando retorna o banco para o estado inicial do curso.

