# Laboratorio 3
# Integración de Pruebas Automatizadas al Pipeline

## Objetivos

Al finalizar este laboratorio el estudiante será capaz de:

- Incorporar pruebas automatizadas dentro de un pipeline de CI/CD.
- Comprender la importancia de las pruebas como mecanismo de validación continua.
- Configurar la ejecución automática de pruebas unitarias.
- Generar y publicar reportes de resultados y cobertura de código.
- Implementar un Quality Gate básico que impida continuar el pipeline cuando existan errores en las pruebas.

---

# Descripción

En este laboratorio se ampliará el pipeline desarrollado en el Laboratorio 2 para incorporar una etapa de validación mediante pruebas automatizadas. Cada vez que se envíen cambios al repositorio, el pipeline deberá compilar la aplicación, ejecutar las pruebas unitarias y publicar los resultados obtenidos.

El objetivo es comprender cómo las pruebas automatizadas permiten detectar errores de manera temprana y garantizan que únicamente el código que cumple con los criterios mínimos de calidad continúe avanzando dentro del proceso de integración continua.

El laboratorio podrá desarrollarse utilizando **GitHub Actions** o **GitLab CI/CD**, manteniendo la equivalencia conceptual entre ambas plataformas.

---

# Requisitos

- Haber completado satisfactoriamente el Laboratorio 2.
- Repositorio con el pipeline de compilación funcionando correctamente.
- Proyecto de ejemplo con pruebas unitarias (o incorporar las pruebas proporcionadas por el docente).
- Visual Studio Code (o editor equivalente).

---

# Parte 1. Preparar el proyecto

1. Utilizar el mismo repositorio desarrollado en los laboratorios anteriores.
2. Verificar que el proyecto incluya pruebas unitarias ejecutables desde el entorno local.
3. Confirmar que todas las pruebas finalicen correctamente antes de modificar el pipeline.

---

# Parte 2. Incorporar la etapa de pruebas

Modificar el pipeline existente para que:

- ejecute las pruebas automáticamente después de la compilación;
- detenga la ejecución del pipeline cuando alguna prueba falle;
- muestre claramente el resultado de la ejecución de las pruebas en los registros.

La etapa de pruebas deberá ejecutarse únicamente cuando la compilación haya finalizado correctamente.

---

# Parte 3. Publicar resultados

Configurar el pipeline para generar y conservar como artefactos:

- el reporte de ejecución de pruebas;
- el reporte de cobertura de código (cuando la herramienta utilizada lo permita).

Verificar que ambos puedan descargarse desde la interfaz del pipeline.

---

# Parte 4. Simular un fallo

Introducir deliberadamente un error en una prueba o en el código fuente para provocar el fallo del pipeline.

Analizar:

- qué etapa falló;
- qué mensaje aparece en los registros;
- cómo el pipeline evita que una compilación defectuosa continúe.

Posteriormente corregir el error y verificar que el pipeline vuelva a ejecutarse exitosamente.

---

# Parte 5. Analizar la ejecución

Responder las siguientes preguntas:

1. ¿Por qué las pruebas automatizadas son un componente esencial de la Integración Continua?
2. ¿Qué diferencia existe entre una compilación exitosa y una validación exitosa?
3. ¿Qué ventajas aporta ejecutar las pruebas automáticamente después de cada cambio?
4. ¿Qué información proporciona el reporte de cobertura de código?
5. ¿Qué ocurriría si un pipeline permitiera continuar el proceso a pesar de que las pruebas fallen?
6. ¿Qué otros tipos de pruebas podrían incorporarse en las siguientes etapas del pipeline?

---

# Entregables

Cada estudiante deberá entregar:

- URL del repositorio actualizado.
- Archivo YAML del pipeline.
- Captura del pipeline ejecutado correctamente.
- Captura del pipeline con una ejecución fallida debido a una prueba.
- Captura de los reportes de pruebas y cobertura.
- Documento PDF con las respuestas al análisis.

---

# Criterios de evaluación

| Criterio | Puntos |
|----------|-------:|
| Integración correcta de la etapa de pruebas | 25 |
| Ejecución automática de pruebas unitarias | 20 |
| Publicación de reportes y cobertura | 20 |
| Evidencia del manejo de una ejecución fallida | 20 |
| Análisis técnico y conclusiones | 15 |

Total: **100 puntos**

---

# Resultado esperado

Al finalizar este laboratorio el estudiante dispondrá de un pipeline que compile automáticamente la aplicación y valide su funcionamiento mediante pruebas unitarias antes de permitir que el proceso continúe. El pipeline incorporará un primer mecanismo de control de calidad (*Quality Gate*), sentando las bases para integrar en los siguientes laboratorios verificaciones de seguridad, reutilización de componentes y estrategias de despliegue continuo.