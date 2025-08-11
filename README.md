# 🧠 Simulación de Empatía – Algoritmo Social basado en Teoría de Conjuntos

Este repositorio contiene una **simulación en Python** que reproduce el **escenario de empatía** descrito en el artículo “*Modelo Matemático de Algoritmo Social Basado en Teoría de Conjuntos*”.  
El objetivo es mostrar **didácticamente** cómo dos miembros de una colonia:

1. **Chatean 5 veces** (interacciones visibles en consola).  
2. Detectan **intereses comunes** (`surf`).  
3. Se sugieren mutuamente el interés con **mayor valor moda**.  
4. Al aceptar, incrementan dichos intereses en:
   - Perfiles de usuario.  
   - Colonia.  
   - Perfiles de miembro.

---

## 📺 Vista previa de la consola
```bash
💬 Simulando 5 interacciones entre Ana y Beto...
💬 Ana → Beto: ¡Hola! ¿Conoces algún buen lugar de surf por aquí?
💬 Ana → Beto: Sí, hay una playa escondida a 10 min. ¿Te gustaría ir?
💬 Ana → Beto: ¡Claro! También me encanta la gastronomía después de surfear.
💬 Ana → Beto: Perfecto, conozco un food-truck cerca que tiene tacos increíbles.
💬 Ana → Beto: ¡Genial! Quedamos para surf + tacos este fin de semana.
Intereses comunes detectados: {'surf'}
Ana sugiere a Beto: surf
Beto sugiere a Ana: gastronomia
Ambos aceptan la sugerencia.
```

## 🧩 Modelos simplificados

Usuario: persona con intereses y valores moda.
Colonia: grupo geolocalizado.
Miembro: usuario dentro de una colonia.
Interés: etiqueta con contador (moda).

---

## 📄 Referencia académica

Torres, J., Ramírez, C., Tuesta, V., Mejía, I., & Álvarez, H. (2016).  
*Modelo matemático de algoritmo social basado en teoría de conjuntos para la recolección e identificación de intereses de colonias humanas*.  
Revista Ingeniería: Ciencia, Tecnología e Innovación, 3(2).  
Recuperado de: https://www.researchgate.net/publication/343614971

---

## 🧪 Requisitos

- Python 3.8 o más.
- Sin dependencias externas.

---

## ▶️ Cómo ejecutar

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/empatia-simulacion.git
   cd empatia-simulacion
   python simulacion_empatia.py
   ```
