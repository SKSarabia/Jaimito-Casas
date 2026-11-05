# Ontología del dominio: Asesoría para decidir entre rentar o comprar vivienda

**Proyecto:** Sistema Experto de Asesoría para la Renta o Compra de Vivienda en Ensenada, Baja California  
**Materia:** Programación Lógica

## Diagrama de clases y relaciones (Mermaid)

```mermaid
flowchart TD

    subgraph CLASES["CLASES Y CONCEPTOS"]
        Usuario["Usuario"]
        SF["SituacionFinanciera"]
        NH["NecesidadHabitacional"]
        Vivienda["Vivienda"]
        Casa["Casa"]
        Departamento["Departamento"]
        Zona["Zona"]
        Precio["PrecioReferencia"]
        Servicio["ServicioZona"]
        Riesgo["RiesgoTerritorial"]
        Opinion["OpinionComunitaria"]
        Fuente["Fuente"]
        Evaluacion["Evaluacion"]
        Recomendacion["Recomendacion"]
    end

    subgraph INSTANCIAS["INSTANCIAS DE ZONA"]
        Centro["Centro de Ensenada"]
        Valle["Valle Dorado"]
        Sauzal["El Sauzal"]
        Lomitas["Las Lomitas"]
        Puerta["Puerta del Mar"]
    end

    subgraph PROPIEDADES["PROPIEDADES Y ATRIBUTOS"]
        AFin["ingresos, gastos, deudas, ahorros"]
        ANec["permanencia, movilidad, preferencias"]
        AViv["tipo, precio de compra, renta"]
        APrecio["monto, operacion, fecha"]
        AZona["nombre, municipio"]
        ARegistro["tipo, fecha, estado o contenido"]
        ARec["tipo, justificacion, advertencias"]
    end

    Casa -.->|es una| Vivienda
    Departamento -.->|es una| Vivienda

    Usuario -->|tiene| SF
    Usuario -->|expresa| NH
    Usuario -->|solicita| Evaluacion

    Evaluacion -->|analiza| Vivienda
    Evaluacion -->|considera| Zona
    Evaluacion -->|genera| Recomendacion

    Vivienda -->|se ubica en| Zona

    Zona -->|registra precios| Precio
    Zona -->|documenta servicios| Servicio
    Zona -->|documenta riesgos| Riesgo
    Zona -->|recibe opiniones| Opinion

    Precio -->|procede de| Fuente
    Servicio -->|procede de| Fuente
    Riesgo -->|procede de| Fuente
    Opinion -->|procede de| Fuente

    Centro -.->|instancia de| Zona
    Valle -.->|instancia de| Zona
    Sauzal -.->|instancia de| Zona
    Lomitas -.->|instancia de| Zona
    Puerta -.->|instancia de| Zona

    SF -.->|tiene atributos| AFin
    NH -.->|tiene atributos| ANec
    Vivienda -.->|tiene atributos| AViv
    Precio -.->|tiene atributos| APrecio
    Zona -.->|tiene atributos| AZona

    Servicio -.->|tiene atributos| ARegistro
    Riesgo -.->|tiene atributos| ARegistro
    Opinion -.->|tiene atributos| ARegistro

    Recomendacion -.->|tiene atributos| ARec

    classDef concepto fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef instancia fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef propiedad fill:#fef3c7,stroke:#d97706,color:#78350f

    class Usuario,SF,NH,Vivienda,Casa,Departamento,Zona,Precio,Servicio,Riesgo,Opinion,Fuente,Evaluacion,Recomendacion concepto
    class Centro,Valle,Sauzal,Lomitas,Puerta instancia
    class AFin,ANec,AViv,APrecio,AZona,ARegistro,ARec propiedad
```

## Descripción de los conceptos

La ontología organiza los conceptos necesarios para el funcionamiento del Sistema Experto de Asesoría para la Renta o Compra de Vivienda en Ensenada.

Las clases principales representan al usuario, su situación financiera, las viviendas, las zonas de la ciudad y los resultados de las evaluaciones.

La clase Vivienda presenta una jerarquía de especialización, ya que Casa y Departamento son tipos de vivienda.

Las zonas Centro, Valle Dorado, El Sauzal, Las Lomitas y Puerta del Mar se representan como instancias de la clase Zona.

Los precios de referencia se mantienen separados de las viviendas individuales, debido a que los valores recopilados durante la investigación no necesariamente representan el costo de una propiedad específica.

Asimismo, las opiniones comunitarias se representan de manera independiente a los riesgos territoriales documentados, evitando considerar comentarios personales como estadísticas oficiales de seguridad.

Las conexiones del diagrama permiten identificar cómo se relacionan los conceptos y qué información deberá utilizarse posteriormente durante el proceso de evaluación.

La ontología servirá como fundamento para organizar la base de conocimiento y facilitar la implementación de las reglas lógicas del Sistema Experto.