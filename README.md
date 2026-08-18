# Proyecto CI/CD - Laboratorios de Integración y Entrega Continua

Repositorio central para el desarrollo y automatización de pipelines de Integración Continua y Entrega Continua (CI/CD) utilizando **GitHub Actions**.

## 🚀 Estrategia de Branching y Flujo de Trabajo

Este proyecto implementa una estrategia de branching basada en **ramas de funcionalidad (Feature Branching)** y control de cambios mediante **Pull Requests** protegidos:

1. `main`: Rama protegida que contiene la versión estable y validada.
2. `feature/*`: Ramas independientes creadas para cada funcionalidad o modificación.
3. **Pull Requests (PR)**: Mecanismo obligatorio para integrar cambios a `main`. Requiere validación exitosa de CI antes de permitir el merge.

```text
Developer ──► Feature Branch ──► Commit & Push ──► CI Pipeline (Automático) ──► Pull Request ──► Code Review ──► Merge ──► main
```

## 📁 Estructura del Proyecto

```text
.
├── .github/
│   └── workflows/
│       └── pipeline.yml       # Flujo de trabajo automatizado de CI
├── app/
│   └── hello.txt              # Archivo de la aplicación base
└── README.md                  # Documentación del proyecto
```

## ⚙️ Pipeline CI as Code

El pipeline se ejecuta automáticamente ante eventos de:
- `push` en la rama `main` y en cualquier rama `feature/*`.
- `pull_request` con destino a la rama `main`.
