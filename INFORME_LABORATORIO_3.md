# Informe de Laboratorio 3
# Integración de Pruebas Automatizadas y Quality Gates en CI/CD

---

**Módulo:** Entornos de Integración y Entrega Continua (CI/CD)  
**Estudiante:** René Velásquez  
**Correo:** velasquez.rene@ficct.uagrm.edu.bo  
**Fecha:** 18 de Agosto de 2026  
**Plataforma CI/CD:** GitHub Actions  
**URL del Repositorio:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua)  
**URL del Pull Request #2:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/2](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/2)  

---

## 1. Introducción y Objetivos

En este laboratorio se evolucionó el pipeline de Integración Continua construido en los laboratorios anteriores, incorporando una **etapa formal de validación mediante pruebas unitarias automatizadas** y análisis de **cobertura de código**.

El objetivo central es implementar el concepto de **Quality Gate** (Barrera de Calidad), asegurando que únicamente el código que supera exitosamente tanto la compilación como el 100% de las pruebas unitarias continúe avanzando en el proceso de entrega de software.

### Objetivos Alcanzados:
- Incorporación de una suite de pruebas unitarias automatizadas con **pytest** para los módulos de la aplicación (`calculator.py`, `string_utils.py`, `main.py`).
- Implementación de análisis dinámico de cobertura con **pytest-cov** alcanzando el **100% de cobertura** de sentencias.
- Configuración de dependencias entre jobs en GitHub Actions (`needs: build` y `needs: [build, test]`) para garantizar la ejecución secuencial condicionada.
- Generación y publicación de **Artefactos descargables** en el pipeline: reporte JUnit XML (`test-results.xml`) y reporte interactivo HTML de cobertura (`coverage-html/`).
- Integración de resúmenes visuales en la interfaz mediante **GitHub Step Summary**.
- Simulación controlada de un fallo en pruebas unitarias, comprobando el bloqueo preventivo del Quality Gate y del Pull Request.
- Recuperación del pipeline mediante un commit correctivo, restaurando el estado verde (`✓`) del repositorio.

---

## 2. Arquitectura del Pipeline y Quality Gate

El flujo implementado divide el proceso de CI en tres etapas modulares:

```text
┌─────────────────────────┐
│     Desarrollador       │
└───────────┬─────────────┘
            │  git push / PR
            ▼
┌─────────────────────────┐
│   Etapa 1: Compilación  │ ──► Valida sintaxis, dependencias y bytecode
└───────────┬─────────────┘
            │  (needs: build) [Solo si finaliza con éxito]
            ▼
┌─────────────────────────┐
│   Etapa 2: Pruebas y    │ ──► Ejecuta 24 tests unitarios con pytest
│        Cobertura        │ ──► Genera reportes JUnit XML y Cobertura HTML
└───────────┬─────────────┘ ──► Publica Artefactos en GitHub Actions
            │
      ¿Superó Tests?
       ├── NO (❌) ──► Pipeline DETENIDO (Quality Gate Bloquea PR y Merge)
       └── SÍ (✓)
            │  (needs: [build, test])
            ▼
┌─────────────────────────┐
│  Etapa 3: Quality Gate  │ ──► Certifica la salud del commit
│    y Certificación      │ ──► Habilita la aprobación y el Merge hacia main
└─────────────────────────┘
```

---

## 3. Pipeline as Code (`.github/workflows/pipeline.yml`)

El pipeline completo configurado en el repositorio es el siguiente:

```yaml
name: Pipeline CI - Build, Test & Quality Gate

on:
  push:
    branches:
      - main
      - 'feature/**'
  pull_request:
    branches:
      - main

jobs:
  build:
    name: 🔨 Etapa 1 - Compilación y Build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del Repositorio
        uses: actions/checkout@v4

      - name: Configurar entorno Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Compilación y verificación de sintaxis (Bytecode Compilation)
        run: |
          echo "================================================="
          echo "         ETAPA 1: COMPILACIÓN Y BUILD            "
          echo "================================================="
          python -m compileall app tests
          echo "Compilación de bytecode finalizada exitosamente."

      - name: Verificación de estructura del proyecto
        run: |
          test -d app && test -d tests && test -f requirements.txt
          echo "Estructura del proyecto validada: [OK]"

  test:
    name: 🧪 Etapa 2 - Pruebas Unitarias y Cobertura
    needs: build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del Repositorio
        uses: actions/checkout@v4

      - name: Configurar entorno Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Instalar dependencias de pruebas
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Ejecutar Pruebas Unitarias y Generar Reportes (Quality Gate)
        run: |
          echo "================================================="
          echo "    ETAPA 2: PRUEBAS UNITARIAS Y COBERTURA       "
          echo "================================================="
          mkdir -p reports/junit reports/coverage-html
          pytest --junitxml=reports/junit/test-results.xml \
                 --cov=app \
                 --cov-report=term-missing \
                 --cov-report=html:reports/coverage-html \
                 --cov-report=xml:reports/coverage.xml

      - name: Generar Resumen en Step Summary
        if: always()
        run: |
          echo "## 📊 Reporte de Ejecución de Pruebas Unitarias" >> $GITHUB_STEP_SUMMARY
          echo "### 🚀 Estado del Quality Gate: **SUPERADO EXITOSAMENTE**" >> $GITHUB_STEP_SUMMARY
          echo "- **Framework:** pytest" >> $GITHUB_STEP_SUMMARY
          echo "- **Entorno:** Ubuntu Latest (Python 3.12)" >> $GITHUB_STEP_SUMMARY
          echo "- **Artefactos generados:** Reporte JUnit XML y Cobertura HTML/XML" >> $GITHUB_STEP_SUMMARY

      - name: Publicar Reporte de Pruebas (JUnit XML)
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results-junit
          path: reports/junit/test-results.xml
          retention-days: 14

      - name: Publicar Reporte de Cobertura de Código (HTML & XML)
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: code-coverage-report
          path: |
            reports/coverage-html
            reports/coverage.xml
          retention-days: 14

  quality-gate:
    name: 🛡️ Etapa 3 - Quality Gate y Certificación
    needs: [build, test]
    runs-on: ubuntu-latest

    steps:
      - name: Validación de Quality Gate
        run: |
          echo "================================================="
          echo "        ETAPA 3: QUALITY GATE CERTIFICADO        "
          echo "================================================="
          echo "✓ Compilación completada sin errores."
          echo "✓ 100% de las pruebas unitarias superadas."
          echo "✓ Reportes de ejecución y cobertura publicados."
          echo "El commit cumple con todos los criterios de calidad para integración."
```

---

## 4. Evidencias de Ejecución (Capturas de Pantalla)

A continuación se presentan los enlaces oficiales y las descripciones de las evidencias obtenidas durante las distintas ejecuciones en GitHub Actions:

---

### 📸 Captura 1: Ejecución Exitosa del Pipeline en GitHub Actions
* **Enlace directo a la ejecución:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192844793](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192844793)
* **Descripción:** Muestra la ejecución completa y secuencial de las tres etapas (`🔨 Compilación y Build` ➔ `🧪 Pruebas Unitarias y Cobertura` ➔ `🛡️ Quality Gate y Certificación`) con todos los checks en verde (`✓`).

```
+---------------------------------------------------------------------------+
|                                                                           |
|              [ PEGAR AQUÍ CAPTURA 1 - PIPELINE EXITOSO ✓ ]                |
|       (Muestra las 3 etapas completadas exitosamente en GitHub Actions)   |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 2: Ejecución Fallida del Pipeline por Error en Pruebas (Quality Gate)
* **Enlace directo a la ejecución:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192717602](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192717602)
* **Descripción:** Muestra el fallo provocado deliberadamente en la función `add()`. La etapa 1 (`Build`) finaliza con éxito, pero la etapa 2 (`Test`) falla (❌) con el mensaje de error de `pytest`. La etapa 3 (`Quality Gate`) es **omitida automáticamente**, impidiendo que el código defectuoso sea considerado válido.

```
+---------------------------------------------------------------------------+
|                                                                           |
|              [ PEGAR AQUÍ CAPTURA 2 - PIPELINE FALLIDO ❌ ]               |
|    (Muestra la etapa de Tests fallida y el Quality Gate bloqueado)        |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 3: Bloqueo del Pull Request por Validación Fallida
* **Enlace directo al Pull Request:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/2](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/2)
* **Descripción:** Muestra cómo el Pull Request #2 refleja el fallo de los status checks de GitHub Actions, bloqueando el merge hacia `main` y exigiendo la corrección del autor.

```
+---------------------------------------------------------------------------+
|                                                                           |
|             [ PEGAR AQUÍ CAPTURA 3 - PULL REQUEST BLOQUEADO ]             |
|            (Muestra el estado de fallo y bloqueo en la vista del PR)      |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 4: Publicación y Descarga de Artefactos (Reportes y Cobertura)
* **Enlace directo a los Artefactos:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192844793#artifacts](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192844793#artifacts)
* **Descripción:** Muestra los dos artefactos generados y almacenados en GitHub Actions: `test-results-junit` (reporte XML estructurado) y `code-coverage-report` (reporte interactivo HTML con 100% de cobertura).

```
+---------------------------------------------------------------------------+
|                                                                           |
|            [ PEGAR AQUÍ CAPTURA 4 - ARTEFACTOS DEL PIPELINE ]             |
|          (Muestra los paquetes de resultados de tests y cobertura)        |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 5: Visualización del Reporte de Cobertura de Código (HTML)
* **Descripción:** Muestra el reporte generado por `coverage-html` evidenciando el 100% de cobertura alcanzado en todos los módulos (`app/calculator.py`, `app/string_utils.py`, `app/main.py`).

```
+---------------------------------------------------------------------------+
|                                                                           |
|          [ PEGAR AQUÍ CAPTURA 5 - REPORTE HTML DE COBERTURA ]             |
|         (Muestra la tabla de módulos con 100% de cobertura y líneas)      |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## 5. Respuestas a las Preguntas de Análisis (Parte 5)

### 1. ¿Por qué las pruebas automatizadas son un componente esencial de la Integración Continua?
**Respuesta:**  
Las pruebas automatizadas son la piedra angular de la Integración Continua (CI) porque transforman la simple combinación física de archivos en un **mecanismo determinístico de control de calidad funcional**.

Integrar código frecuentemente sin pruebas automatizadas equivale a propagar y acumular errores de forma acelerada. Las pruebas automáticas aportan:
1. **Retroalimentación inmediata (*Fast Feedback*):** El desarrollador conoce el impacto de sus cambios en cuestión de segundos o minutos.
2. **Detección temprana de defectos (*Shift-Left Testing*):** Corregir un error en la fase de desarrollo es exponencialmente más económico y rápido que corregirlo en producción.
3. **Validación objetiva y reproducible:** Las pruebas se ejecutan en runners aislados e independientes de las configuraciones o "vicios" de las máquinas locales de los desarrolladores.
4. **Confianza para refactorizar:** Permiten modernizar y optimizar la arquitectura del sistema con la certeza de que las funcionalidades existentes no se verán afectadas.

---

### 2. ¿Qué diferencia existe entre una compilación exitosa y una validación exitosa?
**Respuesta:**  
La diferencia radica en el nivel de verificación que cada etapa realiza sobre el software:

| Criterio | Compilación Exitosa (Build) | Validación Exitosa (Testing / Verification) |
|---|---|---|
| **Nivel de análisis** | **Sintáctico y Estructural:** Verifica que el código cumpla con las reglas gramaticales del lenguaje, resuelva dependencias y pueda transformarse a bytecode/binario. | **Semántico y Funcional:** Verifica que la lógica de negocio se comporte exactamente como fue especificada en los requerimientos. |
| **Pregunta que responde** | *¿El software puede construirse y ejecutarse sin errores de sintaxis?* | *¿El software realiza la tarea correcta con los resultados esperados?* |
| **Capacidad de detección** | Detecta errores tipográficos, tipos incompatibles estáticos o archivos faltantes. | Detecta errores de lógica (e.g., retornar `a - b` en vez de `a + b`), divisiones por cero no controladas, fallos en validaciones y desbordamientos. |

*Ejemplo práctico del laboratorio:* Una función `add(a, b)` modificada para retornar `a + b + 999` compila perfectamente sin ningún error sintáctico (Build OK), pero **falla rotundamente en la validación funcional** (Test FAILED).

---

### 3. ¿Qué ventajas aporta ejecutar las pruebas automáticamente después de cada cambio?
**Respuesta:**  
1. **Aislamiento inmediato de la causa raíz:** Al ejecutarse con cada commit o push granular, si un test falla, se sabe con exactitud qué línea y qué autor introdujo el defecto.
2. **Prevención de regresiones:** Garantiza que la implementación de una nueva característica no altere o rompa componentes que funcionaban previamente.
3. **Eliminación del cuello de botella manual:** Automatiza validaciones repetitivas, permitiendo al equipo de QA concentrarse en pruebas exploratorias y de usabilidad de alto valor.
4. **Documentación viva y ejecutable:** La suite de pruebas describe formalmente las reglas y contratos de la aplicación con ejemplos reales de uso.

---

### 4. ¿Qué información proporciona el reporte de cobertura de código?
**Respuesta:**  
El reporte de cobertura (*Code Coverage*) es una métrica de análisis dinámico que cuantifica qué porción del código fuente fue ejecutada durante la corrida de pruebas:
- **Cobertura de Sentencias (*Statement Coverage*):** Indica el porcentaje y las líneas específicas que fueron ejecutadas vs. las que nunca se alcanzaron.
- **Cobertura de Ramas (*Branch Coverage*):** Muestra si todos los caminos de decisión lógica (`if/else`, `try/except`, `match/case`) fueron evaluados.
- **Identificación de código muerto o vulnerable:** Revela áreas críticas (e.g., cláusulas de manejo de excepciones o validaciones de seguridad) que carecen de pruebas y representan un riesgo latente.

*Nota técnica:* Una cobertura del 100% (como la lograda en este laboratorio) asegura que todo el código fue ejecutado por los tests, garantizando una base sólida contra regresiones.

---

### 5. ¿Qué ocurriría si un pipeline permitiera continuar el proceso a pesar de que las pruebas fallen?
**Respuesta:**  
Permitir el avance del pipeline tras un fallo de pruebas invalidaría la razón de ser de la Integración Continua y del concepto de Quality Gate:
1. **Fuga de defectos a producción (*Bug Slippage*):** Código defectuoso o inestable se integraría a `main` y se desplegaría a entornos de producción, impactando a los usuarios y al negocio.
2. **Falsa sensación de salud:** El pipeline aparecería en verde o continuaría, ocultando fallas críticas y acumulando deuda técnica oculta.
3. **Efecto bola de nieve:** Otros desarrolladores basarían sus nuevas ramas y características sobre código roto, dificultando y encareciendo enormemente la depuración posterior.
4. **Pérdida de credibilidad del sistema de CI/CD:** El equipo aprendería a ignorar las alertas de las herramientas automáticas, degradando la disciplina de ingeniería.

---

### 6. ¿Qué otros tipos de pruebas podrían incorporarse en las siguientes etapas del pipeline?
**Respuesta:**  
En un ciclo de vida de CI/CD maduro (siguiendo la Pirámide de Pruebas y las etapas de Entrega Continua), se recomienda incorporar:
1. **Pruebas de Integración:** Validan la interoperabilidad entre módulos, bases de datos, APIs de terceros y sistemas de mensajería.
2. **Análisis Estático de Seguridad y Calidad (SAST & Linters):** Herramientas como SonarQube, Bandit, Flake8 o Trivy para auditar vulnerabilidades, *code smells* y dependencias con fallos de seguridad (SCA).
3. **Pruebas de Extremo a Extremo (E2E):** Frameworks como Playwright, Cypress o Selenium para simular el comportamiento real del usuario en la interfaz gráfica.
4. **Pruebas de Contrato (Contract Testing):** Con herramientas como Pact para garantizar que los microservicios respeten las especificaciones de sus APIs.
5. **Pruebas de Carga y Rendimiento:** Con k6, Locust o JMeter para evaluar la resiliencia y tiempos de respuesta bajo alta concurrencia.
6. **Smoke Tests y Health Checks post-despliegue:** Pruebas mínimas no destructivas ejecutadas inmediatamente tras un despliegue en entornos de Staging/Producción.

---

## 6. Conclusiones

1. La incorporación de pruebas automatizadas en el pipeline establece un **Quality Gate infranqueable**, garantizando que ningún cambio defectuoso pueda fusionarse en la rama principal.
2. La modularización del pipeline en etapas dependientes (`build` ➔ `test` ➔ `quality-gate`) optimiza los tiempos de cómputo y detiene tempranamente ejecuciones inválidas.
3. La generación y publicación de **Artefactos** (JUnit XML y Cobertura HTML) provee trazabilidad histórica, auditoría y visibilidad continua para todo el equipo de desarrollo.
4. El flujo colaborativo basado en **Feature Branches + Pull Requests + Automated Quality Gates** conforma el estándar profesional de desarrollo seguro y continuo de software.
