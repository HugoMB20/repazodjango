from django.shortcuts import render

# Vista de inicio con la lista de géneros (usará componentes de Bootstrap en la plantilla)
def inicio(request):
    generos = [
        {
            'id': 'accion',
            'nombre': 'Acción',
            'descripcion': 'Películas llenas de adrenalina, persecuciones y combates espectaculares.',
            'imagen': 'accion.jpg'
        },
        {
            'id': 'ciencia_ficcion',
            'nombre': 'Ciencia Ficción',
            'descripcion': 'Explora futuros distópicos, viajes en el espacio y tecnología avanzada.',
            'imagen': 'scifi.jpg'
        }
    ]
    return render(request, 'home_isaac/inicio.html', {'generos': generos})

# Vista para el género Acción
def genero_accion(request):
    peliculas = [
        {
            'nombre': 'Mad Max: Fury Road',
            'edad': '+16',
            'imagen': 'madmax.jpg',
            'descripcion': 'En un desierto posapocalíptico, Max se une a Furiosa para escapar de un tirano.'
        },
        {
            'nombre': 'John Wick 4',
            'edad': '+18',
            'imagen': 'johnwick.jpg',
            'descripcion': 'John Wick descubre un camino para derrotar a la Alta Mesa.'
        }
    ]
    return render(request, 'home_isaac/pelicula_list.html', {
        'titulo_genero': 'Películas de Acción',
        'peliculas': peliculas
    })

# Vista para el género Ciencia Ficción
def genero_scifi(request):
    peliculas = [
        {
            'nombre': 'Interstellar',
            'edad': '+13',
            'imagen': 'interstellar.jpg',
            'descripcion': 'Un grupo de exploradores viaja a través de un agujero de gusano para salvar la humanidad.'
        },
        {
            'nombre': 'Blade Runner 2049',
            'edad': '+16',
            'imagen': 'bladerunner.jpg',
            'descripcion': 'Un nuevo blade runner descubre un secreto guardado durante mucho tiempo.'
        }
    ]
    return render(request, 'home_isaac/pelicula_list.html', {
        'titulo_genero': 'Películas de Ciencia Ficción',
        'peliculas': peliculas
    })