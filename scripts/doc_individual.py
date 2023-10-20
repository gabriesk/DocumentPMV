from docxtpl import DocxTemplate
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

doc = DocxTemplate("template/termo-recebimento.docx")

def createDocument(nome_rem = None, mat_rem = None, setor_rem = None,
                           nome_des = None, mat_des = None, setor_des = None,
                           tipo = None, data = None, motivo = None, 
                           itens = None):
    
    tipo_def, tipo_emp = (" ", " ")    
    
    if tipo == "Definitiva":
        tipo_def = " X "
        devolucao = ""
    elif tipo == "Emprestimo":
        tipo_emp = " X "
        devolucao = data.strftime('%d/%m/%Y')
    
    data_hoje = datetime.today().strftime('%d/%m/%Y')
    data_extenso = datetime.today().strftime('%d de %B de %Y')
    
    
    context = {
        'nome_rem' : nome_rem,
        'mat_rem' : mat_rem,
        'setor_rem' : setor_rem,
        'nome_des' : nome_des,
        'mat_des' : mat_des,
        'setor_des' : setor_des,
        'motivo_transferencia' : motivo,
        'tipo_def' : tipo_def,
        'tipo_emp' : tipo_emp,
        'prazo' : devolucao,
        'table' : [],
        'data' : data_hoje,
        'data_extenso' : data_extenso,
            }

    if len(itens) < 14:
            for _ in range(14 - len(itens)): itens.append(['', '', ''])

    for l in itens: 
            context['table'].append({'plaq' : l[0],
                                     'desc' : l[1],
                                     'qtd' : l[2]})

    doc.render(context)

    #doc.save("{}_{}.docx".format(nome_des, "-".join(setor_des.split('/'))))
    
    return (doc, ("{}_{}.docx".format(nome_des, "-".join(setor_des.split('/')))))