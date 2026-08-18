# Proyecto CI/CD - Laboratorios de Integración y Entrega Continua

Repositorio central para el desarrollo y automatización de pipelines de Integración Continua y Entrega Continua (CI/CD) utilizando **GitHub Actions**.

## 🚀 Estrategia de Branching y Flujo de Trabajo

Este proyecto implementa una estrategia de branching basada en **ramas de funcionalidad (Feature Branching)** y control de cambios mediante **Pull Requests** protegidos con **Quality Gates**:

1. `main`: Rama protegida que contiene la versión estable y validada.
2. `feature/*`: Ramas independientes creadas para cada funcionalidad o modificación.
3. **Pull Requests (PR)**: Mecanismo obligatorio para integrar cambios a `main`. Requiere validación exitosa del pipeline de CI (Compilación, Pruebas Unitarias y Cobertura) antes de permitir el merge.

```text
Developer ──► Feature Branch ──► Commit & Push ──► CI Pipeline (Build + Tests + Cobertura) ──► Pull Request ──► Code Review & Quality Gate ──► Merge ──► main
```

---

## 🧪 Pruebas Automatizadas y Quality Gate (Laboratorio 3)

El pipeline incorpora una etapa de validación exhaustiva mediante pruebas unitarias automatizadas con **pytest** y análisis de cobertura de código con **pytest-cov**.

### Ejecución de Pruebas en Entorno Local:

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar suite de pruebas unitarias y cobertura:**
   ```bash
   pytest --junitxml=reports/junit/test-results.xml \
          --cov=app \
          --cov-report=term-missing \
          --cov-report=html:reports/coverage-html \
          --cov-report=xml:reports/coverage.xml
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python -m app.main
   ```

---

## 📁 Estructura del Proyecto

```text
.
├── .github/
│   └── workflows/
│       └── pipeline.yml       # Flujo de trabajo automatizado de CI (Build, Test, Quality Gate)
├── app/
│   ├── __init__.py
│   ├── calculator.py          # Módulo de funciones matemáticas y lógica de negocio
│   ├── string_utils.py        # Módulo de utilidades de texto y validaciones
│   ├── main.py                # Punto de entrada de la aplicación
│   └── hello.txt              # Archivo de la aplicación base
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py     # Pruebas unitarias para calculadora
│   ├── test_string_utils.py   # Pruebas unitarias para validaciones y cadenas
│   └── test_main.py           # Pruebas unitarias para el punto de entrada
├── .gitignore                 # Archivos y directorios ignorados por Git
├── pytest.ini                 # Configuración de pruebas con pytest
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

---

## ⚙️ Pipeline CI as Code

El pipeline se ejecuta automáticamente ante eventos de:
- `push` en la rama `main` y en cualquier rama `feature/**`.
- `pull_request` con destino a la rama `main`.

### Etapas del Pipeline:
1. **Compilación y Build (`build`):** Configura el runtime de Python 3.12, instala dependencias y compila el bytecode verificando la integridad del proyecto.
2. **Pruebas Unitarias y Cobertura (`test`):** Depende del build (`needs: build`), ejecuta las pruebas con `pytest`, genera reportes JUnit XML y Cobertura HTML/XML, y los publica como **Artefactos** descargables de GitHub Actions.
3. **Quality Gate y Certificación (`quality-gate`):** Valida que todas las etapas previas hayan finalizado con éxito antes de certificar la integración.
