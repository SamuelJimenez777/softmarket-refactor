# Propuesta técnica

## Problema
La duplicación de código, las responsabilidades mezcladas y las dependencias directas dificultan el mantenimiento del sistema.

## Ejemplo seleccionado
Se utiliza el módulo de facturación para mostrar una separación entre:
- `CalculadorTotales`: calcula el total.
- `ServicioFacturacion`: coordina el proceso.
- Repositorio: persiste la factura mediante el contrato `guardar(cliente, total)`.
- Notificador: envía la notificación mediante el contrato `enviar(email, total)`.

## Relación con SOLID
- **SRP:** el cálculo y la coordinación del proceso están separados.
- **OCP:** se puede extender el cálculo creando implementaciones compatibles con el mismo contrato.
- **LSP:** las implementaciones intercambiables deben respetar el comportamiento esperado de sus contratos.
- **ISP:** almacenamiento y notificación son responsabilidades separadas, no una interfaz gigante.
- **DIP:** el servicio recibe sus dependencias desde fuera, en lugar de crear conexiones concretas.

La demostración es educativa y puede ampliarse con interfaces formales, manejo de errores y reglas de negocio reales.
