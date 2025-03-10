# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 16:06:11 2025

@author: Josué Hernández Torres
"""
import tkinter as tk
from tkinter import messagebox, filedialog

def generar_latex():
    titulo = entry_titulo.get()
    alumno = entry_alumno.get()
    especialidad = entry_especialidad.get()
    fecha = entry_fecha.get()
    asesor1 = entry_asesor1.get()
    asesor2 = entry_asesor2.get()
    asesor3 = entry_asesor3.get()
    
    # Construcción dinámica de los asesores
    asesores_text = ""
    if asesor1:
        asesores_text += f"\\Large \\textbf{{{asesor1}}}\\\\[0.5cm]\n"
    if asesor2:
        asesores_text += f"\\Large \\textbf{{{asesor2}}}\\\\[0.5cm]\n"
    if asesor3:
        asesores_text += f"\\Large \\textbf{{{asesor3}}}\\\\[0.5cm]\n"
    
    contenido_latex = rf"""
\documentclass[a4paper]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage{{xcolor, graphicx, geometry}}
\usepackage{{tikz}}

% Definir márgenes personalizados
\geometry{{top=2cm, bottom=2cm, left=3cm, right=2cm}}
% Definiendo el azul del INAOE
\definecolor{{AzulINAOE}}{{HTML}}{{46549F}}

\begin{{document}}

% Definir página completa
\thispagestyle{{empty}}
\begin{{tikzpicture}}[remember picture, overlay]
    
    % Imagen de la franja azul lateral
    \node[anchor=north west] at (-2.5cm, 1.85cm) {{\includegraphics[height=28cm]{{Franja_Azul.png}}}};
    
    % Contenedor central ajustable
    \draw[draw=AzulINAOE, thick] (1.5cm, 1.65cm) rectangle (15.5cm, -26.15cm);

    % Contenido dentro del cuadro central
    \node[align=center] at (8.5cm, -9cm) {{\parbox{{12cm}}{{%
        \centering
        %Título
        \LARGE \textbf{{{titulo}}}\\\\[1cm]
        \Large por\\\\[0.5cm]
        %Nombre del alumno
        \Large\textbf{{{alumno}}}\\\\[1cm]
        \Large Tesis sometida como requisito parcial para la obtención del grado de\\\\[0.5cm]
        %Especialidad
        \Large \textbf{{{especialidad}}}\\\\[1cm]
        \Large en el\\\\[0.5cm]
        \Large \textbf{{Instituto Nacional de Astrofísica, Óptica y Electrónica}}\\\\[1cm]
        %Fecha
        \Large {fecha}\\\\[0.5cm]
        \Large Tonantzintla, Puebla\\\\[1cm]
        \Large Supervisada por: \\\\[0.5cm]
        {asesores_text}
    }}}};

    % Texto inferior con derechos de autor
    \node[align=center] at (8.5cm, -24.5cm) {{\parbox{{10cm}}{{%
        \centering
        \textcopyright\ INAOE 2025 \\\\
        Derechos Reservados \\\\
        El autor otorga al INAOE el permiso de reproducir y \\\\
        distribuir copias de esta tesis en su totalidad o en partes \\\\
        mencionando la fuente.
    }}}};
    
    % Logo inferior derecho
    \node[anchor=south east] at (16cm, -26.5cm) {{\includegraphics[width=2cm]{{Logo_INAOE.jpg}}}};
\end{{tikzpicture}}

\end{{document}}
"""

    archivo_tex = filedialog.asksaveasfilename(defaultextension=".tex", filetypes=[("LaTeX files", "*.tex")])
    if archivo_tex:
        with open(archivo_tex, "w", encoding="utf-8") as file:
            file.write(contenido_latex)
        messagebox.showinfo("Éxito", f"Archivo LaTeX generado:\n{archivo_tex}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Generador de Portada LaTeX")
root.geometry("450x400")

tk.Label(root, text="Título de la tesis:").pack()
entry_titulo = tk.Entry(root, width=50)
entry_titulo.pack()

tk.Label(root, text="Nombre del alumno:").pack()
entry_alumno = tk.Entry(root, width=50)
entry_alumno.pack()

tk.Label(root, text="Especialidad:").pack()
entry_especialidad = tk.Entry(root, width=50)
entry_especialidad.pack()

tk.Label(root, text="Fecha:").pack()
entry_fecha = tk.Entry(root, width=50)
entry_fecha.pack()

tk.Label(root, text="Asesor 1:").pack()
entry_asesor1 = tk.Entry(root, width=50)
entry_asesor1.pack()

tk.Label(root, text="Asesor 2 (Opcional):").pack()
entry_asesor2 = tk.Entry(root, width=50)
entry_asesor2.pack()

tk.Label(root, text="Asesor 3 (Opcional):").pack()
entry_asesor3 = tk.Entry(root, width=50)
entry_asesor3.pack()

tk.Button(root, text="Generar LaTeX", command=generar_latex).pack(pady=10)

root.mainloop()
