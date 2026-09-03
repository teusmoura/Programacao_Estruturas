-- ============================================================
-- BANCO DIDÁTICO: lojas_rede
-- Estruturas de Dados com Python + MySQL
--
-- Cenário: rede varejista fictícia com lojas principalmente em
-- Minas Gerais, algumas unidades fora do estado, centros de
-- distribuição, canais de venda e uma malha logística simplificada.
-- O banco existe para sustentar os exemplos e atividades da disciplina;
-- não pretende reproduzir um ERP real.
-- ============================================================

CREATE DATABASE IF NOT EXISTS lojas_rede
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE lojas_rede;

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(18) NOT NULL UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(80),
    uf CHAR(2),
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fornecedores (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(18) NOT NULL UNIQUE,
    cidade VARCHAR(80),
    uf CHAR(2),
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

-- Autorrelacionamento para recursividade e árvores.
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_categoria_pai INT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_categoria_pai FOREIGN KEY (id_categoria_pai)
        REFERENCES categorias(id_categoria) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(30) NOT NULL UNIQUE,
    nome VARCHAR(120) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    id_fornecedor INT,
    id_categoria INT,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT fk_produto_fornecedor FOREIGN KEY (id_fornecedor)
        REFERENCES fornecedores(id_fornecedor),
    CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
);

-- Uma única entidade representa LOJAs e CDs.
CREATE TABLE IF NOT EXISTS unidades (
    id_unidade INT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    tipo ENUM('LOJA','CD') NOT NULL,
    cidade VARCHAR(80) NOT NULL,
    uf CHAR(2) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

-- Estoque existe por unidade; não há um estoque global duplicado em produtos.
CREATE TABLE IF NOT EXISTS estoques (
    id_unidade INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    estoque_minimo INT NOT NULL DEFAULT 0,
    PRIMARY KEY (id_unidade, id_produto),
    CONSTRAINT fk_estoque_unidade FOREIGN KEY (id_unidade)
        REFERENCES unidades(id_unidade),
    CONSTRAINT fk_estoque_produto FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);

CREATE TABLE IF NOT EXISTS canais_venda (
    id_canal INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_unidade INT NOT NULL,
    id_canal INT NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) NOT NULL DEFAULT 'PENDENTE',
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),
    CONSTRAINT fk_pedido_unidade FOREIGN KEY (id_unidade)
        REFERENCES unidades(id_unidade),
    CONSTRAINT fk_pedido_canal FOREIGN KEY (id_canal)
        REFERENCES canais_venda(id_canal)
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_item_pedido FOREIGN KEY (id_pedido)
        REFERENCES pedidos(id_pedido) ON DELETE CASCADE,
    CONSTRAINT fk_item_produto FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);

-- Fonte natural para pilhas/histórico.
CREATE TABLE IF NOT EXISTS historico_status_pedido (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    status VARCHAR(30) NOT NULL,
    observacao VARCHAR(255),
    data_evento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_historico_pedido FOREIGN KEY (id_pedido)
        REFERENCES pedidos(id_pedido) ON DELETE CASCADE
);

-- A mesma tabela sustenta FIFO (data_solicitacao) e heap (prioridade/prazo).
-- prioridade: 1 = mais urgente; 5 = menos urgente.
CREATE TABLE IF NOT EXISTS solicitacoes_reposicao (
    id_solicitacao INT AUTO_INCREMENT PRIMARY KEY,
    id_unidade INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade_solicitada INT NOT NULL,
    prioridade INT NOT NULL DEFAULT 3,
    status VARCHAR(30) NOT NULL DEFAULT 'PENDENTE',
    data_solicitacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    prazo DATETIME NULL,
    CONSTRAINT fk_reposicao_unidade FOREIGN KEY (id_unidade)
        REFERENCES unidades(id_unidade),
    CONSTRAINT fk_reposicao_produto FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);

-- Encadeamento explícito para a unidade de lista encadeada.
CREATE TABLE IF NOT EXISTS etapas_reposicao (
    id_etapa INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_proxima_etapa INT NULL,
    CONSTRAINT fk_etapa_proxima FOREIGN KEY (id_proxima_etapa)
        REFERENCES etapas_reposicao(id_etapa) ON DELETE SET NULL
);

-- Arestas do grafo logístico. Origem/destino podem ser loja ou CD.
CREATE TABLE IF NOT EXISTS rotas (
    id_rota INT AUTO_INCREMENT PRIMARY KEY,
    id_origem INT NOT NULL,
    id_destino INT NOT NULL,
    distancia_km DECIMAL(8,2) NOT NULL,
    tempo_estimado_min INT NOT NULL,
    ativa BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE KEY uq_rota (id_origem, id_destino),
    CONSTRAINT fk_rota_origem FOREIGN KEY (id_origem)
        REFERENCES unidades(id_unidade),
    CONSTRAINT fk_rota_destino FOREIGN KEY (id_destino)
        REFERENCES unidades(id_unidade)
);
