import sqlite3
from typing import List, Dict, Any
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "helpdesk.db"


def _connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = _connect()
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            chamado INTEGER PRIMARY KEY,
            nome TEXT,
            problema TEXT,
            cpf TEXT,
            contato TEXT,
            tecnico TEXT,
            status TEXT,
            tipo_problema TEXT,
            prazo_resolucao TEXT,
            valor_manutencao REAL,
            peca TEXT,
            quantidade_peca INTEGER,
            valor_peca REAL,
            forma_pagamento TEXT,
            status_pagamento TEXT,
            observacao_financeira TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def insert_cliente(cliente) -> None:
    try:
        conn = _connect()
        c = conn.cursor()
        c.execute(
            """
            INSERT OR REPLACE INTO clientes (
                chamado, nome, problema, cpf, contato, tecnico, status,
                tipo_problema, prazo_resolucao, valor_manutencao, peca,
                quantidade_peca, valor_peca, forma_pagamento, status_pagamento,
                observacao_financeira
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                cliente.chamado,
                cliente.nome,
                cliente.problema,
                str(cliente.cpf),
                str(cliente.contato),
                getattr(cliente, "tecnico", None),
                getattr(cliente, "status", None),
                cliente.tipo_problema,
                cliente.prazo_resolucao,
                cliente.valor_manutencao,
                cliente.peca,
                cliente.quantidade_peca,
                cliente.valor_peca,
                cliente.forma_pagamento,
                cliente.status_pagamento,
                cliente.observacao_financeira,
            ),
        )
        conn.commit()
    finally:
        conn.close()


def update_cliente(chamado: int, **fields) -> None:
    if not fields:
        return
    keys = []
    values = []
    for k, v in fields.items():
        keys.append(f"{k} = ?")
        values.append(v)
    values.append(chamado)

    conn = _connect()
    try:
        c = conn.cursor()
        c.execute(f"UPDATE clientes SET {', '.join(keys)} WHERE chamado = ?", tuple(values))
        conn.commit()
    finally:
        conn.close()


def delete_cliente(chamado: int) -> None:
    conn = _connect()
    try:
        c = conn.cursor()
        c.execute("DELETE FROM clientes WHERE chamado = ?", (chamado,))
        conn.commit()
    finally:
        conn.close()


def load_all_clients() -> List[Dict[str, Any]]:
    conn = _connect()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM clientes ORDER BY chamado")
        rows = c.fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()
