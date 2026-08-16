# Informe de Laboratorio 1
# Primer Pipeline de Integración Continua (CI/CD)

---

**Módulo:** Entornos de Integración y Entrega Continua (CI/CD)  
**Estudiante:** René Velásquez  
**Correo:** velasquez.rene@ficct.uagrm.edu.bo  
**Fecha de Ejecución:** 16 de Agosto de 2026  
**Plataforma CI/CD:** GitHub Actions  
**URL del Repositorio:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua)

---

## 1. Introducción y Objetivos

El presente laboratorio tiene como finalidad configurar el primer pipeline de Integración Continua (CI) del módulo, aplicando el paradigma de **Pipeline as Code** mediante **GitHub Actions**. A través de esta práctica se valida la automatización ante eventos de `push`, la asignación de runners en la nube y el análisis de logs de ejecución.

### Objetivos Específicos
- Configurar un repositorio en Git y sincronizarlo con GitHub.
- Definir un pipeline declarativo en formato YAML (`.github/workflows/pipeline.yml`).
- Automatizar la ejecución de tareas de verificación tras cada `push`.
- Analizar el comportamiento, runners y registros generados por el pipeline.

---

## 2. Estructura del Repositorio

El proyecto cuenta con la estructura estandarizada solicitada en la guía:

```text
Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/
│
├── .github/
│   └── workflows/
│       └── pipeline.yml       # Definición del flujo de trabajo de GitHub Actions
├── app/
│   └── hello.txt              # Archivo de texto requerido por la práctica
├── README.md                  # Documentación general del repositorio
├── INFORME_LABORATORIO_1.md   # Informe y respuestas de análisis
└── laboratorio1.md            # Guía del laboratorio
```

---

## 3. Archivo YAML Utilizado (Pipeline as Code)

Ruta del archivo en el repositorio: `.github/workflows/pipeline.yml`

```yaml
name: Primer Pipeline CI

on:
  push:
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
          echo "      PRIMER PIPELINE CI"
          echo "================================"
          echo "Repositorio: ${{ github.repository }}"
          echo "Rama: ${{ github.ref_name }}"
          echo "Commit: ${{ github.sha }}"
          echo "================================"

      - name: Mostrar fecha y hora
        run: date

      - name: Mostrar versión de Git
        run: git --version

      - name: Finalizar pipeline
        run: echo "Pipeline ejecutado correctamente."
```

---

## 4. Evidencias de Ejecución (Capturas de Pantalla)

> 💡 **Instrucciones:** Reemplaza los bloques de abajo insertando las capturas de pantalla tomadas desde los enlaces proporcionados.

### 📸 Captura 1: Vista General de la Ejecución en GitHub Actions
* **Enlace para captura:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions)
* **Descripción:** Muestra la lista de workflows ejecutados en la pestaña *Actions*, evidenciando el estado exitoso (check verde `✓`) para el commit en la rama `main`.

```
+---------------------------------------------------------------------------+
|                                                                           |
|                  [ PEGAR AQUÍ CAPTURA 1 - ACTIONS LIST ]                  |
|          (Muestra el workflow "Primer Pipeline CI" en verde ✓)            |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

### 📸 Captura 2: Detalle de los Pasos y Logs de Ejecución
* **Enlace para captura:** [https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/31972143411](https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/31972143411)
* **Descripción:** Muestra el detalle del job `Hello CI` con los pasos desplegados mostrando los logs de salida (`echo`, `date`, `git --version` y finalización exitosa).

```
+---------------------------------------------------------------------------+
|                                                                           |
|                   [ PEGAR AQUÍ CAPTURA 2 - LOGS DEL JOB ]                 |
|         (Muestra los pasos y la salida de la consola del Runner)          |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## 5. Respuestas a las Preguntas de Análisis

A continuación se responden de forma técnica y detallada las preguntas planteadas en la Parte 4 del laboratorio:

### 1. ¿Qué evento inició el pipeline?
**Respuesta:**  
El pipeline fue iniciado por un evento de tipo **`push`** hacia la rama `main`. En GitHub Actions, la directiva `on.push.branches: [main]` monitorea el repositorio y desencadena el workflow cada vez que se suben nuevos commits a dicha rama.

### 2. ¿Cuánto tiempo tardó en ejecutarse?
**Respuesta:**  
El tiempo total de ejecución fue de aproximadamente **12 segundos**. Este tiempo comprende la solicitud y aprovisionamiento del runner, la descarga de la acción `actions/checkout@v4`, la ejecución de los comandos de shell y las tareas de limpieza posteriores (*Post Job*).

### 3. ¿En qué sistema operativo se ejecutó?
**Respuesta:**  
Se ejecutó sobre el sistema operativo **Linux Ubuntu** en su versión LTS más reciente soportada por la plataforma, especificado en el archivo YAML mediante la directiva `runs-on: ubuntu-latest`.

### 4. ¿Qué runner ejecutó el pipeline?
**Respuesta:**  
Fue ejecutado por un **GitHub-hosted Runner** (un runner estándar administrado por GitHub en la nube de Microsoft Azure). Se trata de una máquina virtual efímera y aislada que se inicia bajo demanda y se destruye tras finalizar el job.

### 5. ¿Qué información muestran los logs?
**Respuesta:**  
Los logs reflejan de manera cronológica cada una de las fases del job:
1. **Set up job:** Configuración del entorno virtual y descarga de componentes del runner.
2. **Checkout repository:** Descarga del código fuente del repositorio y checkout al commit exacto (`4adf30f`).
3. **Mostrar información del entorno:** Impresión de variables de contexto de GitHub (`github.repository`, `github.ref_name`, `github.sha`).
4. **Mostrar fecha y hora:** Salida del comando `date` (`Sun Aug 16 20:59:28 UTC 2026`).
5. **Mostrar versión de Git:** Salida del comando `git --version` (`git version 2.54.0`).
6. **Finalizar pipeline:** Confirmación de ejecución exitosa con código de salida `0` (*exit code 0*).
7. **Post-job y Complete job:** Limpieza de procesos y reporte final de métricas.

### 6. ¿Qué ocurriría si el archivo YAML contiene un error de sintaxis?
**Respuesta:**  
Si el archivo contiene un error de sintaxis (por ejemplo, mala indentación, claves mal escritas o caracteres no válidos), el motor de validación de GitHub Actions detectará la inconsistencia durante la fase de *parsing* antes de asignar un runner. El pipeline no llegará a ejecutar ningún comando y se marcará inmediatamente como **Failed / Invalid Workflow**, indicando en la interfaz web la línea y columna exactas donde se originó el error.

---

## 6. Conclusiones

- Se implementó exitosamente el concepto de **Pipeline as Code**, manteniendo la definición del ciclo de integración dentro del control de versiones.
- Se comprendió el ciclo de vida de los runners efímeros y la trazabilidad que ofrecen los registros (logs) ante eventos del repositorio.
- Este pipeline base servirá de plataforma para integrar progresivamente etapas de compilación, análisis estático de código, testing automatizado, seguridad y despliegue continuo.
