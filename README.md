## Wikidata-IATEXT

Wikidata-IATEXT fue un proyecto que consistió en la curación y estructuración de datos relacionados con los miembros del Instituto de Análisis y Aplicaciones Textuales (IATEXT) de la ULPGC. El objetivo fue crear los elementos de todos los investigadores y sus respectivas publicaciones, tantas como fuese posible.

Se dividió en dos fases. La priemra dedacada a los investigadores y la segunda a las publicaciones. La primera consistió en la creación y modificación (ado que ya había elementos creados) de un total de 64 elementos. La segunda fase no tuvo límite debido a que no había una base de datos ni proyecto en el que aclarar esta cantidad y extraer los datos. Véase el apartado *[Resultados. Problemas principales](#Problemas principales)*.

El [informe final](https://www.wikidata.org/wiki/User:Iván_Hernández_Cazorla/IATEXT) se encuentra en inglés en Wikidata. Si el proyecto te parece interesante, te animo a leer el informe ya que está más ilustrado (cuadros y tablas) que en este archivo.

### Organización del repositorio
 - Hay dos carpetas principales: ``researchers`` y ``publications`` en las que se encuentran los documentos respectivos a ambos sujetos. Los documentos que amparen a ambos se guardarán en la raíz del repositorio hasta que organice mejor el repositorio.
 - Ambos CSV, [``researchers.csv``](researchers/researchers.csv) y [``publications.csv``](publications/publications.csv), fueron extraídos a partir de sus respectivas consultas SPARQL en el [Wikidata Query Service](https://query.wikidata.org) el 1 de octubre de 2018.
 - Si las consultas SPARQL se ejecutan en el [Wikidata Query Service](https://query.wikidata.org) es posible que arrojen más resultados que los que se almacenan en los CSV, dado que pueden haberse creado más elementos que cumplan esas condiciciones.
 - **Atención**: la consulta [``publications-per-year.rq``](publications-per-year.rq), y por lo tanto su correspondiente CSV, necesitan ser corregidas porque no muestran la cantidad real de elementos por año-autor.

### Metodología 

Al principio, antes de comenzar, el método para realizar esta tarea consistía en la creación de un archivo CSV con todas las propiedades y ejemplos de valores, la extracción de datos y la organization de estos en el CSV, para luego crear los elementos en masa con [QuickStatements](https://www.wikidata.org/wiki/Help:QuickStatements/es); finalmente, se revisarían los elementos para solucionar posibles [restricciones de las propiedades](https://wikidata.org/wiki/Help:Property_contraints_portal), corregir pares de propidad-valor erróneos, añadir pares necesarios en elementos concretos, y generar las identificadores/autoridades con el [script para el control de autoridades](https://www.wikidata.org/wiki/User:Magnus_Manske/authority_control.js) desarrollado por [Magnus Manske](https://www.wikidata.org/wiki/User:Magnus_Manske).

Sin embargo esto no funcionó del todo. En el caso de los investigadores fue más sencillo, pero con las publicaciones fue más complicado porque no hay un proyecto en el que sea posible extraer los datos de todas las publicaciones de los investigadores del IATEXT. Debido a esta situación las fuentes se delimitaron a tres: sitios web personales y oficiales, [Acceda](https://acceda.ulpgc.es) (repositorio institucional de la ULPGC) y [Dialnet](https://dialnet.unirioja.es) (base de datos bibliográfica). El problema principal con estas fuentes es que ninguna está bien estructurado, por lo que es imposible extraer de una modo sencillo los datos necesarios. Dialnet es, de las tres, la fuente más estrcuturada, pero no permite extraer su contenido, probablemente debido a la configuración de su archivo ``robots.txt``. Los datos en Acceda están muy mal estructurados, no parece que sean revisados ni corregidos, por lo que cualquier publicación que se suba con un error o en un formato incorecto en alguna propiedad/campo no se corrige a posteriori.

Debido a esto QuickStatements no fue muy útil, ya que insertar los datos en el CSV, para luego subirlos con QuickStatements y corregir posibles problemas era un trabajo doble. Por lo que el método cambió a insertar las publicaciones manualmente: elemento por elemento, propiedad por propiedad.

### Esquema de datos básicos

 - Para el esquema de los investigadores, véase *[Basic data to create an item for a researcher](https://www.wikidata.org/wiki/User:Iván_Hernández_Cazorla/IATEXT#Basic_data_to_create_an_item_for_a_researcher)*.
 - Para el esquema de las publicaciones, véase *[Basic data to create an item for a publication](https://www.wikidata.org/wiki/User:Iván_Hernández_Cazorla/IATEXT#Basic_data_to_create_an_item_for_a_publication)*.

### Progreso

 - [Fase uno: investigadores](https://www.wikidata.org/wiki/User:Iván_Hernández_Cazorla/IATEXT#Phase_one:_researchers).
 - [Fase dos: producción científica](https://www.wikidata.org/wiki/User:Iván_Hernández_Cazorla/IATEXT#Phase_two:_scientific_production) (por división del IATEXT).

### Resultados

Hasta el 21 de septimebre de 2018 se realizaron más de 43&nbsp;429 ediciones en el espacio de elementos de Wikidata y se editaron 1689 elementos, de los que 1430 fueron creados.

La fase uno terminó con la creación de los elementos para los 52 investigadores de plantilla, 3 posdoctorales, 2 predoctorales y 7 afiliados.
La fase dos terminó con 923-1079 elementos correspondientes a las publicaciones de los miembros del IATEXT. Además, durante esta fase han sido creados elementos que no están relacionados directamente con el IATEXT. Por ej., revistas científicas, obras coordinadas por investigadores externos y supervisores doctorales, entre otros.

 - En los archivos [``researchers.csv``](researchers/researchers.csv) y [``publications.csv``](publications/publications.csv) están los resultados.
 - En el apartado *[Resultados](https://wikidata.org/wiki/User:Iván_Hernández_Cazorla/IATEXT#Results)* del informe final en Wikidata hay dos tablas que comprueban cada día si hay nuevos elementos que reunan las condiciones de la consulta SPARQL introducida. Probablemente en un futuro haya más elementos de los que se han elaborado en este proyecto.

#### Problemas principales

A parte de los problemas ya mencionados en el apartado *[Metodología](#Metodología)*, al principio de este reporte, hubo algunos problemas que se deben mencionar:

 1. El instituto universitario (IATEXT) no tenía una lista con todos los miembros y sus datos completos, por lo que fue necesario encontrar los datos en diferentes fuentes. Ahora, el IATEXT puede obtener estos datos a partir de Wikidata.
 2. El punto anterior también se aplica a las publicaciones científicas.
 3. Los datos de las publicaciones almacenadas en Acceda no se pueden recopilar automáticamente debido a que no hay un modelo homogéneo entre ellas: cada autor entiende los «campos» que hay que completar a su manera, por lo que fue necesario revisar otras fuentes o incluso el documento para confirmar que el autor, o la persona que lo subió (no se puede saber si fue el autor o no), lo hizo correctamente.
 No será posible automatizar y refinar un conjunto de datos extraídos de Acceda hasta que las publicaciones sean revisadas.
 4. Dialnet ha sido la fuente principal de datos para añadir referencias. Al principio hubo un intento de automatizar la extracción de datos de las páginas de los investigadores, pero no funcionó debido a que su sitio web no permite el uso de arañas web. Además, no se disponía de tiempo suficiente como para desarrollar un programa para extraer todos los datos necesarios.
 5. El tiempo ha sido un factor importante. Aunque el proyecto fue planeado para una específica cantidad de meses, ha durado más tiempo del esperado debido a la gran cantidad de elementos que había que crear y a los problemas mencionados arriba. Es importante tener esto en cuenta de cara a planear un proyecto similar.

En resumen, el mayor problema ha sido la ausencia de una base de datos o un repositorio de datos estructurado realizado por la propia universidad o el instituto universitario.

### Financiación

Este proyecto ha sido financiado y promovido por el Instituto de Análisis y Aplicaciones Textuales (IATEXT) de la Universidad de Las Palmas de Gran Canaria.

### Licencia

 - Este repositorio se encuentran bajo la licencia [GNU General Public License v3.0](LICENSE).
 - La página del informe de Wikidata se encuentra bajo licencia [Creative Commons Atribución-CompartirIgual 3.0 Unported](https://www.wikidata.org/wiki/Wikidata:Copyright).
 - Todos los datos insertados en Wikidata se encuentran bajo [dominio público](https://www.wikidata.org/wiki/Wikidata:License). Wikidata se asegura de que esto se sepa utilizando la herramienta de dominio público [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).
