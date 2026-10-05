"""
Utilitários de conversão e parsing para teoria dos conjuntos.
"""
from typing import Any, List, Set, Union
import re


def parse_set_input(raw_input: str) -> List[Any]:
    """
    Converte uma entrada de texto do usuário em uma lista de elementos únicos,
    descartando repetições preservando a essência de um conjunto matemático.
    
    Exemplos suportados:
      - '1, 2, 2, 3, 4' -> [1, 2, 3, 4]
      - '{1, 2, 3}' -> [1, 2, 3]
      - '1 a 10' -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      - 'vazio', '{}', 'Ø', 'O' -> []
      - 'rock, jazz, cinema' -> ['rock', 'jazz', 'cinema']
    """
    text = raw_input.strip()
    
    # Casos de conjunto vazio
    if not text or text in ("{}", "Ø", "vazio", "Vazio", "VAZIO", "None"):
        return []
    
    # Remover chaves externas se presentes
    if text.startswith("{") and text.endswith("}"):
        text = text[1:-1].strip()
    
    # Suporte a intervalos inteiros, ex: '1 a 10' ou '1..10'
    range_match = re.match(r"^(\d+)\s*(?:a|\.\.)\s*(\d+)$", text, re.IGNORECASE)
    if range_match:
        inicio = int(range_match.group(1))
        fim = int(range_match.group(2))
        return list(range(inicio, fim + 1))
    
    # Separar por vírgula, ponto e vírgula ou espaço (se não contiver vírgulas)
    if "," in text:
        tokens = [t.strip() for t in text.split(",")]
    elif ";" in text:
        tokens = [t.strip() for t in text.split(";")]
    else:
        tokens = [t.strip() for t in text.split()]
    
    resultado: List[Any] = []
    
    for token in tokens:
        if not token:
            continue
        
        # Tentar converter para inteiro se for número
        elemento: Any
        try:
            elemento = int(token)
        except ValueError:
            try:
                elemento = float(token)
            except ValueError:
                elemento = token  # Mantém string se for texto
        
        # Eliminação manual de repetições (laço e condicional conforme o espírito da atividade)
        ja_existe = False
        for item in resultado:
            if item == elemento:
                ja_existe = True
                break
        if not ja_existe:
            resultado.append(elemento)
            
    return resultado


def format_set(elements: Union[List[Any], Set[Any]]) -> str:
    """
    Formata uma coleção como representação matemática de conjunto: {1, 2, 3} ou Ø.
    Ordena os elementos quando possível para clareza visual.
    """
    elem_list = list(elements)
    if not elem_list:
        return "Ø"
    
    try:
        sorted_list = sorted(elem_list, key=lambda x: (isinstance(x, str), x))
    except TypeError:
        sorted_list = elem_list
        
    items_str = ", ".join(str(x) for x in sorted_list)
    return "{" + items_str + "}"
