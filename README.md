# SoftMarket Refactor

Repositorio académico de ejemplo para la propuesta de mejora de ingeniería de software de SoftMarket S.A.

## Objetivo
Demostrar una estructura modular para el módulo de facturación, pruebas unitarias y un flujo de trabajo con Git basado en ramas y Pull Requests.

## Requisitos
- Python 3.10 o superior

## Ejecutar las pruebas
Desde la carpeta raíz del repositorio:

```bash
python -m unittest discover -s tests -v
```

## Estructura
```text
softmarket-refactor/
├── README.md
├── docs/
│   ├── propuesta-tecnica.md
│   └── flujo-versionamiento.md
├── src/
│   └── facturacion/
│       ├── __init__.py
│       ├── calculador_totales.py
│       └── servicio_facturacion.py
└── tests/
    └── test_facturacion.py
```

## Flujo de trabajo propuesto
1. Actualizar `main`.
2. Crear una rama `feature/...` o `fix/...`.
3. Desarrollar y ejecutar las pruebas.
4. Crear commits descriptivos.
5. Abrir un Pull Request.
6. Solicitar revisión de otro integrante.
7. Integrar en `main` cuando la revisión y las pruebas sean satisfactorias.

## Ejemplos de commits
- `feat: agregar calculo de totales`
- `refactor: separar responsabilidades de facturacion`
- `test: agregar pruebas del servicio de facturacion`
- `docs: documentar flujo de versionamiento`

> Nota académica: la tasa de impuesto usada en el ejemplo es configurable y solo ilustrativa. No representa una recomendación fiscal.
