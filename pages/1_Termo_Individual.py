import streamlit as st
import base64
import styles.headers as h
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval
import scripts.doc_individual as doc
import time
from io import BytesIO

st.set_page_config(
    page_title="Termo de Transferência Individual",
    page_icon="📄"
)

h.header()

def download_file(object, filename):
    
    try:
        b64 = base64.b64encode(object.encode()).decode()
    except AttributeError as e:
        b64 = base64.b64encode(object).decode()
    
    dl_link = f"""
    <html>
    <head>
    <title>Start Auto Download file</title>
    <script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script>
    $('<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64}" download="{filename}">')[0].click()
    </script>
    </head>
    </html>
    """
    
    return dl_link

def download_doc():
    buff = BytesIO()
    form.save(buff)
    components.html(download_file(buff.getvalue(), filename), height=0)


st.header("Movimentação de Equipamentos")
st.subheader("Identificação dos Participantes")

col1, col2 = st.columns(2)
col1.write("Identificação do Remetente")
col2.write("Identificação do Destinatário")

with col1:
    nome_rem = st.text_input("Nome do Remetente")
    mat_rem = st.text_input("Matricula do Remetente")
    setor_rem = st.text_input("Setor/Unidade Administrativa do Remetente")
    
    
    
with col2:
    nome_des = st.text_input("Nome do Destinatário")
    mat_des = st.text_input("Matricula do Destinatario")
    setor_des = st.text_input("Setor/Unidade Administrativa do Destinatário")


st.divider()

st.subheader("Sobre a Transferência")

col1, col2 = st.columns(2)

with col1:
    tipo = st.radio(
        "Tipo de Transferência", ["Definitiva", "Emprestimo"],
        index=0)

with col2:
    if tipo == "Definitiva":
        devolucao =st.date_input("Data de Devolução:",
                                disabled=True,
                                format="DD/MM/YYYY"
                                )
    else:
        devolucao =st.date_input("Data de Devolução:",
                                 disabled=False,
                                 format="DD/MM/YYYY"                              
                                )

motivo = st.text_area("Motivo Detalhado da Transferência:")

st.divider()

st.subheader("Lista de Equipamentos")

col1, col2, col3 = st.columns(3)

with col1:
    computador = st.checkbox("Computador")
    monitor = st.checkbox("Monitor")

with col2:
    mouse = st.checkbox("Mouse")
    teclado = st.checkbox("Teclado")

with col3:
    forca = st.checkbox("Cabos de Força")
    video = st.checkbox("Cabos de Vídeo (VGA/DVI/HDMI/DP/USB-C)")

if computador:
    pat_com = st.text_input("Patrimônio - Computador")
    lst_pat_com = (pat_com, 'Computador', 1)
    
if monitor:
    qtd_monitor = st.radio(
        "Quantidade de Monitores", [1,2,3]
    )
    
    if qtd_monitor >= 1:
        pat_mon1 = st.text_input("Patrimônio - Monitor 1")
        lst_pat_mon1 = (pat_mon1, 'Monitor', 1)
        if  qtd_monitor >= 2:
            pat_mon2 = st.text_input("Patrimônio - Monitor 2")
            lst_pat_mon2 = (pat_mon2, 'Monitor', 1)
            if qtd_monitor >= 3:
                pat_mon3 = st.text_input("Patrimônio - Monitor 3")
                lst_pat_mon3 = (pat_mon3, 'Monitor', 1)
            
if mouse:
    sn_mouse = st.text_input("SN - Mouse")
    lst_sn_mouse = (sn_mouse, 'Mouse', 1)

if teclado:
    sn_teclado = st.text_input("SN - Teclado")
    lst_sn_teclado = (sn_teclado, 'Teclado', 1)

if forca:
    qtd_forca = st.radio(
        "Quantidade de Cabos de Força", [1,2,3,4]
    )
    lst_qtd_forca = ('-', 'Cabos de Força', qtd_forca)

if video:
    qtd_video = st.radio(
        "Quantidade de Cabos de Vídeo", [1,2,3]
    )
    
    opc_video = ["VGA", 
               "DVI",
               "HDMI",
                "DP",
                "USB-C"]
    
    if qtd_video >= 1:
        cabovideo1 = st.radio("Tipo de Cabo 1", opc_video)
        lst_cabovideo1 = ('-', "Cabo de Vídeo " + cabovideo1, 1)
        if qtd_video >= 2:
            cabovideo2 = st.radio("Tipo de Cabo 2", opc_video)
            lst_cabovideo2 = ('-', "Cabo de Vídeo " + cabovideo2, 1)
            if qtd_video >= 3:
                cabovideo3 = st.radio("Tipo de Cabo 3", opc_video)
                lst_cabovideo3 = ('-', "Cabo de Vídeo " + cabovideo3, 1)
                
if True in (computador, monitor, mouse, teclado, forca, video): 
    
    try:
        _, col2, _ = st.columns(3)
        st.divider()
        
        with col2:
            
            if st.button("Confirmar Transferência",):
                
                itens = []

                for var in list(dir()):
                    if var.startswith("lst"):
                        itens.append(globals()[var])
                        
                
                form, filename = doc.createDocument(nome_rem, mat_rem, setor_rem,
                                nome_des, mat_des, setor_des,
                                tipo, devolucao, motivo, itens
                                )
                
                download_doc()
                st.success("Cadastro Realizado!")
                
                with st.spinner(text="Limpando formulário"):
                    time.sleep(4)
                
                
                
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
                
    
    except:
        st.error("O documento se encontra aberto em alguma máquina.")