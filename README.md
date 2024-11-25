# API de Compartilhamento de Despesas

API REST desenvolvida em Python com FastAPI para gerenciar despesas de grupos.

## Funcionalidades

1. **Adicionar Despesa**: Cadastro de despesas com salvamento em CSV.
2. **Listar Despesas**: Consulta de todas as despesas registradas.
3. **Atualizar Despesa**: Edição de despesas específicas.
4. **Remover Despesa**: Exclusão de despesas por ID.
5. **Contar Despesas**: Retorna o número total de despesas no CSV.
6. **Compactar Arquivo**: Gera um arquivo ZIP a partir do CSV.
7. **Hash SHA256**: Retorna o hash do CSV para validação.

## Como Rodar
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
