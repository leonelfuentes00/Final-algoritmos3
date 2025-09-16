from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Incidente:
    id: int
    descripcion: str
    tipo: str

@dataclass
class Ticket:
    id: int
    cliente: str       # hardcodeado
    servicio: str      # hardcodeado
    incidente_id: int
    estado: str = "Abierto"
    fecha_creacion: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fecha_cierre: Optional[str] = None
