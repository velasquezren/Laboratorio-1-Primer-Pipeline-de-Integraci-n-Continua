# Laboratorio 1
# Primer Pipeline de Integración Continua

## Objetivos

Al finalizar este laboratorio el estudiante será capaz de:

- Comprender la estructura básica de un pipeline de CI/CD.
- Configurar un repositorio para ejecutar un pipeline automático.
- Crear un primer pipeline utilizando Pipeline as Code.
- Ejecutar un pipeline después de realizar un commit.
- Analizar el resultado de la ejecución y los registros generados.

---

# Descripción

En este laboratorio se construirá el primer pipeline del módulo. Aunque su funcionalidad será sencilla, servirá como base para todos los laboratorios posteriores. El objetivo no es automatizar una aplicación completa, sino comprender el flujo de ejecución de un pipeline moderno.

El laboratorio podrá realizarse utilizando **GitHub Actions** o **GitLab CI/CD**, según la plataforma seleccionada por cada estudiante.

---

# Requisitos

- Cuenta en GitHub o GitLab.
- Git instalado.
- Visual Studio Code (o editor equivalente).
- Conocimientos básicos de Git.
- Acceso a Internet.

---

# Parte 1. Crear el repositorio

1. Crear un nuevo repositorio llamado:

```

ci-cd-labs

```

2. Clonar el repositorio localmente.

3. Crear la siguiente estructura:

```

ci-cd-labs/
│
├── README.md
└── app/
└── hello.txt

```

El archivo **hello.txt** puede contener cualquier texto.

---

# Parte 2. Crear el pipeline

Crear el archivo correspondiente según la plataforma utilizada.

## GitHub Actions

```

.github/workflows/pipeline.yml

```

## GitLab

```

.gitlab-ci.yml

```

El pipeline deberá:

- ejecutarse automáticamente después de cada Push;
- mostrar un mensaje de bienvenida;
- mostrar la fecha y hora de ejecución;
- mostrar la versión de Git instalada;
- finalizar correctamente.

No es necesario agregar procesos de compilación todavía.

---

# Parte 3. Ejecutar el pipeline

Realizar un commit.

Enviar los cambios al repositorio remoto.

Verificar que el pipeline se ejecute automáticamente.

---

# Parte 4. Analizar la ejecución

Responder las siguientes preguntas:

1. ¿Qué evento inició el pipeline?

2. ¿Cuánto tiempo tardó en ejecutarse?

3. ¿En qué sistema operativo se ejecutó?

4. ¿Qué runner ejecutó el pipeline?

5. ¿Qué información muestran los logs?

6. ¿Qué ocurriría si el archivo YAML contiene un error de sintaxis?

---

# Entregables

Cada estudiante deberá entregar:

- URL del repositorio.
- Captura del pipeline ejecutado correctamente.
- Captura de los logs.
- Archivo YAML utilizado.
- Documento PDF respondiendo las preguntas de análisis.

---

# Criterios de evaluación

| Criterio | Puntos |
|----------|-------:|
| Repositorio correctamente creado | 20 |
| Pipeline ejecuta correctamente | 30 |
| Archivo YAML correctamente estructurado | 20 |
| Evidencias de ejecución | 20 |
| Respuestas al análisis | 10 |

Total: **100 puntos**

---

# Resultado esperado

Al finalizar este laboratorio el estudiante dispondrá de un repositorio completamente funcional sobre el cual se irán incorporando nuevas etapas del pipeline durante el resto del módulo.