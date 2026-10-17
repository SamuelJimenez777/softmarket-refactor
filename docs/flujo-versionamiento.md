# Flujo de versionamiento

```mermaid
flowchart TD
    A[Asignar tarea] --> B[Actualizar main]
    B --> C[Crear rama feature o fix]
    C --> D[Desarrollar y probar]
    D --> E[Crear commits descriptivos]
    E --> F[Subir rama remota]
    F --> G[Abrir Pull Request]
    G --> H[Revisión y pruebas CI]
    H --> I{¿Aprobado y pruebas correctas?}
    I -- No --> J[Corregir observaciones]
    J --> D
    I -- Sí --> K[Integrar en main]
    K --> L[Verificar versión integrada]
```

## Reglas
- No trabajar directamente sobre `main`.
- Usar una rama por tarea.
- Solicitar al menos una revisión de otro integrante.
- Corregir observaciones y ejecutar nuevamente las pruebas.
- Integrar únicamente cuando se cumplan los criterios acordados.
