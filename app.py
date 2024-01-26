from flask import Flask, request, render_template
from flask import jsonify

import itertools

app = Flask(__name__)


# Datos de los resortes proporcionados
resortes = [
    {'tipo': '9X7', 'vueltas': 5.5, 'peso_por_resorte': 24.4},
    {'tipo': '9X7', 'vueltas': 6, 'peso_por_resorte': 25.7},
    {'tipo': '9X7', 'vueltas': 6.5, 'peso_por_resorte': 26.9},
    {'tipo': '9X7', 'vueltas': 7, 'peso_por_resorte': 28.3},
    {'tipo': '9X7', 'vueltas': 7.5, 'peso_por_resorte': 29.7},
    {'tipo': '9X7', 'vueltas': 8, 'peso_por_resorte': 31.2},
    {'tipo': '9X7', 'vueltas': 8.5, 'peso_por_resorte': 32.8},

    {'tipo': '9X8', 'vueltas': 5.5, 'peso_por_resorte': 28.4},
    {'tipo': '9X8', 'vueltas': 6, 'peso_por_resorte': 29.8},
    {'tipo': '9X8', 'vueltas': 6.5, 'peso_por_resorte': 31.3},
    {'tipo': '9X8', 'vueltas': 7, 'peso_por_resorte': 32.9},
    {'tipo': '9X8', 'vueltas': 7.5, 'peso_por_resorte': 34.5},
    {'tipo': '9X8', 'vueltas': 8, 'peso_por_resorte': 36.3},
    {'tipo': '9X8', 'vueltas': 8.5, 'peso_por_resorte': 38.1},
    {'tipo': '9X8', 'vueltas': 9, 'peso_por_resorte': 40},
    {'tipo': '9X8', 'vueltas': 9.5, 'peso_por_resorte': 42},

    {'tipo': '10X7', 'vueltas': 5.5, 'peso_por_resorte': 27.2},
    {'tipo': '10X7', 'vueltas': 6, 'peso_por_resorte': 28.6},
    {'tipo': '10X7', 'vueltas': 6.5, 'peso_por_resorte': 30},
    {'tipo': '10X7', 'vueltas': 7, 'peso_por_resorte': 31.5},
    {'tipo': '10X7', 'vueltas': 7.5, 'peso_por_resorte': 33.1},
    {'tipo': '10X7', 'vueltas': 8, 'peso_por_resorte': 34.7},
    {'tipo': '10X7', 'vueltas': 8.5, 'peso_por_resorte': 36.5},

    {'tipo': '10X8', 'vueltas': 5.5, 'peso_por_resorte': 31.6},
    {'tipo': '10X8', 'vueltas': 6, 'peso_por_resorte': 33.2},
    {'tipo': '10X8', 'vueltas': 6.5, 'peso_por_resorte': 34.9},
    {'tipo': '10X8', 'vueltas': 7, 'peso_por_resorte': 36.6},
    {'tipo': '10X8', 'vueltas': 7.5, 'peso_por_resorte': 38.4},
    {'tipo': '10X8', 'vueltas': 8, 'peso_por_resorte': 40.4},
    {'tipo': '10X8', 'vueltas': 8.5, 'peso_por_resorte': 42.4},
    {'tipo': '10X8', 'vueltas': 9, 'peso_por_resorte': 44.5},
    {'tipo': '10X8', 'vueltas': 9.5, 'peso_por_resorte': 46.7},

    {'tipo': '12X7', 'vueltas': 5.5, 'peso_por_resorte': 32.7},
    {'tipo': '12X7', 'vueltas': 6, 'peso_por_resorte': 34.3},
    {'tipo': '12X7', 'vueltas': 6.5, 'peso_por_resorte': 36},
    {'tipo': '12X7', 'vueltas': 7, 'peso_por_resorte': 37.8},
    {'tipo': '12X7', 'vueltas': 7.5, 'peso_por_resorte': 39.7},
    {'tipo': '12X7', 'vueltas': 8, 'peso_por_resorte': 41.7},
    {'tipo': '12X7', 'vueltas': 8.5, 'peso_por_resorte': 43.8},
 
    {'tipo': '12X8', 'vueltas': 5.5, 'peso_por_resorte': 38},
    {'tipo': '12X8', 'vueltas': 6, 'peso_por_resorte': 39.9},
    {'tipo': '12X8', 'vueltas': 6.5, 'peso_por_resorte': 41.9},
    {'tipo': '12X8', 'vueltas': 7, 'peso_por_resorte': 43.9},
    {'tipo': '12X8', 'vueltas': 7.5, 'peso_por_resorte': 46.1},
    {'tipo': '12X8', 'vueltas': 8, 'peso_por_resorte': 48.4},
    {'tipo': '12X8', 'vueltas': 8.5, 'peso_por_resorte': 50.9},
    {'tipo': '12X8', 'vueltas': 9, 'peso_por_resorte': 53.4},
    {'tipo': '12X8', 'vueltas': 9.5, 'peso_por_resorte': 56.1},

    {'tipo': '14X7', 'vueltas': 5.5, 'peso_por_resorte': 38.1},
    {'tipo': '14X7', 'vueltas': 6, 'peso_por_resorte': 40},
    {'tipo': '14X7', 'vueltas': 6.5, 'peso_por_resorte': 42},
    {'tipo': '14X7', 'vueltas': 7, 'peso_por_resorte': 44.1},
    {'tipo': '14X7', 'vueltas': 7.5, 'peso_por_resorte': 46.3},
    {'tipo': '14X7', 'vueltas': 8, 'peso_por_resorte': 48.6},
    {'tipo': '14X7', 'vueltas': 8.5, 'peso_por_resorte': 51},
   
    {'tipo': '14X8', 'vueltas': 5.5, 'peso_por_resorte': 39.5},
    {'tipo': '14X8', 'vueltas': 6, 'peso_por_resorte': 41.5},
    {'tipo': '14X8', 'vueltas': 6.5, 'peso_por_resorte': 43.6},
    {'tipo': '14X8', 'vueltas': 7, 'peso_por_resorte': 45.8},
    {'tipo': '14X8', 'vueltas': 7.5, 'peso_por_resorte': 48.1},
    {'tipo': '14X8', 'vueltas': 8, 'peso_por_resorte': 50.5},
    {'tipo': '14X8', 'vueltas': 8.5, 'peso_por_resorte': 53},
    {'tipo': '14X8', 'vueltas': 9, 'peso_por_resorte': 55.7},
    {'tipo': '14X8', 'vueltas': 9.5, 'peso_por_resorte': 58.4},
   
    {'tipo': '16X7', 'vueltas': 5.5, 'peso_por_resorte': 43.5},
    {'tipo': '16X7', 'vueltas': 6, 'peso_por_resorte': 45.7},
    {'tipo': '16X7', 'vueltas': 6.5, 'peso_por_resorte': 48},
    {'tipo': '16X7', 'vueltas': 7, 'peso_por_resorte': 50.4},
    {'tipo': '16X7', 'vueltas': 7.5, 'peso_por_resorte': 52.9},
    {'tipo': '16X7', 'vueltas': 8, 'peso_por_resorte': 55.6},
    {'tipo': '16X7', 'vueltas': 8.5, 'peso_por_resorte': 58.3},
   
    {'tipo': '16X8', 'vueltas': 5.5, 'peso_por_resorte': 50.6},
    {'tipo': '16X8', 'vueltas': 6, 'peso_por_resorte': 53.1},
    {'tipo': '16X8', 'vueltas': 6.5, 'peso_por_resorte': 55.8},
    {'tipo': '16X8', 'vueltas': 7, 'peso_por_resorte': 58.6},
    {'tipo': '16X8', 'vueltas': 7.5, 'peso_por_resorte': 61.5},
    {'tipo': '16X8', 'vueltas': 8, 'peso_por_resorte': 64.6},
    {'tipo': '16X8', 'vueltas': 8.5, 'peso_por_resorte': 67.8},
    {'tipo': '16X8', 'vueltas': 9, 'peso_por_resorte': 71.2},
    {'tipo': '16X8', 'vueltas': 9.5, 'peso_por_resorte': 74.8},
 
    {'tipo': '18X7', 'vueltas': 5.5, 'peso_por_resorte': 48.9},
    {'tipo': '18X7', 'vueltas': 6, 'peso_por_resorte': 51.3},
    {'tipo': '18X7', 'vueltas': 6.5, 'peso_por_resorte': 53.9},
    {'tipo': '18X7', 'vueltas': 7, 'peso_por_resorte': 56.6},
    {'tipo': '18X7', 'vueltas': 7.5, 'peso_por_resorte': 59.4},
    {'tipo': '18X7', 'vueltas': 8, 'peso_por_resorte': 62.4},
    {'tipo': '18X7', 'vueltas': 8.5, 'peso_por_resorte': 65.5},

    {'tipo': '18X8', 'vueltas': 5.5, 'peso_por_resorte': 56.8},
    {'tipo': '18X8', 'vueltas': 6, 'peso_por_resorte': 59.7},
    {'tipo': '18X8', 'vueltas': 6.5, 'peso_por_resorte': 62.7},
    {'tipo': '18X8', 'vueltas': 7, 'peso_por_resorte': 65.8},
    {'tipo': '18X8', 'vueltas': 7.5, 'peso_por_resorte': 69.1},
    {'tipo': '18X8', 'vueltas': 8, 'peso_por_resorte': 72.5},
    {'tipo': '18X8', 'vueltas': 8.5, 'peso_por_resorte': 76.2},
    {'tipo': '18X8', 'vueltas': 9, 'peso_por_resorte': 80},
    {'tipo': '18X8', 'vueltas': 9.5, 'peso_por_resorte': 84},
   
    {'tipo': '20X7', 'vueltas': 5.5, 'peso_por_resorte': 53.6},
    {'tipo': '20X7', 'vueltas': 6, 'peso_por_resorte': 56.3},
    {'tipo': '20X7', 'vueltas': 6.5, 'peso_por_resorte': 59.1},
    {'tipo': '20X7', 'vueltas': 7, 'peso_por_resorte': 62.1},
    {'tipo': '20X7', 'vueltas': 7.5, 'peso_por_resorte': 65.2},
    {'tipo': '20X7', 'vueltas': 8, 'peso_por_resorte': 68.4},
    {'tipo': '20X7', 'vueltas': 8.5, 'peso_por_resorte': 71.8},
   
    {'tipo': '20X8', 'vueltas': 5.5, 'peso_por_resorte': 62.3},
    {'tipo': '20X8', 'vueltas': 6, 'peso_por_resorte': 65.4},
    {'tipo': '20X8', 'vueltas': 6.5, 'peso_por_resorte': 68.7},
    {'tipo': '20X8', 'vueltas': 7, 'peso_por_resorte': 72.2},
    {'tipo': '20X8', 'vueltas': 7.5, 'peso_por_resorte': 75.8},
    {'tipo': '20X8', 'vueltas': 8, 'peso_por_resorte': 79.6},
    {'tipo': '20X8', 'vueltas': 8.5, 'peso_por_resorte': 83.5},
    {'tipo': '20X8', 'vueltas': 9, 'peso_por_resorte': 87.7},
    {'tipo': '20X8', 'vueltas': 9.5, 'peso_por_resorte': 92.1},

    {'tipo': '24X7', 'vueltas': 5.5, 'peso_por_resorte': 65.3},
    {'tipo': '24X7', 'vueltas': 6, 'peso_por_resorte': 68.6},
    {'tipo': '24X7', 'vueltas': 6.5, 'peso_por_resorte': 72},
    {'tipo': '24X7', 'vueltas': 7, 'peso_por_resorte': 75.6},
    {'tipo': '24X7', 'vueltas': 7.5, 'peso_por_resorte': 79.4},
    {'tipo': '24X7', 'vueltas': 8, 'peso_por_resorte': 83.3},
    {'tipo': '24X7', 'vueltas': 8.5, 'peso_por_resorte': 87.5},
   
    {'tipo': '24X8', 'vueltas': 5.5, 'peso_por_resorte': 75.9},
    {'tipo': '24X8', 'vueltas': 6, 'peso_por_resorte': 79.7},
    {'tipo': '24X8', 'vueltas': 6.5, 'peso_por_resorte': 83.7},
    {'tipo': '24X8', 'vueltas': 7, 'peso_por_resorte': 87.9},
    {'tipo': '24X8', 'vueltas': 7.5, 'peso_por_resorte': 92.3},
    {'tipo': '24X8', 'vueltas': 8, 'peso_por_resorte': 96.9},
    {'tipo': '24X8', 'vueltas': 8.5, 'peso_por_resorte': 101.7},
    {'tipo': '24X8', 'vueltas': 9, 'peso_por_resorte': 106.8},
    {'tipo': '24X8', 'vueltas': 9.5, 'peso_por_resorte': 112.2},
   
]

def calcular_vueltas(altura):
    PIE = 30.5  # cm
    return altura / PIE

def encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes):
    combinaciones_validas = []
    
    # Filtrar los resortes que tienen un número de vueltas cercano al calculado
    resortes_cercanos = [resorte for resorte in resortes if abs(resorte['vueltas'] - vueltas) <= 0.5]
    
    # Generar todas las combinaciones posibles de num_resortes
    for combo in itertools.combinations(resortes_cercanos, num_resortes):
        peso_combinado = sum(resorte['peso_por_resorte'] for resorte in combo)
        if abs(peso_combinado - peso_objetivo) <= 4:  # Ajustar el margen de error a ±4 kg
            combinaciones_validas.append(combo)
    
    # Ordenar las combinaciones válidas según su cercanía al peso objetivo
    combinaciones_validas.sort(key=lambda combo: abs(sum(resorte['peso_por_resorte'] for resorte in combo) - peso_objetivo))
    
    return combinaciones_validas




def main():
    # Solicitar datos al usuario
    peso_objetivo = float(input("Introduce el peso (kg): "))
    ancho = float(input("Introduce el ancho (m): "))
    altura = float(input("Introduce el alto (m): ")) * 100  # Convertir a cm

    vueltas = calcular_vueltas(altura)
    print(f'El número de vueltas calculado para el resorte es: {int(vueltas) if vueltas.is_integer() else str(int(vueltas)) + " 1/2"}')

    opciones = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5
    }

    # Mostrar las 6 combinaciones más cercanas de 1 y 2 resortes
    combinaciones_cercanas = []
    for num_resortes in [1, 2]:
        combinaciones_cercanas.extend(encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes))
    
    combinaciones_cercanas.sort(key=lambda combo: abs(sum(resorte['peso_por_resorte'] for resorte in combo) - peso_objetivo))
    for combo in combinaciones_cercanas[:6]:
        tipos = [f"{resorte['tipo']} ({resorte['vueltas']} vueltas)" for resorte in combo]
        print(", ".join(tipos))
    print()

    # Mostrar opciones adicionales
    print("Ver más combinaciones de resortes recomendadas:")
    for letra, num_resortes in opciones.items():
        combinaciones = encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes)
        if combinaciones:
            print(f"{letra}: Con {num_resortes} resorte(s): {len(combinaciones)} Combinaciones encontradas.")
    
    # Seleccionar una opción y mostrar combinaciones correspondientes
    opcion_seleccionada = input("Selecciona una opción (A, B, C, D, E): ").upper()
    if opcion_seleccionada in opciones:
        num_resortes = opciones[opcion_seleccionada]
        combinaciones = encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes)
        for combo in combinaciones:
            tipos = [f"{resorte['tipo']} ({resorte['vueltas']} vueltas)" for resorte in combo]
            print(", ".join(tipos))



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los valores del formulario
        peso_objetivo = float(request.form['peso'])
        altura = float(request.form['altura']) * 100  # Convertir a cm

        vueltas = calcular_vueltas(altura)
        # Calculamos inicialmente para 1 y 2 resortes
        combinaciones_iniciales = []
        for num_resortes in [1, 2]:
            combinaciones_iniciales.extend(encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes))

        # Limitar las combinaciones iniciales si lo deseas
        combinaciones_iniciales = combinaciones_iniciales[:6]

        # Calcular opciones adicionales
        opciones_adicionales = {
            num_resortes: {
                'cantidad': len(encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes)),
                'texto_boton': f"Ver resultados para {num_resortes} resortes"
            } for num_resortes in range(1, 6)
        }
        return render_template('resultados.html', 
                               combinaciones=combinaciones_iniciales, 
                               opciones=opciones_adicionales)
    return render_template('index.html')













# IMPRIMIR MAS

@app.route('/get_combinaciones', methods=['POST'])
def get_combinaciones():
    num_resortes = int(request.form['num_resortes'])
    peso_objetivo = float(request.form['peso'])
    altura = float(request.form['altura']) * 100
    vueltas = calcular_vueltas(altura)

    combinaciones = encontrar_combinaciones(peso_objetivo, vueltas, resortes, num_resortes)
    combinaciones_formato = [", ".join(f"{resorte['tipo']} ({resorte['vueltas']} vueltas)" for resorte in combo) for combo in combinaciones]

    return jsonify(combinaciones_formato)





@app.route('/filtrar_resultados', methods=['POST'])
def filtrar_resultados():
    # Obtener los valores del formulario
    peso_objetivo = float(request.form['peso'])
    altura = float(request.form['altura']) * 100  # Convertir a cm
    vueltas = calcular_vueltas(altura)

    # Obtener tipos de resortes seleccionados
    tipos_seleccionados = request.form.getlist('resortes_disponibles')
    
    # Filtrar los resortes basándose en los tipos seleccionados
    resortes_filtrados = [resorte for resorte in resortes if resorte['tipo'] in tipos_seleccionados]

    # Calcular combinaciones con los resortes filtrados
    combinaciones_filtradas = []
    for num_resortes in [1, 2]:
        combinaciones_filtradas.extend(encontrar_combinaciones(peso_objetivo, vueltas, resortes_filtrados, num_resortes))

    # Calcular opciones adicionales
    opciones_adicionales = {
        num_resortes: {
            'cantidad': len(encontrar_combinaciones(peso_objetivo, vueltas, resortes_filtrados, num_resortes)),
            'texto_boton': f"Ver resultados para {num_resortes} resortes"
        } for num_resortes in range(1, 6)
    }

    # Crear un conjunto de tipos únicos de resortes
    tipos_unicos = {resorte['tipo'] for resorte in resortes}

    # Renderizar la plantilla con los resultados filtrados y los tipos únicos
    return render_template('resultados.html', 
                           combinaciones=combinaciones_filtradas, 
                           opciones=opciones_adicionales,
                           tipos_unicos=tipos_unicos)






if __name__ == '__main__':
    app.run(debug=True)




