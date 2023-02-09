from django import template

register = template.Library()

@register.filter(nome='plural_comentarios')
def plural_comentario(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)
    
        if num_comentarios == 1:
            return f'{num_comentarios} comentario'
        elif num_comentarios == 0 :
            return f'sem comentario '
        else:
            return f'{num_comentarios} comentarios'
    except:
        return f'{num_comentarios} comentarios'