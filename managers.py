import sqlite3
from models import Incidente, Ticket
from database import DB_NAME
from datetime import datetime

class IncidenteManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def listar(self):
        rows = self.conn.execute("SELECT * FROM incidentes").fetchall()
        return [Incidente(**dict(r)) for r in rows]

    def crear(self, descripcion, tipo):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO incidentes (descripcion, tipo) VALUES (?, ?)", (descripcion, tipo))
        self.conn.commit()
        return Incidente(cur.lastrowid, descripcion, tipo)

    def obtener(self, incidente_id):
        row = self.conn.execute("SELECT * FROM incidentes WHERE id=?", (incidente_id,)).fetchone()
        return Incidente(**dict(row)) if row else None


class TicketManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def listar(self):
        rows = self.conn.execute("SELECT * FROM tickets").fetchall()
        return [Ticket(**dict(r)) for r in rows]

    def crear(self, cliente, servicio, incidente_id):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO tickets (cliente, servicio, incidente_id, estado, fecha_creacion)
            VALUES (?, ?, ?, ?, ?)
        """, (cliente, servicio, incidente_id, "Abierto", fecha))
        self.conn.commit()
        return Ticket(cur.lastrowid, cliente, servicio, incidente_id, "Abierto", fecha)

    def obtener(self, ticket_id):
        row = self.conn.execute("SELECT * FROM tickets WHERE id=?", (ticket_id,)).fetchone()
        return Ticket(**dict(row)) if row else None

    def cerrar(self, ticket_id):
        fecha_cierre = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conn.execute("UPDATE tickets SET estado=?, fecha_cierre=? WHERE id=?",
                          ("Cerrado", fecha_cierre, ticket_id))
        self.conn.commit()
        return self.obtener(ticket_id)
