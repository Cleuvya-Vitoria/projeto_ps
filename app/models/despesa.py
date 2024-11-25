from pydantic import BaseModel
from datetime import datetime

class Despesa(BaseModel):
    id: int
    descricao: str
    valor: float
    status: str  # "pendente", "paga", "parcialmente paga"
    grupo_id: int
    data_criacao: datetime = datetime.now()
