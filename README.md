
# POKEDÉX

![Galería de Imágenes](https://culturageek.com.ar/wp-content/uploads/2024/09/Pokemon-demanda-Pocketpair-www.culturageek.com_.ar_.webp)

- El trabajo consiste en implementar una aplicación web usando **[Django](https://docs.djangoproject.com/en/4.2/)** que permita buscar imágenes de **POKéMON**. La información será proporcionada mediante una API y luego renderizada por el *framework* en distintas *cards* que mostrarán -como mínimo- la imagen del Pokémon, los tipos del mismo, altura, peso y el nivel base en el que estos existen.

- Gran parte de la aplicación ya está resuelta: solo falta implementar las funcionalidades más importantes... ¿comenzamos? 😉.

### 📝 ¿Cómo empiezo?

1. Descargá e instalá **Visual Studio Code** desde ```https://code.visualstudio.com/```
    - Adicionalmente, se recomienda la instalación de las siguientes extensiones para facilitar el desarrollo:
        - After Dark.
        - Prettier - Code formatter.
        - Pylance.
        - Python.
        - Python Debugger.
    
    Finalizada la instalación, ejecutá el programa. Deberías ver algo como lo siguiente (muestra dentro del mismo TP):
    ![imagen](https://i.ibb.co/3R4KDCt/reg1.png)
    Guía oficial de instalación de extensiones disponible [aquí](https://code.visualstudio.com/docs/editor/extension-marketplace).

2. Instalá la última versión de Python desde ```www.python.org```. **Asegúrate de agregarlo al PATH durante la instalación:**

![imagen](https://i.postimg.cc/JnY2cVWq/python-image.png)

3. Creá una cuenta en GitHub [haciendo clic acá](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home). Luego, debés efectuar un *fork* (copia) del proyecto a tu repositorio (o al del grupo): [tutorial para hacer forks - thx. MitoCode](https://www.youtube.com/watch?v=9YUaf-uxuRM). **No te olvidés de mirar los clips de Git/GitHub al final de este documento**.

4. Cloná el repositorio copiado en tu máquina local (*git clone*). A continuación, dentro de la carpeta del repositorio local, abrí una terminal de *VS Code* e instalá Django ejecutando el siguiente comando:
```pip install django==4.2.10```

5. Instalá las dependencias necesarias:
```pip install -r requirements.txt```

6. Ejecutá el servidor Django (3000 representa el puerto donde se ejecutará la app):
```python manage.py runserver 3000```

7. Abrí tu navegador y dirigíte a ```http://localhost:3000``` para ver la aplicación. Deberá mostrar una pantalla como la siguiente: 
![imagen](https://i.ibb.co/kcVDhnZ/reg1.png)

8. Por último, para ver el contenido de la base integrada (SQLite), recomendamos el uso de **DB Browser for SQLite**. Link de descarga: https://sqlitebrowser.org/dl/
    - El archivo que se debe abrir es **db.sqlite3**.

### 📝 Lo que ya está implementado
- A nivel de **template**, se cuenta con 5 HTMLs: **header (cabecera de la página)**, **footer (pie de página)**, **home (sección donde se mostrarán las imágenes y el buscador)**, **index (contener principal que incluye a los 3 HTMLs anteriores)** y **favourites (panel para mostrar los favoritos en caso de implementarlos).** Para el caso del *header*, se implementó cierta lógica para determinar si un usuario está logueado (o no) y obtener así su nombre; para el caso del *home*, éste permite recorrer cada elemento de la API y dibujar su información en pantalla. El *footer* no posee acciones a nivel código relevantes para el desarrollo.

- A nivel de **vistas**, en el archivo **views.py** encontrarán algunas funciones semidesarrolladas: *index_page(request)* que muestra el contenido de 'index.html'; *home(request)* que obtiene todas las imágenes mapeadas de la API -a través de la capa de servicio- y los favoritos del usuario, y muestra el contenido de 'home.html' pasándole dicha información.

- A nivel de **lógica**, se incluye el archivo **transport.py** completo con todo el código necesario para consumir la API. Además, se anexa un **translator.py** con la lógica necesaria para convertir/mapear los resultados en una **Card** (objeto que finalmente se utilizará en el template para dibujar los resultados).

- El proyecto está construido sobre una **[arquitectura multicapas](https://medium.com/@e0324913/multilayered-software-architecture-1eaa97b8f49e)**, donde cada capa posee una única responsabilidad, a saber:
    - **Persistence** (empleada para el alta/baja/modificación (ABM) de objetos en una base de datos tipo fichero, llamada **[SQLite](https://www.youtube.com/watch?v=mZEpEVtSVtQ&pp=ygUNcXVlIGVzIHNxbGl0ZQ%3D%3D)**).
    - **Services** (usada para la lógica de negocio de la aplicación).
    - **Transport** (utilizada para el consumo de los datos de la API).
    - **Utilities** (almacena *translators* y demas elementos propios de la aplicación, usados en los templates).

Si bien no es un parámetro de evaluación dónde colocan las funciones, es altamente recomendado que las funciones que se agreguen estén en las capas que correspondan (consultar con los docentes en caso de dudas).

### 📝 ¿Qué voy a ver al iniciar la app?
- Al iniciar la aplicación y hacer clic sobre **Galería**, verás lo siguiente:
![imagen](https://i.ibb.co/Y71NF8w3/Captura-de-pantalla-2025-05-01-203110.png)


### 📝 Lo que falta hacer (OBLIGATORIO)

- Aún faltan implementar ciertas funciones de los módulos **views.py**, **services.py** y modificar el template **home.html**. Éstas son las encargadas de hacer que las imágenes de la galería se muestren:
    
    - **(1) views.py**:
        - *home(request):* obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template. Si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
        ![imagen](https://i.ibb.co/JRTsmDC/image.png)

    - **(2) services.py**:
        - *getAllImages:* obtiene un listado de imágenes convertidas **en cards** desde la API.
        ![imagen](https://i.ibb.co/TkpXGtr/image.png)
        
    - **(3) home.html**:
        - La card debe cambiar su *border color* dependiendo de los tipos mas iconicos, fuego, agua y planta. Si pertenece a **planta('grass' en ingles)**, mostrará un borde verde; si es de tipo **fuego ('fire')** mostrará rojo y si es de tipo **agua (water)**, será azul. Para cualquier otro tipo, será color naranja. Se sugiere consultar la **[documentación de Bootstrap sobre Cards](https://getbootstrap.com/docs/4.0/components/card/)** y **[cómo generar condicionales en Django](https://medium.com/powered-by-django/if-else-conditions-in-django-templates-5b3658cbf287)** para tener un mejor acercamiento a la solución.

**Concluido su desarrollo, deberían ver algo como lo siguiente:**
![imagen](https://i.ibb.co/Y71NF8w3/Captura-de-pantalla-2025-05-01-203110.png)
###### Notar el borde que posee cada imagen. ATENCIÓN: los pokémon pueden tener varios Tipos por lo que es posible listarlos con mejores estilos.

### 📝 Condiciones de entrega

- Requisitos de aprobación y criterios de corrección
    - El TP debe realizarse en grupos de 2 o 3 integrantes (no 1). Para aprobar el trabajo se deberán reunir los siguientes ítems:
      - **La galería de imágenes se muestra adecuadamente.**
      - El código debe ser **claro**. Las variables y funciones deben tener nombres que hagan fácil de entender el código a quien lo lea -de ser necesario, incluir comentarios que clarifiquen-. **Reutilizar el código mediante funciones todas las veces que se amerite.**
      - No deben haber variables que no se usan, funciones que tomen parámetros que no necesitan, ciclos innecesarios, etc.
    - **El 'correcto' funcionamiento del código NO es suficiente para la aprobación del TP, son necesarios todos los ítems anteriores.**



### 📝 Opcionales
Las siguientes funcionalidades del juego NO son necesarias para la aprobación (con nota mínima **4**), pero sirven para mejorar la calificación. De optar por hacerlas, se aplican las mismas reglas y criterios de corrección respecto de las funcionalidades básicas. Cualquier otra funcionalidad extra que se desee implementar debe ser antes consultada con los docentes.

**Los opcionales notados con ⭐ ya están parcialmente resueltos.** Se sugiere comenzar con ellos y luego seguir con los demás. **⚠️NO ES NECESARIO REALIZAR TODOS LOS OPCIONALES.⚠️** Enfóquense en los más relevantes, teniendo en cuenta el tiempo de desarrollo y pruebas.

**NOVEDAD: los opcionales notados con ✅ ya están resueltos en esta versión de la materia**.


- #### **Buscador I (según el nombre del pokémon)** ⭐
  - Se debe **completar** la funcionalidad para que el buscador filtre adecuadamente las imágenes, según los siguientes criterios:
    - Si el usuario **NO** ingresa dato alguno y hace clic sobre el botón 'Buscar', debe mostrar las mismas imágenes que si hubiese hecho clic sobre el enlace Galería.
    - Si el usuario ingresa algún dato (ej. *Pikachu*), al hacer clic en 'Buscar' se deben desplegar las imágenes filtradas relacionadas a dicho valor.

---

- #### **Buscador II (filtro según tipo fuego, agua o planta)** ⭐
  - Se debe **completar** la funcionalidad para que los 3 botones de filtrado de resultados funcionen, según los siguientes criterios:
    - Si se hace clic sobre **FUEGO**, debe mostrar resultados de pokemon con dicho tipo.
    - Ídem para el caso de **AGUA**.
    - Ídem para el caso de **PLANTA**.
 
  Ejemplo para *PLANTA*. **ATENCIÓN, la solucion mostrada es solo orientativa. puede haber mas o menos resultados**:
    ![imagen](https://i.ibb.co/1JKfGhZ6/filtro.jpg)

---

- #### **Inicio de sesión** ✅
  -  **En esta versión del TP se entrega resuelto.** [Tutorial de autenticación login/logout básica.](https://www.youtube.com/watch?v=oKuZQ238Ncc)

    ![imagen](https://i.ibb.co/nMHGFD9/session-1.png)
    ![imagen](https://i.ibb.co/cwzcBNx/session-2.png)

---

- #### **Favoritos** ⭐⭐ 
  - Se debe **completar** la lógica presente para permitir que un usuario logueado pueda almacenar una o varias imágenes de la galería como **favoritos**, mediante el clic de un botón en la parte inferior. 
  - **Observaciones**
    - Este punto puede realizarse SOLO si el ítem anterior (inicio de sesión) está desarrollado/funcionando bien.
    - Si el favorito ya fue añadido, debe mostrarse un botón que impida reañadirlo. 
    - Debe existir una sección llamada 'Favoritos' que permita listar todos los agregados por el usuario, mediante una tabla. Además, debe existir un botón que permita removerlo del listado (**si fue removido, desde la galería de imágenes podrá ser agregado otra vez**).
  - **Parte del código ya está resuelto**. Revisar los archivos *views.py*, *repositories.py* y *services.py*.
  
  Una posible visualización de este ítem resuelto es:
    ![imagen](https://i.ibb.co/0W2r0BM/basedatos.jpg)

---

- #### ALTA de nuevos usuarios
  - Actualmente la aplicación no permite el registro/alta de nuevos usuarios. Se desea implementar esta sección, para permitir que cualquier persona pueda registrarse en la aplicación.
  - Consideraciones:
    - Se debe solicitar nombre, apellido, usuario, contraseña y correo electrónico. **Si dos personas poseen el mismo nombre de usuario se anulará el alta, visualizando un mensaje descriptivo del error.**
    - El registro exitoso debe disparar un correo a la casilla indicada por el usuario, que indique en el cuerpo del mismo las credenciales de acceso.
  - Ayuda: [envío de emails usando cuenta @gmail a través de Django](https://github.com/akjasim/cb_django-sending-emails)
  
   ![imagen](https://mantpress.com/wp-content/uploads/02-03-22-X-plugins-para-el-registro-de-usuarios-en-tu-sitio-web-1200x630.png)

---

- #### *Loading Spinner* para la carga de imágenes
  - Se desea implementar una pantalla de carga/*loading spinner* que indique el usuario que espere hasta que la carga de imágenes se complete. **esto puede ser muy util si se demora la app al traer muchos datos**
  
  ![imagen](https://media.tenor.com/tEBoZu1ISJ8AAAAC/spinning-loading.gif)

---

- #### Renovar interfaz gráfica
  - Se debe proponer una nueva interfaz gráfica para los distintos *templates* de la aplicación. 
  - Recomendaciones:
    - Pueden usar el *framework CSS* que deseen, sea [Bootstrap](https://getbootstrap.com/), [Tailwind](https://tailwindcss.com/), [Foundation](https://get.foundation/), etc., siempre y cuando **consideren que el código debe resultar LEGIBLE para su corrección**.
    - Verificar que la lógica implementada en los *templates* funcione bien a medida que se modifica la interfaz.

  ![imagen](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShH3gYS_Po2eaj0zb9qsjWrSJttgdJe2C2PEKsrRGVhRrP89i968HBir68O_2PiUiGmn4&usqp=CAU)

---

### 📝 Fecha de entrega
El trabajo debe ser entregado en la fecha estipulada en el cronograma. **Recordar que es requisito hacer pre-entregas.**

### 📝 Formato de entrega
- La entrega se dividirá de 2 partes: **código** e **informe**:

  - **Parte 1: código:** todo el desarrollo debe estar en un repositorio interno del grupo (*fork* del repo base del TP). Se deben añadir a los docentes de la comisión con motivo de verificar los avances del mismo (corregir funciones, brindar sugerencias o recomendaciones, etc). Dado el caudal de alumnos, **serán responsables los estudiantes de notificar a los docentes para evaluar una pre-entrega, corregir alguna duda o similar que bloquee/impida del avance del TP**.
  
    Sugerimos:
      - Que cada integrante tenga su propia cuenta de GitHub, NO usar una única en el proyecto.
      - Cada integrante debe *commitear* una o varias porciones de código, dependiendo cómo distribuyan el trabajo. **Se debe visualizar el aporte individual al TP.**
  

  - **Parte 2: informe:** deben redactar un documento donde exista una introducción que explique de qué se trata el trabajo (sin utilizar lenguaje técnico), que incluya el código de las funciones implementadas y una breve explicación de cada una de ellas junto con las **dificultades de implementación** y **decisiones tomadas** -con su correspondiente justificación-. **NO incluir explicaciones de funcionalidades de Python, Django o similares**. Este documento debe estar en formato PDF anexo dentro de la carpeta del TP.
    
  🔥 **Se DEBE cumplir con ambas partes (código + informe) para aprobar el trabajo práctico.**


### 📝 Documentación adicional
- Documentación oficial de Django disponible aquí: https://docs.djangoproject.com/en/4.2/
- Sección **GIT**
    - Introducción a GIT: [clic acá](https://www.youtube.com/watch?v=mzHWafbVRyU).
    - Manejo de ramas/branches: [clic acá](https://www.youtube.com/watch?v=BRY9gamL9PE).
    - Merge & resolución de conflictos: [clic acá](https://www.youtube.com/watch?v=9YUaf-uxuRM).
    - Introducción a JSON: [clic acá](https://www.youtube.com/watch?v=FGG-UTCwlJw).
