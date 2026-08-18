"""
Script para generar Informe_Laboratorio_3_Pruebas_Automatizadas_Quality_Gate.docx
"""
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_color):
    """Establece color de fondo a una celda."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Establece márgenes internos a una celda."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    """Agrega un bloque de código con fondo gris y fuente monoespaciada."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F3F4F6")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    # Borde sutil
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                        f'<w:left w:val="single" w:sz="12" w:space="0" w:color="3B82F6"/>'
                        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
                        f'</w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph() # Espacio después

def add_screenshot_box(doc, title, url, description, placeholder_text):
    """Agrega un recuadro estilizado para capturas de pantalla."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="94A3B8"/>'
                        f'<w:left w:val="single" w:sz="16" w:space="0" w:color="0284C7"/>'
                        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="94A3B8"/>'
                        f'<w:right w:val="single" w:sz="6" w:space="0" w:color="94A3B8"/>'
                        f'</w:tcBorders>')
    tcPr.append(borders)
    
    p0 = cell.paragraphs[0]
    p0.paragraph_format.space_before = Pt(2)
    p0.paragraph_format.space_after = Pt(2)
    r0 = p0.add_run(f"📸 {title}\n")
    r0.bold = True
    r0.font.name = 'Calibri'
    r0.font.size = Pt(10.5)
    r0.font.color.rgb = RGBColor(15, 23, 42)
    
    if url:
        r_url = p0.add_run(f"🔗 Enlace directo: {url}\n")
        r_url.font.name = 'Calibri'
        r_url.font.size = Pt(9)
        r_url.font.color.rgb = RGBColor(2, 132, 199)
        r_url.font.underline = True
        
    r_desc = p0.add_run(f"📝 Descripción: {description}\n\n")
    r_desc.font.name = 'Calibri'
    r_desc.font.size = Pt(9.5)
    r_desc.font.italic = True
    r_desc.font.color.rgb = RGBColor(71, 85, 105)
    
    p1 = cell.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(8)
    p1.paragraph_format.space_after = Pt(8)
    r_box = p1.add_run(f"┌─────────────────────────────────────────────────────────────┐\n"
                       f"│                                                             │\n"
                       f"│               [ {placeholder_text} ]               │\n"
                       f"│                                                             │\n"
                       f"└─────────────────────────────────────────────────────────────┘")
    r_box.font.name = 'Consolas'
    r_box.font.size = Pt(8.5)
    r_box.font.color.rgb = RGBColor(100, 116, 139)
    doc.add_paragraph()

def build_docx(filepath):
    doc = docx.Document()
    
    # Configurar márgenes normales (1 pulgada = 72 pt)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    # --- ENCABEZADO Y TÍTULO ---
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(2)
    r_inst = p_meta.add_run("UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO\nFACULTAD DE INGENIERÍA EN CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES\n")
    r_inst.bold = True
    r_inst.font.name = 'Calibri'
    r_inst.font.size = Pt(9.5)
    r_inst.font.color.rgb = RGBColor(100, 116, 139)
    
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("Informe de Laboratorio 3\n")
    r_title.bold = True
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(22)
    r_title.font.color.rgb = RGBColor(30, 58, 138) # Navy Blue
    
    r_sub = p_title.add_run("Integración de Pruebas Automatizadas y Quality Gates en CI/CD")
    r_sub.bold = True
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(14)
    r_sub.font.color.rgb = RGBColor(14, 116, 144)
    
    # Tabla de Metadatos
    tbl_meta = doc.add_table(rows=6, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Módulo:", "Entornos de Integración y Entrega Continua (CI/CD)"),
        ("Estudiante:", "René Velásquez"),
        ("Correo Institucional:", "velasquez.rene@ficct.uagrm.edu.bo"),
        ("Fecha:", "18 de Agosto de 2026"),
        ("Plataforma CI/CD:", "GitHub Actions (Ubuntu Latest / Python 3.12)"),
        ("Repositorio GitHub:", "https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua")
    ]
    for idx, (label, val) in enumerate(meta_data):
        row = tbl_meta.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(1.8)
        c1.width = Inches(4.9)
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "F8FAFC")
        set_cell_margins(c0, top=40, bottom=40, left=60, right=60)
        set_cell_margins(c1, top=40, bottom=40, left=60, right=60)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.name = 'Calibri'
        r0.font.size = Pt(9)
        r0.font.color.rgb = RGBColor(51, 65, 85)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(val)
        r1.font.name = 'Calibri'
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor(15, 23, 42)
        if "http" in val:
            r1.font.color.rgb = RGBColor(2, 132, 199)
            r1.font.underline = True
            
    doc.add_paragraph() # Espacio
    
    # --- SECCIÓN 1: INTRODUCCIÓN Y OBJETIVOS ---
    h1 = doc.add_heading("1. Introducción y Objetivos", level=1)
    h1.style.font.color.rgb = RGBColor(30, 58, 138)
    
    p = doc.add_paragraph(
        "En esta práctica se amplió el pipeline construido en los laboratorios anteriores para incorporar "
        "una etapa de validación rigurosa mediante pruebas unitarias automatizadas y análisis dinámico de cobertura de código. "
        "El objetivo principal es implementar el concepto de Quality Gate (Barrera de Calidad), asegurando que únicamente el código "
        "que cumple satisfactoriamente tanto con la compilación como con el 100% de las pruebas unitarias avance en el ciclo de integración continua."
    )
    p.paragraph_format.line_spacing = 1.15
    
    doc.add_heading("Objetivos Alcanzados", level=2)
    bullets = [
        "Desarrollo de módulos funcionales en Python (app/calculator.py, app/string_utils.py, app/main.py) y su suite de pruebas exhaustivas con pytest.",
        "Alcanzar el 100% de cobertura de código (Statement & Branch Coverage) medido con pytest-cov.",
        "Configuración de etapas modulares y dependencias en GitHub Actions (needs: build y needs: [build, test]).",
        "Generación y publicación de Artefactos de CI descargables (Reporte JUnit XML y Cobertura HTML interactiva).",
        "Implementación efectiva de un Quality Gate que bloquea automáticamente la ejecución del pipeline y el Pull Request ante fallos de pruebas.",
        "Simulación de un fallo deliberado y recuperación exitosa mediante commits sobre la rama de funcionalidad feature/add-automated-tests."
    ]
    for b in bullets:
        bp = doc.add_paragraph(b, style='List Bullet')
        bp.paragraph_format.space_after = Pt(3)
        bp.paragraph_format.line_spacing = 1.1
        
    doc.add_paragraph()
    
    # --- SECCIÓN 2: ARQUITECTURA DEL QUALITY GATE ---
    doc.add_heading("2. Arquitectura del Pipeline y Quality Gate", level=1)
    p_arch = doc.add_paragraph(
        "El pipeline de CI/CD se estructuró en 3 etapas secuenciales fuertemente desacopladas. "
        "Si la etapa de compilación o la etapa de pruebas falla, el Quality Gate interrumpe el flujo impidiendo cualquier avance:"
    )
    p_arch.paragraph_format.line_spacing = 1.15
    
    add_code_block(doc, 
"""+-----------------------------------------------------------------------------------+
|                            FLUJO DEL PIPELINE Y QUALITY GATE                      |
+-----------------------------------------------------------------------------------+
  Desarrollador (Local) ──► git push / PR (feature/add-automated-tests)
         │
         ▼
  [Etapa 1: Compilación & Build]
  - Configuración de Python 3.12 y caché de dependencias pip
  - Bytecode Compilation (python -m compileall app tests)
  - Validación de integridad estructural [OK]
         │ (needs: build)
         ▼
  [Etapa 2: Pruebas Unitarias y Cobertura]
  - Ejecución de 24 tests unitarios con pytest
  - Análisis de cobertura con pytest-cov (100% alcanzado)
  - Publicación de Artefactos: JUnit XML y Cobertura HTML
  - Publicación de resumen en GitHub Step Summary
         │
  ¿Superó 100% de las pruebas?
   ├── NO (❌) ──► PIPELINE BLOQUEADO (Quality Gate rechaza el Pull Request)
   └── SÍ (✓)
         │ (needs: [build, test])
         ▼
  [Etapa 3: Quality Gate y Certificación]
  - Certificación formal de calidad
  - Estado verde (✓) habilitado para Merge hacia main""")

    # --- SECCIÓN 3: PIPELINE AS CODE ---
    doc.add_heading("3. Pipeline as Code (.github/workflows/pipeline.yml)", level=1)
    doc.add_paragraph("A continuación se presenta la definición declarativa completa del pipeline en GitHub Actions:")
    
    pipeline_path = ".github/workflows/pipeline.yml"
    with open(pipeline_path, "r", encoding="utf-8") as f:
        pipeline_code = f.read()
    add_code_block(doc, pipeline_code)
    
    # --- SECCIÓN 4: EVIDENCIAS DE EJECUCIÓN ---
    doc.add_heading("4. Evidencias de Ejecución (Capturas de Pantalla)", level=1)
    doc.add_paragraph("A continuación se detallan los enlaces de verificación y los recuadros para la inclusión de capturas:")
    
    add_screenshot_box(
        doc,
        "Captura 1: Ejecución Exitosa del Pipeline (Todas las Etapas Aprobadas)",
        "https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192844793",
        "Muestra las 3 etapas completadas exitosamente (Build, Test, Quality Gate) con checks en verde y artefactos adjuntos.",
        "PEGAR AQUÍ CAPTURA 1 - PIPELINE EXITOSO ✓"
    )
    
    add_screenshot_box(
        doc,
        "Captura 2: Ejecución Fallida del Pipeline por Error en Pruebas (Quality Gate)",
        "https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192717602",
        "Muestra el fallo provocado deliberadamente en la función add(). La etapa de Tests falla (❌) y el Quality Gate se omite (🚫).",
        "PEGAR AQUÍ CAPTURA 2 - PIPELINE FALLIDO ❌"
    )
    
    add_screenshot_box(
        doc,
        "Captura 3: Bloqueo del Pull Request por Fallo de Status Checks",
        "https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/pull/2",
        "Muestra el Pull Request #2 con el check de pruebas en rojo y el bloqueo de integración a la rama main.",
        "PEGAR AQUÍ CAPTURA 3 - PULL REQUEST BLOQUEADO"
    )
    
    add_screenshot_box(
        doc,
        "Captura 4: Publicación y Descarga de Artefactos de Pruebas y Cobertura",
        "https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua/actions/runs/32192844793#artifacts",
        "Muestra los artefactos 'code-coverage-report' y 'test-results-junit' listos para descarga en GitHub Actions.",
        "PEGAR AQUÍ CAPTURA 4 - ARTEFACTOS DEL PIPELINE"
    )
    
    add_screenshot_box(
        doc,
        "Captura 5: Reporte Interactivo de Cobertura de Código (HTML)",
        "https://github.com/velasquezren/Laboratorio-1-Primer-Pipeline-de-Integraci-n-Continua",
        "Muestra la visualización del reporte HTML de pytest-cov con 100% de cobertura en calculator.py, string_utils.py y main.py.",
        "PEGAR AQUÍ CAPTURA 5 - REPORTE HTML DE COBERTURA 100%"
    )
    
    # --- SECCIÓN 5: RESPUESTAS A PREGUNTAS DE ANÁLISIS ---
    doc.add_heading("5. Respuestas a las Preguntas de Análisis (Parte 5)", level=1)
    
    qa_list = [
        ("1. ¿Por qué las pruebas automatizadas son un componente esencial de la Integración Continua?",
         "Las pruebas automatizadas constituyen la piedra angular de la Integración Continua (CI) porque transforman la integración de código desde un simple ejercicio de mezcla de archivos en un mecanismo objetivo y determinístico de garantía de calidad.\n\n"
         "Principales razones técnicas:\n"
         "• Retroalimentación Rápida (Fast Feedback): Los desarrolladores conocen el impacto de sus modificaciones minutos después de realizar un commit, reduciendo drásticamente el tiempo de depuración.\n"
         "• Detección Temprana de Defectos (Shift-Left Testing): Resolver un bug en la fase de desarrollo cuesta hasta 10 veces menos que resolverlo en etapas avanzadas o en producción.\n"
         "• Reproducibilidad y Neutralidad: Las pruebas se ejecutan en runners limpios y estandarizados, eliminando el clásico problema de 'en mi máquina funciona'.\n"
         "• Confianza en la Refactorización: Permiten mejorar el diseño del código con la seguridad de que no se introducirán regresiones."),
        
        ("2. ¿Qué diferencia existe entre una compilación exitosa y una validación exitosa?",
         "La diferencia radica en la profundidad y el objetivo de la verificación realizada sobre el software:\n\n"
         "• Compilación Exitosa (Build): Verifica únicamente la corrección sintáctica y estructural del código fuente. Asegura que no existan errores de sintaxis, que las dependencias se resuelvan y que el intérprete o compilador pueda generar bytecode o ejecutables.\n"
         "• Validación Exitosa (Testing / Verification): Evalúa la corrección semántica, el comportamiento funcional y la lógica de negocio frente a casos de prueba previstos y escenarios límite.\n\n"
         "Ejemplo evidente del laboratorio: La función add(a, b) modificada para retornar 'a + b + 999' compila y se procesa perfectamente sin errores de sintaxis (Compilación Exitosa), pero falla catastróficamente al ejecutarse frente a los tests unitarios (Validación Fallida)."),
         
        ("3. ¿Qué ventajas aporta ejecutar las pruebas automáticamente después de cada cambio?",
         "Ejecutar pruebas automáticamente tras cada cambio aporta ventajas clave:\n\n"
         "• Aislamiento Inmediato de la Causa Raíz: Al dispararse con cada push granular, si ocurre una falla se identifica de inmediato qué commit específico y qué líneas introdujeron el defecto.\n"
         "• Prevención de Regresiones: Garantiza que la adición de una nueva funcionalidad no dañe componentes preexistentes.\n"
         "• Aceleración del Time-to-Market: Suprime la necesidad de extensos periodos manuales de 'congelamiento de código' previos al despliegue.\n"
         "• Documentación Viva: La suite de pruebas actúa como especificación funcional ejecutable que documenta cómo debe responder cada módulo ante diversas entradas."),
         
        ("4. ¿Qué información proporciona el reporte de cobertura de código?",
         "El reporte de cobertura (Code Coverage) es una métrica de análisis dinámico que detalla con exactitud qué partes del código fueron ejecutadas durante la corrida de pruebas:\n\n"
         "• Cobertura de Sentencias (Statement Coverage): Porcentaje y líneas específicas que fueron ejecutadas versus líneas omitidas.\n"
         "• Cobertura de Ramas (Branch Coverage): Determina si todas las rutas de decisión lógica (if/else, try/except) fueron recorridas.\n"
         "• Identificación de Puntos Ciegos y Zonas de Riesgo: Revela funciones, excepciones o validaciones que carecen de pruebas y podrían ocultar fallos graves.\n\n"
         "Nota: Una cobertura del 100% (alcanzada en esta práctica) asegura que cada línea fue evaluada, sirviendo como una sólida red de seguridad ante regresiones."),
         
        ("5. ¿Qué ocurriría si un pipeline permitiera continuar el proceso a pesar de que las pruebas fallen?",
         "Permitir que el pipeline continúe tras un fallo de pruebas anula el propósito de CI/CD y desactiva el Quality Gate:\n\n"
         "• Fuga de Defectos a Producción (Bug Slippage): Código inestable o defectuoso llegaría a ambientes de producción, causando caídas de servicio e insatisfacción de usuarios.\n"
         "• Falsa Sensación de Seguridad: El equipo asumiría erróneamente que el sistema funciona correctamente al ver que el proceso finaliza.\n"
         "• Efecto Cascada / Deuda Técnica: Otros miembros del equipo construirían nuevas funciones sobre una base defectuosa, volviendo la depuración exponencialmente más costosa.\n"
         "• Degradación de la Cultura de Calidad: Los desarrolladores aprenderían a ignorar las alertas de CI, restando valor a la automatización."),
         
        ("6. ¿Qué otros tipos de pruebas podrían incorporarse en las siguientes etapas del pipeline?",
         "En un pipeline de CI/CD maduro (siguiendo la Pirámide de Pruebas de Software), deben integrarse progresivamente:\n\n"
         "• Pruebas de Integración: Evalúan la comunicación entre módulos, bases de datos y APIs externas.\n"
         "• Análisis Estático de Seguridad y Código (SAST & Linters): Herramientas como SonarQube, Bandit o Flake8 para detectar vulnerabilidades y deuda técnica.\n"
         "• Pruebas de Extremo a Extremo (E2E): Con Playwright, Cypress o Selenium para simular flujos de usuario reales en la interfaz gráfica.\n"
         "• Pruebas de Contrato (Contract Testing): Con herramientas como Pact para garantizar interoperabilidad entre microservicios.\n"
         "• Pruebas de Rendimiento y Estrés: Con k6, Locust o JMeter para medir tiempos de respuesta y límites de carga.\n"
         "• Smoke Tests Post-Despliegue: Verificaciones básicas no destructivas ejecutadas inmediatamente tras desplegar en Staging o Producción.")
    ]
    
    for q_title, q_ans in qa_list:
        doc.add_heading(q_title, level=2)
        p_ans = doc.add_paragraph(q_ans)
        p_ans.paragraph_format.line_spacing = 1.15
        p_ans.paragraph_format.space_after = Pt(6)
        
    doc.add_paragraph()
    
    # --- SECCIÓN 6: CONCLUSIONES ---
    doc.add_heading("6. Conclusiones", level=1)
    conclusions = [
        "La integración de pruebas unitarias automatizadas con pytest y reportes de cobertura conforma el primer Quality Gate indispensable en cualquier pipeline profesional de CI/CD.",
        "La arquitectura modular con jobs interdependientes (build ➔ test ➔ quality-gate) garantiza que los recursos de cómputo solo se utilicen cuando las fases precedentes han sido validadas exitosamente.",
        "La publicación de Artefactos (JUnit XML y Cobertura HTML) dota al equipo de desarrollo de trazabilidad histórica, auditoría y visibilidad continua sobre la calidad del software.",
        "El flujo de trabajo basado en Feature Branches, Pull Requests protegidos y validación automática de CI elimina el factor de error humano en la incorporación de cambios a la rama principal."
    ]
    for c in conclusions:
        cp = doc.add_paragraph(c, style='List Bullet')
        cp.paragraph_format.space_after = Pt(3)
        cp.paragraph_format.line_spacing = 1.1
        
    # Guardar documento
    doc.save(filepath)
    print(f"Documento guardado exitosamente en: {filepath}")

if __name__ == "__main__":
    build_docx("Informe_Laboratorio_3_Pruebas_Automatizadas_Quality_Gate.docx")
