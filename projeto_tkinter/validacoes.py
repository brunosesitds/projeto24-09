def validar_titulo(title: str) -> bool:
    if not title:
        return False
    return len(title.strip()) >= 2


def normalizar_prioridade(value) -> int:
    try:
        v = int(value)
        if v < 1:
            return 1
        if v > 5:
            return 5
        return v
    except Exception:
        return 3
