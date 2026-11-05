
# Sistema Experto: Rentar o comprar vivienda


# Cada clave H01, H02, etc. identifica un hecho de la tabla del avance 2.
# Diccionario que almacena los hechos identificados
hechos = {
    # H01-H05: Precios de compra o renta recopilados en el avance 1.
    "H01": {
        "descripcion": "El precio promedio de compra de una vivienda en el Centro de Ensenada es de $3,659,500.",
        "dato": 3659500,
        "unidad": "MXN",
        "fuente": "Propiedades.com"
    },
    "H02": {
        "descripcion": "La renta mensual promedio de una casa en Valle Dorado es de $19,675.",
        "dato": 19675,
        "unidad": "MXN/mes",
        "fuente": "Propiedades.com"
    },
    "H03": {
        "descripcion": "El costo de compra en El Sauzal es de $4,918,690, siendo una de las zonas más caras.",
        "dato": 4918690,
        "unidad": "MXN",
        "fuente": "Propiedades.com"
    },
    "H04": {
        "descripcion": "En Las Lomitas el precio de compra es de $1,667,440, más accesible que zonas céntricas.",
        "dato": 1667440,
        "unidad": "MXN",
        "fuente": "Propiedades.com"
    },
    "H05": {
        "descripcion": "En Puerta del Mar la renta mensual aproximada es de $15,700.",
        "dato": 15700,
        "unidad": "MXN/mes",
        "fuente": "Propiedades.com"
    },
    # H06: Conectividad del transporte público.
    "H06": {
        "descripcion": "El transporte público conecta zonas como El Sauzal, Chapultepec y Maneadero con el centro de Ensenada.",
        "dato": "Conexión de El Sauzal, Chapultepec y Maneadero con el Centro",
        "unidad": None,
        "fuente": "Enstop.app/map"
    },
    # H07-H10: Opiniones de usuarios en Reddit, NO hechos comprobados de seguridad.
    "H07": {
        "descripcion": "Usuarios describen el Centro y zona turística como transitadas y relativamente tranquilas para caminar.",
        "dato": "Opiniones de tranquilidad relativa y actividad peatonal",
        "unidad": None,
        "fuente": "Reddit (r/ensenada)"
    },
    "H08": {
        "descripcion": "En Las Lomitas hay opiniones mixtas: algunos la consideran tranquila, otros mencionan riesgo de robos.",
        "dato": "Opiniones mixtas sobre tranquilidad y robos",
        "unidad": None,
        "fuente": "Reddit (r/ensenada)"
    },
    "H09": {
        "descripcion": "Colonias como Popular 89, Indeco y Azteca tienen mala reputación por delincuencia e infraestructura deficiente.",
        "dato": "Comentarios sobre reputación de Popular 89, Indeco y Azteca",
        "unidad": None,
        "fuente": "Reddit (r/ensenada)"
    },
    "H10": {
        "descripcion": "Valle Dorado es considerada tranquila y cercana a escuelas y universidades.",
        "dato": "Opiniones sobre tranquilidad y cercanía a escuelas y universidades",
        "unidad": None,
        "fuente": "Reddit (r/ensenada)"
    }
}


# Mostrar los hechos almacenados
for identificador, informacion in hechos.items():
    print(f"\n{identificador}. {informacion['descripcion']}")
    print(f"    Dato: {informacion['dato']}")
    print(f"    Fuente: {informacion['fuente']}")

# Mostrar la cantidad total
print(f"\nTotal de hechos registrados: {len(hechos)}")

