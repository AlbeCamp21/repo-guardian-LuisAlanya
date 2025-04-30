##### **2. Plantilla para PullRequests (`PULL_REQUEST_TEMPLATE.md`)**  
**Ubicación**: `.github/PULL_REQUEST_TEMPLATE.md`  
**Contenido**:  
```markdown
---
name: "Pull Request"
about: Proponer cambios al código
title: "[TIPO] RX-XX: Descripción breve"
labels: ""
assignees: ""

---

### **Descripción**  
[Explica los cambios y su motivación. Ej: "Añade soporte para packfiles en object_scanner.py".]  

### **Checklist**  
- [ ] Código probado localmente.  
- [ ] Tests pasan (`pytest -n auto --cov=guardian`).  
- [ ] Cobertura ≥80% (adjuntar reporte).  
- [ ] Documentación actualizada (README/docs).  
- [ ] Captura de pantalla (si aplica a cambios en CLI/TUI).  

### **Issue Relacionado**  
Closes #<NÚMERO>  
