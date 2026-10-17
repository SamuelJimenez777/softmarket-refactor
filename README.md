# SoftMarket Refactor

## Descripción
Este repositorio forma parte de una propuesta académica para mejorar el proceso de desarrollo de software de SoftMarket S.A. Se utiliza el módulo de facturación como ejemplo para aplicar buenas prácticas de programación, principios SOLID y control de versiones con Git.

## Objetivos
- Mejorar la organización y el mantenimiento del código.
- Separar las responsabilidades del módulo de facturación.
- Validar los datos utilizados en los cálculos.
- Aplicar un flujo de trabajo con ramas, commits y Pull Requests.
- Comprobar el funcionamiento mediante pruebas automatizadas.

## Tecnologías utilizadas
- Python 3.10 o superior.
- Git para el control de versiones.
- GitHub para alojar el repositorio y gestionar las revisiones.
- unittest para ejecutar las pruebas automatizadas.

## Estructura del proyecto

```text
softmarket-refactor/
├── docs/
│   ├── propuesta-tecnica.md
│   └── flujo-versionamiento.md
├── src/
│   └── facturacion/
│       ├── __init__.py
│       ├── calculador_totales.py
│       └── servicio_facturacion.py
├── tests/
│   └── test_facturacion.py
├── .gitignore
└── README.md
```

## Módulo de facturación
El módulo separa el cálculo de los totales de la coordinación del proceso de facturación. También valida que los precios no sean negativos y permite comprobar el comportamiento mediante pruebas automatizadas.

La tasa de impuesto utilizada en el ejemplo es ilustrativa y no representa una regla fiscal universal.

## Ejecutar las pruebas

Desde la carpeta raíz del proyecto, abre una terminal y ejecuta:

```bash
python -m unittest discover -s tests -v
```

Las pruebas verifican el cálculo del total, el almacenamiento y la notificación simulados, el rechazo de tasas negativas y la validación de precios negativos.

## Estrategia de versionamiento

Se propone utilizar las siguientes ramas:

- `main`: contiene la versión principal del proyecto.
- `feature/gestion-clientes`: representa el desarrollo de funcionalidades relacionadas con clientes.
- `feature/refactor-facturacion`: representa la mejora del módulo de facturación.
- `fix/calculo-impuestos`: representa una corrección relacionada con los cálculos.

El flujo de trabajo consiste en crear una rama por tarea, registrar cambios mediante commits descriptivos, subir la rama a GitHub, abrir un Pull Request y solicitar una revisión antes de integrar los cambios en `main`.

## Convención de commits

- `feat`: nueva funcionalidad.
- `fix`: corrección de errores.
- `refactor`: mejora de la estructura interna.
- `test`: incorporación o modificación de pruebas.
- `docs`: cambios en la documentación.

Ejemplo: `fix: validar precios negativos en facturacion`.

## Documentación adicional
- `docs/propuesta-tecnica.md`: describe la propuesta de mejora y la aplicación de SOLID.
- `docs/flujo-versionamiento.md`: presenta el flujo de trabajo con Git.

## Alcance
Este repositorio es una demostración académica. No representa un sistema comercial completo ni incluye conexiones reales con bases de datos o servicios de correo.