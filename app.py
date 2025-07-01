import streamlit as st
import time
import random
from PIL import Image
import os

# Configuração da página
st.set_page_config(
    page_title="Quiz do Gestor de Contratos",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para melhorar a aparência
st.markdown("""
<style>
    /* Importar fontes do Google */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Animações */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: #5a5a5a;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out;
    }
    
    /* Container de pergunta */
    .question-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        margin: 1.5rem 0;
        animation: fadeInUp 0.5s ease-out;
    }
    
    .question-container h3 {
        color: #2c3e50;
        font-weight: 600;
        font-size: 1.4rem;
        line-height: 1.5;
        margin: 0;
    }
    
    /* Container de resultado */
    .result-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem auto;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        max-width: 100%;
    }
    
    .result-container h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-weight: 700;
    }
    
    .result-container h2 {
        font-size: 2rem;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        color: white;
    }
    
    .result-container h3 {
        color: white;
        margin-top: 2rem;
        font-size: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    .result-container img {
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        margin: 2rem auto;
        border: 5px solid rgba(255, 255, 255, 0.3);
        max-width: 400px;
    }
    
    /* Texto de carregamento */
    .loading-text {
        text-align: center;
        font-size: 1.6rem;
        font-weight: 600;
        color: #667eea;
        margin: 1.5rem 0;
    }
    
    /* Emoji grande */
    .big-emoji {
        font-size: 4rem;
        margin: 1rem 0;
        display: block;
        text-align: center;
    }
    
    /* Badge de pergunta */
    .question-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        display: inline-block;
        font-weight: 600;
        margin-bottom: 1rem;
        font-size: 0.95rem;
        box-shadow: 0 3px 8px rgba(102, 126, 234, 0.3);
    }
    
    /* Descrição do perfil */
    .profile-description {
        font-size: 1.1rem;
        line-height: 1.7;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        margin-top: 1rem;
    }
    
    .profile-description strong {
        font-size: 1.3rem;
        display: block;
        margin-bottom: 0.8rem;
    }
    
    /* Ajuste dos botões do Streamlit */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Remove customizações que quebram os radio buttons */
    div[data-testid="stRadioButton"] {
        margin-top: 1rem;
    }
    
    div[data-testid="stRadioButton"] label {
        font-size: 1.05rem;
        margin: 0.3rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Dados do quiz
PERGUNTAS = [
    {
        "pergunta": "O contrato acabou de ser publicado. Qual seu primeiro movimento?",
        "opcoes": {
            "A": "Verifico prazos e datas no sistema e já planejo as ações",
            "B": "Envio ofício ao setor requisitante solicitando informações",
            "C": "Ligo pro jurídico perguntando o que pode dar errado",
            "D": "Ajusto minha planilha de controle para gerar alertas automáticos sobre prazos e entregas"
        }
    },
    {
        "pergunta": "Ao assumir a fiscalização de um contrato, quais documentos você analisa primeiro?",
        "opcoes": {
            "A": "Contrato, cronograma e contatos - o essencial para começar",
            "B": "Processo completo: edital, proposta, atas, pareceres e anexos",
            "C": "Procuro a porta de saída, o telefone do advogado e onde assino o seguro de vida",
            "D": "Digitalizo tudo e uso IA para mapear pontos críticos e riscos"
        }
    },
    {
        "pergunta": "Para você, qual a principal diferença entre gestor e fiscal de contrato?",
        "opcoes": {
            "A": "Gestor coordena, fiscal vai a campo e confere se está sendo cumprido",
            "B": "Gestor cuida da parte administrativa e legal, fiscal verifica a execução técnica",
            "C": "Gestor assina e se responsabiliza, fiscal só olha e denuncia se algo der errado",
            "D": "Gestor gerencia dados e processos, fiscal valida entregas via sistema digital"
        }
    },
    {
        "pergunta": "Como você realiza a fiscalização de um contrato?",
        "opcoes": {
            "A": "Vou direto ao local, confiro pessoalmente e resolvo na hora",
            "B": "Sigo rigorosamente o checklist oficial e documento tudo em relatório",
            "C": "Levo testemunhas, máquina fotográfica, gravador e colete à prova de balas",
            "D": "Uso app de vistoria digital com geolocalização e timestamps automáticos"
        }
    },
    {
        "pergunta": "Como fiscal, em caso de erro na execução contratual, você:",
        "opcoes": {
            "A": "Resolvo com o fornecedor e depois documento a solução",
            "B": "Notifico formalmente e sigo o rito processual completo",
            "C": "Comunico imediatamente jurídico, pregoeiro e chefe",
            "D": "Aciono o sistema de gestão de riscos que já previa essa situação"
        }
    },
    {
        "pergunta": "Como a IA pode auxiliar você na gestão dos contratos?",
        "opcoes": {
            "A": "Útil para tarefas básicas, mas prefiro resolver pessoalmente",
            "B": "Só se for homologada e aprovada pelo jurídico",
            "C": "Tenho medo de errar usando isso, prefiro o método tradicional",
            "D": "Automatizo alertas, análises de risco e até gero relatórios com IA"
        }
    },
    {
        "pergunta": "Ao ser designado fiscal de contrato, o que você gostaria de receber da chefia?",
        "opcoes": {
            "A": "Autonomia para agir e resolver problemas rapidamente",
            "B": "Manual detalhado com todos os procedimentos e fluxos",
            "C": "Garantia por escrito de que terei suporte jurídico",
            "D": "Acesso a sistemas modernos e ferramentas de gestão"
        }
    },
    {
        "pergunta": "O contrato exige reajuste anual. O que deve ser feito antes da renovação?",
        "opcoes": {
            "A": "Calculo o reajuste e já acerto com o fornecedor",
            "B": "Verifico cláusula de reajuste e índice definido no contrato",
            "C": "Espero o fornecedor solicitar formalmente para me proteger",
            "D": "Meu sistema já calculou automaticamente com base no índice"
        }
    },
    {
        "pergunta": "Quais cláusulas são essenciais em um contrato administrativo segundo a Lei 14.133/21?",
        "opcoes": {
            "A": "As principais: objeto, preço, prazo e penalidades",
            "B": "Todas as obrigatórias: partes, objeto, preço, prazo, garantias, fiscalização...",
            "C": "As que me protegem: penalidades, rescisão e responsabilidades",
            "D": "As digitalizáveis: SLA, KPIs, métricas de performance e gestão"
        }
    }
]

PERFIS = {
    "A": {
        "nome": "Gestor Executor",
        "emoji": "🎯",
        "imagem": "images/characters/executor_1.jpg",
        "descricao": """
🎯 **Você é o Gestor Executor - O Chuck Norris dos Contratos!**

💪 Enquanto outros gestores ainda estão lendo o edital, você já executou, entregou e está tomando café.

🏃‍♂️ **Características:**
• Resolve problemas antes mesmo deles existirem
• Tem o WhatsApp de todos os fornecedores no favoritos
• Sua assinatura vale mais que carimbo

⚡ **Superpoderes:**
• Telepatia com fornecedores atrasados
• Transforma crise em oportunidade
• Faz reunião de 2 horas em 15 minutos

⚠️ **Kryptonita:** 
Burocracia excessiva e reuniões sem pauta. Quando vê um formulário em 3 vias, começa a suar frio.

🎪 **Bordão:** "Deixa que eu resolvo!" (e realmente resolve)

📌 **Conselho dos anciões:** Às vezes, documentar é tão importante quanto executar. Seu futuro eu agradece!
        """
    },
    "B": {
        "nome": "Gestor Burocrata",
        "emoji": "📋",
        "imagem": "images/characters/burocrata_1.jpg",
        "descricao": """
📋 **Você é o Gestor Burocrata - O Mestre Jedi da Lei 14.133/21!**

📚 Você não apenas lê contratos, você RESPIRA contratos. Conhece cada vírgula, cada inciso e até os considerandos.

🎓 **Características:**
• Cita artigos de lei no churrasco de família
• Tem pesadelos com prazos vencidos
• Organiza até a geladeira por ordem alfabética

🛡️ **Superpoderes:**
• Detecta irregularidades a 10 metros de distância
• Memória fotográfica para números de processo
• Produz pareceres mais rápidos que a luz

⚠️ **Kryptonita:**
Mudanças de última hora e "jeitinho brasileiro". Quando alguém diz "vamos simplificar", você treme.

📐 **Bordão:** "Tem que seguir o rito!" (e o rito tem 47 etapas)

💡 **Sabedoria ancestral:** Nem toda batalha precisa de 15 carimbos. Às vezes, eficiência também é compliance!
        """
    },
    "C": {
        "nome": "Gestor Sobrevivente",
        "emoji": "😰",
        "imagem": "images/characters/sobrevivente_1.jpg",
        "descricao": """
😰 **Você é o Gestor Sobrevivente - O Bear Grylls dos Contratos!**

🏃‍♂️ Sua missão: sobreviver ao contrato sem virar réu. Cada dia sem notificação é uma vitória!

🦺 **Características:**
• Faz backup do backup do backup
• Tem mais prints que o Instagram
• Conhece todos os advogados da cidade

🛡️ **Superpoderes:**
• Sexto sentido para problemas
• Cria trilha de auditoria até para ir ao banheiro
• Transforma paranoia em precaução

⚠️ **Kryptonita:**
Ligação do TCU, e-mail do MP, carta da CGU... basicamente qualquer sigla de 3 letras te apavora.

🏃 **Bordão:** "Não fui eu!" (mesmo quando ninguém perguntou nada)

🌟 **Palavra de esperança:** Coragem! Gestão responsável não é sobre ter medo, é sobre fazer o certo. Você é mais capaz do que imagina!
        """
    },
    "D": {
        "nome": "Gestor Futurista",
        "emoji": "🤖",
        "imagem": "images/characters/futurista_1.webp",
        "descricao": """
🤖 **Você é o Gestor Futurista - O Tony Stark da Administração Pública!**

🚀 Enquanto outros usam Excel, você já está no metaverso dos contratos. Blockchain? Já era, você está em tecnologia quântica!

💻 **Características:**
• Fala em Python fluentemente
• Tem dashboard até para controlar o café
• Usa IA para prever o futuro (e acerta)

⚡ **Superpoderes:**
• Automatiza processos só de olhar
• Cria KPIs até para respirar
• Transforma PDF em API

⚠️ **Kryptonita:**
Sistemas legados e pessoas que imprimem e-mail. Quando vê arquivo em papel, entra em pânico existencial.

🎮 **Bordão:** "Isso aí dá pra automatizar!" (e geralmente dá mesmo)

🔮 **Profecia digital:** Tecnologia sem humanidade é só complicação disfarçada. Lembre-se: contratos são sobre pessoas, não apenas dados!
        """
    }
}

def inicializar_sessao():
    """Inicializa as variáveis de sessão"""
    if 'respostas' not in st.session_state:
        st.session_state.respostas = {}
    if 'pergunta_atual' not in st.session_state:
        st.session_state.pergunta_atual = 0
    if 'quiz_finalizado' not in st.session_state:
        st.session_state.quiz_finalizado = False
    if 'resultado_calculado' not in st.session_state:
        st.session_state.resultado_calculado = False

def calcular_resultado():
    """Calcula o perfil baseado nas respostas"""
    pontuacao = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    # Conta as respostas
    for pergunta_idx, resposta in st.session_state.respostas.items():
        pontuacao[resposta] += 1
    
    # Encontra o perfil dominante
    max_pontos = max(pontuacao.values())
    perfis_dominantes = [perfil for perfil, pontos in pontuacao.items() if pontos == max_pontos]
    
    if len(perfis_dominantes) == 1:
        return perfis_dominantes[0], False
    else:
        # Caso de empate
        return perfis_dominantes, True

def mostrar_carregamento():
    """Mostra animação de carregamento"""
    placeholder = st.empty()
    
    mensagens = [
        ("🔍", "Analisando suas respostas..."),
        ("🧠", "Processando seu perfil..."),
        ("📊", "Calculando compatibilidade..."),
        ("🎯", "Identificando seu tipo de gestor..."),
        ("✨", "Preparando seu resultado...")
    ]
    
    for i, (emoji, mensagem) in enumerate(mensagens):
        with placeholder.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f'<div class="big-emoji">{emoji}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="loading-text">{mensagem}</div>', unsafe_allow_html=True)
                
                # Barra de progresso estilizada
                progresso = (i + 1) / len(mensagens)
                st.progress(progresso)
            
        time.sleep(1.2)
    
    placeholder.empty()

def mostrar_resultado():
    """Mostra o resultado final"""
    resultado, empate = calcular_resultado()
    
    if empate:
        # Caso de empate
        st.balloons()
        
        # Container principal centralizado apenas na horizontal
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.markdown("""
            <div class="result-container">
                <h1 style="text-align: center;">🤯 HÍBRIDO INDECISO!</h1>
            </div>
            """, unsafe_allow_html=True)
            
            # Imagem de empate
            if os.path.exists("images/characters/empate_1.jpg"):
                try:
                    img = Image.open("images/characters/empate_1.jpg")
                    st.image(img, use_container_width=True)
                except:
                    st.markdown('<div style="text-align: center;"><span class="big-emoji">🤷‍♂️</span></div>', unsafe_allow_html=True)
            
            perfis_nomes = [PERFIS[p]["nome"] for p in resultado]
            
            st.markdown(f"## Você é um híbrido entre {' e '.join(perfis_nomes)}!")
            
            st.markdown("""
            ### 🎭 O que isso significa?
            
            Você é tipo aquele colega que:
            - Um dia chega resolvendo tudo na base do "deixa comigo" 
            - No outro tá pedindo parecer jurídico pra comprar clips
            - E na sexta tá escondido embaixo da mesa quando toca o telefone
            
            ### 🤔 Diagnóstico Profissional:
            
            **Síndrome do Gestor Camaleão** - Muda de cor conforme o contrato!
            
            Você tem múltiplas personalidades gerenciais, o que pode significar:
            1. Você é extremamente adaptável (ótimo!)
            2. Ou está em crise existencial profunda (nem tão ótimo...)
            
            ### 💊 Prescrição Médica:
            
            - **Dose diária de autoconhecimento**: Descubra qual perfil te deixa mais feliz
            - **Terapia de grupo**: Converse com outros gestores (eles também estão perdidos)
            - **Exercício prático**: Escolha UM estilo por contrato e veja o que acontece
            
            ### 🎯 Missão Especial:
            
            Use sua versatilidade como superpoder! Seja o Coringa da gestão de contratos - imprevisível, mas sempre eficaz!
            """)
    else:
        # Resultado normal
        perfil = PERFIS[resultado]
        
        # Efeitos visuais
        st.balloons()
        
        # Container principal centralizado apenas na horizontal
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.markdown(f"""
            <div class="result-container">
                <h1 style="text-align: center;">{perfil['emoji']} {perfil['nome'].upper()}!</h1>
            </div>
            """, unsafe_allow_html=True)
            
            # Imagem do perfil
            if os.path.exists(perfil["imagem"]):
                try:
                    img = Image.open(perfil["imagem"])
                    st.image(img, use_container_width=True)
                except Exception as e:
                    st.markdown(f'<div style="text-align: center;"><span class="big-emoji">{perfil["emoji"]}</span></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="text-align: center;"><span class="big-emoji">{perfil["emoji"]}</span></div>', unsafe_allow_html=True)
            
            # Descrição do perfil com markdown normal
            st.markdown(perfil["descricao"])
    
    # Espaçamento
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Botão para reiniciar centralizado
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Fazer o Quiz Novamente", key="reiniciar", use_container_width=True):
            # Reset das variáveis de sessão
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Análise detalhada no final (opcional)
    with st.expander("📊 Ver análise detalhada das respostas"):
        # Cria dados para o gráfico
        respostas_lista = list(st.session_state.respostas.values())
        perfis = ['🎯 Executor', '📋 Burocrata', '😰 Sobrevivente', '🤖 Futurista']
        contagens = [
            respostas_lista.count('A'),
            respostas_lista.count('B'),
            respostas_lista.count('C'),
            respostas_lista.count('D')
        ]
        
        # Mostra as métricas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(perfis[0], f"{contagens[0]} respostas")
        with col2:
            st.metric(perfis[1], f"{contagens[1]} respostas")
        with col3:
            st.metric(perfis[2], f"{contagens[2]} respostas")
        with col4:
            st.metric(perfis[3], f"{contagens[3]} respostas")

def main():
    """Função principal da aplicação"""
    inicializar_sessao()
    
    # Título principal
    st.markdown('<h1 class="main-title">🎯 Quiz do Gestor de Contratos</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Descubra qual é o seu perfil como gestor de contratos públicos!</p>', unsafe_allow_html=True)
    
    # Se o quiz não foi iniciado, mostra introdução
    if 'quiz_iniciado' not in st.session_state:
        st.session_state.quiz_iniciado = False
    
    if not st.session_state.quiz_iniciado and not st.session_state.quiz_finalizado:
        # Container de introdução
        st.markdown("""
        ### 🎮 Como funciona:
        
        - 📝 **9 perguntas** sobre seu estilo de gestão
        - 🎯 **4 opções** em cada pergunta (A, B, C, D)
        - ⏱️ **5 minutos** para completar
        - 🏆 **4 perfis possíveis**: Executor, Burocrata, Sobrevivente ou Futurista
        
        💡 **Dica:** Responda com sinceridade! Cada opção (A, B, C, D) corresponde a um perfil diferente.
        """)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Começar o Quiz", use_container_width=True):
                st.session_state.quiz_iniciado = True
                st.rerun()
    
    # Se o quiz foi iniciado mas não finalizado, mostra as perguntas
    elif st.session_state.quiz_iniciado and not st.session_state.quiz_finalizado:
        pergunta_idx = st.session_state.pergunta_atual
        total_perguntas = len(PERGUNTAS)
        
        # Badge de progresso estilizado
        st.markdown(f'<div class="question-badge">📝 Pergunta {pergunta_idx + 1} de {total_perguntas}</div>', unsafe_allow_html=True)
        
        # Barra de progresso visual
        progresso = (pergunta_idx + 1) / total_perguntas
        st.progress(progresso)
        
        # Espaçamento
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Pergunta atual com container estilizado
        pergunta = PERGUNTAS[pergunta_idx]
        
        st.markdown(f'<div class="question-container"><h3>{pergunta["pergunta"]}</h3></div>', unsafe_allow_html=True)
        
        # Opções de resposta com visual melhorado
        opcao_selecionada = st.radio(
            "🎯 Escolha sua resposta:",
            options=list(pergunta["opcoes"].keys()),
            format_func=lambda x: f"{x}) {pergunta['opcoes'][x]}",
            key=f"pergunta_{pergunta_idx}"
        )
        
        # Container de navegação
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if pergunta_idx > 0:
                if st.button("⬅️ Anterior", use_container_width=True):
                    # Salva a resposta atual antes de voltar
                    if opcao_selecionada:
                        st.session_state.respostas[pergunta_idx] = opcao_selecionada
                    st.session_state.pergunta_atual -= 1
                    st.rerun()
        
        with col3:
            if opcao_selecionada:
                # Salva a resposta atual imediatamente
                st.session_state.respostas[pergunta_idx] = opcao_selecionada
                
                if pergunta_idx < total_perguntas - 1:
                    if st.button("Próxima ➡️", use_container_width=True):
                        st.session_state.pergunta_atual += 1
                        st.rerun()
                else:
                    if st.button("🏁 Finalizar Quiz", use_container_width=True):
                        st.session_state.quiz_finalizado = True
                        st.rerun()
    
    # Se o quiz foi finalizado mas o resultado ainda não foi calculado
    elif not st.session_state.resultado_calculado:
        mostrar_carregamento()
        st.session_state.resultado_calculado = True
        st.rerun()
    
    # Mostra o resultado final
    else:
        mostrar_resultado()

if __name__ == "__main__":
    main()

