# Laboratorio 2

# Branching, Pull Requests y Ejecución de CI

## Objetivos

Al finalizar este laboratorio el estudiante será capaz de:

* Crear y gestionar ramas de trabajo utilizando Git.
* Aplicar una estrategia de branching basada en ramas de funcionalidad.
* Utilizar Pull Requests o Merge Requests como mecanismo de integración.
* Asociar eventos de Git con ejecuciones automáticas de CI.
* Comprender la relación entre branching, revisión de código y CI/CD.
* Aplicar reglas básicas para proteger la rama principal.

---

# Descripción

En este laboratorio se ampliará el repositorio desarrollado en el Laboratorio 1.

El pipeline construido anteriormente continuará siendo utilizado, pero ahora el flujo de trabajo incorporará una estrategia de branching basada en ramas de funcionalidad y Pull Requests/Merge Requests.

El objetivo no es solamente aprender a crear ramas, sino comprender cómo una organización puede establecer reglas para controlar la incorporación de cambios al código principal.

El laboratorio podrá realizarse utilizando **GitHub Actions** o **GitLab CI/CD**.

---

# Escenario

Suponga que forma parte de un equipo de desarrollo que mantiene una aplicación.

La organización establece las siguientes reglas:

* `main` representa la versión principal del proyecto.
* Los desarrolladores no deben trabajar directamente sobre `main`.
* Cada cambio debe desarrollarse en una rama independiente.
* Las ramas deben utilizar nombres descriptivos.
* Los cambios deben incorporarse mediante Pull Request o Merge Request.
* El pipeline de CI debe ejecutarse automáticamente para validar el cambio.
* Un cambio no debería integrarse si las validaciones obligatorias fallan.

A partir de estas reglas deberá implementar el flujo de trabajo.

---

# Requisitos

* Haber completado satisfactoriamente el Laboratorio 1.
* Tener funcionando el pipeline básico.
* Git instalado.
* Cuenta en GitHub o GitLab.
* Visual Studio Code o editor equivalente.

---

# Parte 1. Analizar el repositorio

Antes de realizar cambios:

1. Revisar el repositorio utilizado en el Laboratorio 1.
2. Identificar la rama principal.
3. Revisar el archivo del pipeline.
4. Ejecutar el pipeline actual.
5. Verificar que finalice correctamente.

Responder:

> ¿Qué evento provoca actualmente la ejecución del pipeline?

---

# Parte 2. Crear una rama de funcionalidad

Crear una nueva rama para incorporar una modificación.

Utilizar una convención descriptiva, por ejemplo:

```text
feature/update-readme
```

o:

```text
feature/add-project-info
```

La rama debe crearse a partir de `main`.

Ejemplo:

```bash
git switch main
git pull
git switch -c feature/update-readme

# Usando git checkout
git checkout -b feature/12345_update_readme
git push -u origin feature/12345_update_readme

```

---

# Parte 3. Realizar un cambio

Modificar el proyecto.

Por ejemplo:

* Actualizar `README.md`.
* Agregar información del proyecto.
* Incorporar una nueva sección.
* Agregar un archivo de documentación.

Realizar un commit descriptivo:

```bash
git add .
git commit -m "docs: update project documentation"
```

Enviar la rama al repositorio remoto:

```bash
git push -u origin feature/update-readme

# Si la rama ya fue enviada, entonces solo hacer push de los cambios
git push
```

---

# Parte 4. Observar la ejecución de CI

Después del `push`:

1. Acceder a la plataforma.
2. Revisar si el pipeline fue ejecutado.
3. Identificar qué evento provocó la ejecución.
4. Identificar el job.
5. Identificar el runner.
6. Revisar los logs.

Registrar la evidencia de la ejecución.

---

# Parte 5. Crear un Pull Request / Merge Request

Crear un:

* **Pull Request**, si utiliza GitHub.
* **Merge Request**, si utiliza GitLab.

La solicitud debe:

* Tener un título descriptivo.
* Explicar brevemente el cambio realizado.
* Indicar qué archivos fueron modificados.
* Asociarse con la rama `main`.

---

# Parte 6. Analizar el flujo

Observar la relación entre:

```text
Developer
    ↓
Feature Branch
    ↓
Commit
    ↓
Push
    ↓
CI Pipeline
    ↓
Pull / Merge Request
    ↓
Review
    ↓
Merge
    ↓
main
```

Responder:

1. ¿Por qué es conveniente trabajar en una rama independiente?
2. ¿Qué ventaja proporciona realizar el Pull/Merge Request antes del merge?
3. ¿En qué momento se ejecutó el pipeline?
4. ¿Qué ocurriría si el pipeline fallara?
5. ¿Qué diferencia existe entre revisar código manualmente y validarlo mediante CI?

---

# Parte 7. Protección de la rama principal

Configurar, cuando la plataforma lo permita, reglas básicas de protección para `main`.

Como mínimo:

* Evitar modificaciones directas.
* Requerir Pull Request/Merge Request.
* Requerir que las validaciones de CI sean exitosas antes del merge.

> **Nota:** Las opciones disponibles pueden variar según la plataforma y el nivel de servicio utilizado.

---

# Parte 8. Experimentación

Realizar una segunda modificación que provoque deliberadamente una ejecución fallida del pipeline.

Observar:

* Estado del Pull/Merge Request.
* Resultado del pipeline.
* Mensajes de error.
* Posibilidad o imposibilidad de realizar el merge según las reglas configuradas.

Posteriormente corregir el problema y conseguir una ejecución exitosa.

---

# Entregables

Cada estudiante deberá entregar:

1. URL del repositorio.
2. Captura de la rama de funcionalidad.
3. Captura del pipeline ejecutado.
4. URL o captura del Pull Request/Merge Request.
5. Evidencia de la protección de `main`.
6. Evidencia de una ejecución fallida.
7. Evidencia de la ejecución corregida.
8. Documento PDF con las respuestas de análisis.

---

# Criterios de evaluación

| Criterio                                   |  Puntos |
| ------------------------------------------ | ------: |
| Creación y utilización correcta de la rama |      15 |
| Implementación del flujo Branch → PR/MR    |      20 |
| Ejecución correcta del pipeline            |      20 |
| Configuración de protección de `main`      |      15 |
| Simulación y análisis del fallo            |      15 |
| Análisis conceptual                        |      15 |
| **Total**                                  | **100** |

---

# Resultado esperado

Al finalizar el laboratorio, el estudiante habrá evolucionado el pipeline del Laboratorio 1 desde un proceso basado únicamente en `push` hacia un flujo de trabajo colaborativo basado en ramas y Pull/Merge Requests.

El estudiante deberá comprender que:

> **La estrategia de branching define cómo fluye el código dentro del equipo, mientras que CI/CD automatiza las verificaciones necesarias para controlar ese flujo.**

Este modelo será utilizado posteriormente para incorporar compilación, pruebas, Quality Gates y controles de seguridad.
