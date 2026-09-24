def validar_titulo(title: str) -> bool:
    if not title:
        return False
    return len(title.strip()) >= 2


def validar_descricao(description: str) -> bool:
    if not description:
        return False
    return len(description.strip()) >= 3


def normalizar_prioridade(value) -> int:
    try:
        v = int(value)
        if v < 1:
            return 1
        if v > 5:
            return 5
        return v
    except (TypeError, ValueError):
        return 3


def normalizar_status(value) -> str:
    status = (value or 'pendente').strip().lower()
    return status if status in {'pendente', 'concluida'} else 'pendente'
