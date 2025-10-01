from django.shortcuts import render, redirect
from .models import Receta, EventosCulinarios
from .formularios import FormularioDeEvento

# Create your views here.

# Vistas y variables pertenecientes al sitio de recetas
RECETAS = [
        Receta(
            imagen="https://i.postimg.cc/8PxcXTQn/Completo-italiano.jpg",
            nombre="Completo Italiano",
            descripcion="El completo es un bocadillo tradicional de Chile que consiste en un pan de hot dog, «pan de completo» o «pan copihue» abierto a lo largo, con una vienesa en el medio sobre la cual se colocan diversos ingredientes.\nEs una de las especialidades de comida rápida más comunes y conocidas en Chile. Se diferencia del tradicional hot dog estadounidense por llevar una mayor cantidad de ingredientes y aderezos y, además, por tener un mayor tamaño.",
            ingredientes=["Vienesa", "Tomate", "Palta", "Mayonesa casera"],
            optativos=["Cebolla", "Ketchup", "Mostaza", "Chucrut", "Americana"],
            instrucciones=["Cocer las vienesas en agua hirviendo por 5 minutos.", "Lavar y picar el tomate en cuadritos pequeños y moler la palta (o aguacate) con un poquito de sal. Aliñar el tomate con unas gotitas de aceite y sal.", "Cuando las salchichas estén listas, ponerlas en el pan y hornear por 3 minutos en el horno a temperatura máxima", "Agregar la palta, luego el tomate y por último la mayonesa. Y ¡A disfrutar!"]
        ),
        Receta(
            imagen="https://i.postimg.cc/TYKhcpSD/Cazuela-de-pollo.jpg",
            nombre="Cazuela de Ave",
            descripcion="La historia de la cazuela de ave chilena es una mezcla de tradiciones indígenas y españolas, originada en la época colonial. Los españoles trajeron el concepto de la 'cazuela' desde España, inspirado en platos como el 'cocido' o 'puchero', pero adaptaron y fusionaron esta preparación con los ingredientes locales que ya consumían los mapuches en el territorio chileno, como la papa, el zapallo, el choclo y la quinoa. La receta evolucionó con el tiempo, dando lugar a diversas variantes regionales y convirtiéndose en un símbolo de la cocina casera y el mestizaje cultural en Chile.",
            ingredientes=["Pollo", "Zapallo", "Papa", "Cebolla", "Ajo"],
            optativos=["Arroz", "Chuchoca", "Cilantro", "Fideos (Cabellos de ángel)"],
            instrucciones=["En una olla grande, poner a hervir el pollo con agua suficiente para cubrirlo. Agregar sal, cebolla y ajo.", "Cuando el pollo esté cocido, sacarlo de la olla y reservar. Colar el caldo para eliminar impurezas.", "Agregar al caldo las verduras picadas (zapallo, papa, choclo, porotos verdes) y cocinar hasta que estén tiernas.", "Si se desea, agregar arroz, chuchoca o fideos para hacer la cazuela más sustanciosa.", "Agregar el pollo desmenuzado nuevamente a la olla y cocinar por unos minutos más. Servir caliente y disfrutar."]
        ),
        Receta(
            imagen="https://i.postimg.cc/JnT4NL5x/images.jpg",
            nombre="Arepas",
            ingredientes=["Harina de maíz", "Agua", "Sal"],
            descripcion="La arepa es una preparación culinaria de origen amerindio hecha a base de masa de maíz cocido. Tiene forma circular y aplanada, y se cocina mediante métodos diversos como el asado, horneado o la fritura. La masa puede incluir variaciones contemporáneas que incorporan otros ingredientes como queso, huevos o vegetales. Al igual que en otros países en los que un alimento aplanado de maíz en forma de disco es parte de la base alimenticia, la denominada 'arepa' es un componente fundamental en las gastronomías de Colombia y Venezuela, países donde su consumo es cotidiano y está arraigado en la cultura alimenticia, así como en algunas regiones del oriente de Bolivia, en donde también se le conoce por ese nombre.",
            instrucciones=["Mezclar la harina de maíz con agua y sal hasta formar una masa suave.", "Dividir la masa en porciones y formar bolas, luego aplanarlas para darles forma de disco.", "Cocinar las arepas en una sartén caliente o en una parrilla hasta que estén doradas por ambos lados.", "Abrir las arepas por la mitad y rellenarlas con los ingredientes de tu preferencia, como queso, carne, pollo, palta (o aguacate), etc."],
        ),
        Receta(
            imagen="https://www.gourmet.cl/wp-content/uploads/2016/12/Carbonara-editada.jpg",
            nombre="Spaghetti Carbonara",
            descripcion="Spagetti típico italiano",
            ingredientes=["Spaghetti", "huevos", "panceta", "queso parmesano", "pimienta"],
            instrucciones=["Cocinar la pasta.", "Mezclar con huevos y queso.", "Añadir panceta frita."]
        ),
        Receta(
            imagen="https://partaste.com/worldrecipes/wp-content/uploads/sites/2/2015/06/tacos_de_pollo.jpg",
            nombre="Tacos de Pollo",
            descripcion="Deliciosos taquitos de pollo",
            ingredientes=["Tortillas", "pollo", "lechuga", "tomate", "salsa"],
            instrucciones=["Cocinar pollo.", "Armar tacos con ingredientes."]
        ),
    ]

def home(request):
    return render(request, 'home.html')

def recetas(request):
    return render(request, 'recetas.html', {'recetas': RECETAS})

def contacto(request):
    return render(request, 'contacto.html')

def detalle_receta(request, receta_index):
    if 0 <= receta_index < len(RECETAS):
        receta = RECETAS[receta_index]
        return render(request, 'detalle_receta.html', {'receta': receta})
    return render(request, 'detalle_receta.html', {'receta': None})

# Vistas y variables pertenecientes al sitio de eventos
EVENTOS = []

def eventos(request):
    if request.method == 'POST':
        formulario = FormularioDeEvento(request.POST)
        if formulario.is_valid():
            evento = formulario.cleaned_data['evento']
            fecha = formulario.cleaned_data['fecha']
            ubicacion = formulario.cleaned_data['ubicacion']
            print("Informacion del formulario")
            print(evento, fecha, ubicacion)
            return redirect('evento_exito')
        else:
            return render(request, 'eventos.html', {'eventos': EVENTOS})
    else:
        formulario = FormularioDeEvento()    
        return render(request, 'eventos.html', {'eventos': EVENTOS})

def nuevo_evento(request):
    return render (request, 'evento_exito.html' )