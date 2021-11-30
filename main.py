from fpdf import FPDF
def crear_pdf(nombre_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_author("Powered By Daniel Marín")
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(0 ,0,0)
    pdf.image("images.jpg",10,10,20,15)
    pdf.cell(0, 15, 'Reporte de venta\n',0,1,"C")
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0,10,"",0)
    pdf.multi_cell(35,10,"Fecha",1,"C")
    pdf.cell(10,6,"Dia",1)
    pdf.cell(10,6,"Mes",1)
    pdf.cell(15,6,"Año",1)
    pdf.cell(120,6,"Requerimiento de material",0,0,"C")
    pdf.multi_cell(0,6,"Folio",1,"C")
    pdf.cell(10,6,"30",1)
    pdf.cell(10,6,"11",1)
    pdf.cell(15,6,"2021",1)
    pdf.cell(35,10,"",0)
    pdf.cell(50,6,"PARTIDA: 21101",1)
    pdf.cell(35,10,"",0)
    pdf.multi_cell(0,6,"#Folio",1,"C")
    pdf.multi_cell(0,4,"",0)
    pdf.set_fill_color(130, 129, 129)
    pdf.cell(0,5,"UNIDAD ADMINISTRATIVA",1,1,"C",1)
    pdf.cell(0,8,"COORDINACIÓN DE MODERNIZACIÓN ADMINISTRATIVA E INNOVACIÓN GUBERNAMENTAL",1,1,"C")
    pdf.set_fill_color(130, 129, 129)
    pdf.cell(0,5,"AREA ASIGNADA",1,1,"C",1)
    pdf.cell(0,8,"SUPERVISIÓN DE CALIDAD Y EVALUACIÓN",1,1,"C",0)
    pdf.cell(30,8,"LOTE",1)
    pdf.cell(30,8,"CANTIDAD",1)
    pdf.cell(30,8,"UNIDAD",1)
    pdf.multi_cell(0,8,"DESCRIPCIÓN",1)
    #BODY
    #25 registros
    for i in range(25):
        pdf.cell(30,6,"#",1)
        pdf.cell(30,6,"#",1)
        pdf.cell(30,6,"#",1)
        pdf.multi_cell(0,6,"#",1)
    #ENDBODY
    pdf.rect(10,61.1,190.0,184,"D")
    pdf.set_xy(10,250)
    pdf.cell(48,5,"AUTORIZÓ",0,0,"C")
    pdf.cell(65,5,"",0)
    pdf.multi_cell(0,5,"SOLICITÓ",0,"C")
    pdf.multi_cell(0,3,"",0,"C")
    pdf.multi_cell(0,3,"",0,"C")
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(57,5,"SILVIA ELENA FLORES BANDA",0,0,"C")
    pdf.set_font('Arial', '', 11)
    pdf.cell(55,5,"",0)
    pdf.set_font('Arial', 'B', 11)
    pdf.multi_cell(0,5,"TERESA DE JESUS LOPEZ HERNANDEZ",0,0,"C")
    pdf.set_font('Arial', '', 11)
    pdf.cell(64,5,"SUBDIRECTORA DE SUPERVISIÓN",0,0,"C")
    pdf.cell(69,5,"",0)
    pdf.multi_cell(0,5,"ADMINISTRADOR",0,0,"C")
    pdf.cell(52,5,"DE CALIDAD Y EVALUACIÓN",0,0,"C")
    pdf.output(nombre_pdf+'.pdf', 'F')
crear_pdf("reporte")
# Powered By DanielMarín