# Informe de Laboratorio 2
# Branching, Pull Requests y Ejecución de CI

---

**Módulo:** Entornos de Integración y Entrega Continua (CI/CD)  
**Estudiante:** René Velásquez  
**Correo:** velasquez.rene@ficct.uagrm.edu.bo  
**Fecha:** 16 de Agosto de 2026  
**Plataforma CI/CD:** GitHub Actions  
**URL del Repositorio:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua)  
**URL del Pull Request #1:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/1](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/1)

---

## 1. Introducción y Objetivos

En este laboratorio se amplió el proyecto desarrollado en el Laboratorio 1, evolucionando desde un modelo simple basado únicamente en `push` directo hacia una **estrategia de branching basada en ramas de funcionalidad (Feature Branching)** integrada con **Pull Requests (PR)** y políticas de protección de la rama principal (`main`).

### Objetivos Alcanzados:
- Creación y gestión de la rama de funcionalidad `feature/update-readme`.
- Implementación del flujo de integración controlada mediante Pull Request.
- Configuración de eventos múltiples en GitHub Actions (`push` y `pull_request`).
- Establecimiento de reglas de protección en la rama `main` (requiriendo PR y validación de status checks).
- Experimentación con fallos deliberados y recuperación automática de la salud del pipeline.

---

## 2. Flujo de Trabajo y Estrategia de Branching

El flujo implementado garantiza que ningún desarrollador introduzca cambios directamente sobre `main`, protegiendo la estabilidad del código en producción:

```text
Developer (Local)
       ↓
Rama de funcionalidad (feature/update-readme)
       ↓
Commit & Push remoto
       ↓
Ejecución de CI en la rama
       ↓
Creación de Pull Request hacia main
       ↓
Ejecución de CI sobre el PR (Validación de Checks)
       ↓
Reglas de Protección (Branch Protection Rules)
       ↓
Revisión & Merge a main
```

---

## 3. Pipeline as Code (`.github/workflows/pipeline.yml`)

El pipeline se actualizó para reaccionar a eventos en ramas de funcionalidad y Pull Requests:

```yaml
name: Primer Pipeline CI

on:
  push:
    branches:
      - main
      - 'feature/**'
  pull_request:
    branches:
      - main

jobs:
  hello-ci:
    name: Hello CI
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Mostrar información del entorno
        run: |
          echo "================================"
          echo "         PIPELINE CI"
          echo "================================"
          echo "Repositorio: ${{ github.repository }}"
          echo "Evento:      ${{ github.event_name }}"
          echo "Rama/Ref:    ${{ github.ref_name }}"
          echo "Commit SHA:  ${{ github.sha }}"
          echo "================================"

      - name: Mostrar fecha y hora
        run: date

      - name: Mostrar versión de Git
        run: git --version

      - name: Simulacion de verificacion y build
        run: |
          echo "Ejecutando verificacion de build y consistencia..."
          test -f README.md && test -f app/hello.txt
          echo "Validacion de archivos requeridos: EXITOSA (OK)"

      - name: Finalizar pipeline
        run: echo "Pipeline ejecutado correctamente."
```

---

## 4. Evidencias de Ejecución (Capturas de Pantalla)

A continuación se detallan los enlaces y los recuadros donde insertar las capturas solicitadas en los entregables:

---

### 📸 Captura 1: Creación y Existencia de la Rama de Funcionalidad
* **Enlace directo:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/branches](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/branches)
* **Descripción:** Muestra la lista de ramas activas en GitHub, evidenciando la rama `feature/update-readme` creada a partir de `main`.

```
+---------------------------------------------------------------------------+
|                                                                           |
|                 [ PEGAR AQUÍ CAPTURA 1 - RAMAS / BRANCHES ]               |
|            (Muestra main y la rama feature/update-readme)                 |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 2: Ejecución del Pipeline en la Rama y en el Pull Request
* **Enlace directo:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions)
* **Descripción:** Muestra las ejecuciones del workflow en la pestaña *Actions*, evidenciando los eventos `push` y `pull_request` sobre la rama de funcionalidad.

```
+---------------------------------------------------------------------------+
|                                                                           |
|                 [ PEGAR AQUÍ CAPTURA 2 - HISTORIAL DE ACTIONS ]           |
|            (Muestra ejecuciones asociadas a feature/update-readme)         |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 3: Creación y Estado del Pull Request
* **Enlace directo:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/1](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/1)
* **Descripción:** Muestra el Pull Request #1 abierto desde `feature/update-readme` hacia `main` con su descripción y lista de commits.

```
+---------------------------------------------------------------------------+
|                                                                           |
|                  [ PEGAR AQUÍ CAPTURA 3 - PULL REQUEST #1 ]               |
|              (Muestra la vista principal del Pull Request #1)             |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 4: Reglas de Protección de la Rama Principal (`main`)
* **Enlace directo:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/settings/branches](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/settings/branches)
* **Descripción:** Muestra la configuración de **Branch Protection Rules** para la rama `main`, exigiendo Pull Request y el check obligatorio `Hello CI`.

```
+---------------------------------------------------------------------------+
|                                                                           |
|               [ PEGAR AQUÍ CAPTURA 4 - PROTECCIÓN DE MAIN ]               |
|          (Muestra las reglas de protección de rama en Settings)           |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 5: Simulación de Ejecución Fallida (Fallo Deliberado)
* **Enlace directo:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/31975074208](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/31975074208)
* **Descripción:** Muestra el fallo simulado en el pipeline (cruz roja ❌) y el bloqueo del Pull Request al no cumplirse el status check requerido.

```
+---------------------------------------------------------------------------+
|                                                                           |
|                [ PEGAR AQUÍ CAPTURA 5 - FALLO DEL PIPELINE ❌ ]            |
|          (Muestra el check fallido y el PR bloqueado para merge)          |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 6: Ejecución Corregida y Estado Exitoso
* **Enlace directo:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/31975118120](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/31975118120)
* **Descripción:** Muestra la recuperación del pipeline tras el commit de corrección (check verde `✓`) y el Pull Request listo para ser integrado.

```
+---------------------------------------------------------------------------+
|                                                                           |
|              [ PEGAR AQUÍ CAPTURA 6 - PIPELINE RECUPERADO ✓ ]             |
|          (Muestra la ejecución exitosa tras el commit de arreglo)         |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## 5. Respuestas a las Preguntas de Análisis

### Pregunta Inicial (Parte 1):
**¿Qué evento provoca actualmente la ejecución del pipeline?**  
> **Respuesta:** En el Laboratorio 1, el pipeline se disparaba exclusivamente ante eventos de tipo `push` directo sobre la rama `main`. Tras la evolución en este Laboratorio 2, el pipeline se dispara ante eventos de `push` (tanto en `main` como en ramas `feature/**`) y ante eventos de `pull_request` dirigidos a `main`.

---

### Preguntas de Flujo (Parte 6):

#### 1. ¿Por qué es conveniente trabajar en una rama independiente?
**Respuesta:**  
Trabajar en ramas de funcionalidad (*feature branches*) aísla el código en desarrollo respecto a la versión estable de producción (`main`). Esto previene que código incompleto o inestable afecte a otros miembros del equipo, facilita el desarrollo paralelo de múltiples funcionalidades y permite realizar experimentos o pruebas de forma segura sin comprometer el despliegue principal.

#### 2. ¿Qué ventaja proporciona realizar el Pull/Merge Request antes del merge?
**Respuesta:**  
El Pull Request actúa como una puerta de control de calidad (*Quality Gate*) y colaboración. Permite:
- Ejecutar pruebas y validaciones automáticas de CI sobre la combinación del código propuesto antes de incorporarlo.
- Facilitar la revisión por pares (*Code Review*), discusiones y sugerencias de mejora.
- Mantener una trazabilidad histórica del por qué y cómo se introdujo cada cambio.
- Aplicar políticas organizacionales obligatorias (aprobaciones, firmas, pruebas pasando).

#### 3. ¿En qué momento se ejecutó el pipeline?
**Respuesta:**  
El pipeline se ejecutó en dos momentos clave:
1. **Al hacer `push` a la rama remota `feature/update-readme`:** Validando los cambios de forma temprana en el entorno del desarrollador.
2. **Al abrir/actualizar el `Pull Request`:** Validando la integración potencial contra la rama `main`.

#### 4. ¿Qué ocurriría si el pipeline fallara?
**Respuesta:**  
Si el pipeline falla (como se demostró en la Parte 8):
- La plataforma marca el status check como **FAILURE / FAILED** (❌).
- Gracias a las reglas de protección de rama, el botón de **Merge queda bloqueado**, impidiendo que cualquier desarrollador fusione código defectuoso a `main`.
- Se generan logs detallados indicando la causa raíz del fallo para que el autor suba un nuevo commit correctivo sobre la misma rama.

#### 5. ¿Qué diferencia existe entre revisar código manualmente y validarlo mediante CI?
**Respuesta:**  
| Criterio | Revisión Manual (Code Review) | Validación Automatizada (CI) |
|---|---|---|
| **Enfoque** | Diseño, arquitectura, legibilidad, lógica de negocio y buenas prácticas. | Sintaxis, compilación, ejecución de tests, análisis estático, seguridad y formateo. |
| **Velocidad** | Lenta (depende de la disponibilidad del revisor humano). | Rápida e inmediata (minutos/segundos tras el push). |
| **Consistencia** | Subjetiva y propensa a descuidos u omisiones humanas. | 100% determinística y estandarizada en cada ejecución. |
| **Sinergia** | Ambos enfoques se complementan: el CI valida que el código funcione técnicamente para que el revisor humano se concentre en el valor del código. |

---

## 6. Conclusiones

1. La combinación de **Feature Branching + Pull Requests + CI/CD** constituye el estándar de la industria para el desarrollo colaborativo y seguro de software.
2. Las **Branch Protection Rules** aseguran que las directrices de calidad no dependan de la disciplina manual, sino que sean impuestas automáticamente por la plataforma.
3. El pipeline asume el rol de centinela del repositorio, permitiendo una detección temprana de errores (*Shift-Left Testing*) antes de que impacten ramas productivas.
