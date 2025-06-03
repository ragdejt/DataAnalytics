import streamlit
from sqlalchemy import text
from database.database import SessionLocal

def page_config(
        title:str = 'DataAnalytics',
        icon:str = '',
        layout:str = 'wide',
        initial_sidebar_state:str = 'expanded',
):
    """Configure the Streamlit page settings."""
    streamlit.set_page_config(
        page_title=title,
        page_icon=icon,
        layout=layout,
        initial_sidebar_state=initial_sidebar_state,
    )

    if 'login' not in streamlit.session_state:
        streamlit.session_state['login'] = False
    if 'user' not in streamlit.session_state:
        streamlit.session_state['user'] = None
    streamlit.markdown(
        """
        <style>

        .stMainMenu {
            display:none;
        }

        .stDecoration {
            display:none;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    if streamlit.session_state['login'] and streamlit.session_state['user']:
        coluna1, coluna2 = streamlit.columns(
            [1, 0.2],
            gap='small',
            vertical_alignment='center',
            border=True
        )
        with coluna1:
            streamlit.title(':green[DataAnalytics]')
        with coluna2:
            streamlit.title(f'{streamlit.session_state["user"]}')

        with streamlit.sidebar:
            option = streamlit.selectbox(
                label='Selecione uma opção',
                options=[
                    'Adicionar',
                    'Editar',
                    'Consultar'
                ],
                index=None,
                placeholder='Selecione uma opção'
            )
            streamlit.button(
                label='Sair',
                icon=':material/logout:',
                use_container_width=True,
                on_click=lambda: streamlit.session_state.update({'login': False}),
            )
        return option
    else:
        streamlit.header('Transforme dados em :green[Decisões estratégicas]', divider='green')
        streamlit.subheader('Centralize informações, automatize processos e ganhe eficiência operacional com relatórios em tempo real.')  
        streamlit.write("Isso não é futurismo é :green[DataAnalytics]!")

        with streamlit.expander(
            label="Porque Data Analytics ?",
            icon=':material/indeterminate_question_box:',
        ):
            streamlit.info("""
            A utilização de um sistema logístico traz inúmeras vantagens para qualquer empresa que busca crescimento, organização e eficiência. 
            Esse tipo de sistema permite que todas as informações essenciais como dados de produtos, fornecedores, funcionários e estoque sejam centralizadas e organizadas de forma clara! 
            Evitando perda de dados e falhas de controle. Além disso, a automação de processos rotineiros reduz o tempo gasto com tarefas manuais e diminui consideravelmente o risco de erros. 
            O que impacta diretamente na produtividade da equipe.
                            
            Outro grande benefício é a geração rápida e confiável de relatórios, que facilita a análise de dados e permite uma tomada de decisões mais estratégica e segura. 
            O controle de estoque também se torna muito mais eficiente, já que o sistema acompanha em tempo real a entrada e saída de produtos! 
            Ajudando a evitar desperdícios, faltas ou excessos de mercadorias. 
            Com uma interface acessível e muitas vezes disponível online, gestores e colaboradores podem acessar informações de qualquer lugar, tornando a administração mais flexível e dinâmica.
            Além disso, um sistema logístico bem estruturado contribui diretamente para a redução de custos operacionais! 
            Pois diminui falhas, retrabalhos e desperdícios, aumentando o lucro e a eficiência geral da empresa. 
            Outro ponto importante é que, com os dados organizados e atualizados, auditorias e análises se tornam muito mais simples e transparentes, fortalecendo a confiança na gestão. 
            Em resumo, investir em um sistema logístico é apostar na organização, no controle e no crescimento sustentável de uma empresa.
            """
            )
        column1, column2 = streamlit.columns(2)
        with column1:
            with streamlit.expander("✔️ :green[Vantagens]"):
                streamlit.write("``Organização e Centralização de Dados``")
                streamlit.info("""
                Um sistema logístico permite que todas as informações importantes da empresa como produtos, fornecedores e funcionários sejam organizadas e armazenadas em um único lugar.
                Isso elimina a necessidade de planilhas manuais ou anotações dispersas, reduzindo falhas e otimizando o acesso aos dados.
                """)
                streamlit.divider()
                streamlit.write("``Agilidade na Tomada de Decisões``")
                streamlit.info("""
                Com dados atualizados em tempo real e relatórios automatizados, a gestão consegue identificar rapidamente problemas e oportunidades.
                Isso permite uma tomada de decisão mais assertiva, embasada em dados concretos e não em suposições.
                """)
                streamlit.divider()
                streamlit.write("``Redução de Erros e Retrabalho``")
                streamlit.info("""
                Ao automatizar cadastros, atualizações e geração de relatórios, o sistema minimiza erros manuais, como duplicidade de informações ou falhas de digitação.
                Diminuindo a porcentagem de erros isso impacta diretamente no controle de estoque, faturamento ou entrega.
                """)
                streamlit.divider()
                streamlit.write("``Melhor Controle de Estoque e Recursos``")
                streamlit.info("""
                Um sistema logístico facilita o acompanhamento do nível de estoque, evitando tanto a falta quanto o excesso de produtos.
                Isso ajuda na organização de compras, reduz desperdícios e melhora o planejamento de reposição.
                """)
                streamlit.divider()
                streamlit.write("``Otimização do Tempo e Aumento da Produtividade``")
                streamlit.info("""
                Automatizando tarefas operacionais que antes consumiam tempo, o sistema libera os colaboradores para se dedicarem a atividades mais estratégicas e produtivas, aumentando o rendimento geral da equipe.
                """)
                streamlit.divider()
                streamlit.write("``Facilidade de Acesso e Monitoramento Remoto``")
                streamlit.info("""
                Com uma interface web desenvolvida em streamlit o sistema pode ser acessado de qualquer lugar.
                Permitindo que gestores monitorem processos, verifiquem informações e gerem relatórios mesmo fora da empresa.
                """)
                streamlit.divider()
                streamlit.write("``Geração de Relatórios Profissionais``")
                streamlit.info("""
                A exportação de dados para planilhas Excel permite que informações sejam apresentadas de forma clara e organizada.
                Sendo ideal para auditorias, reuniões e análises estratégicas, facilitando o controle de resultados.
                """)
        with column2:
            with streamlit.expander("❌ :red[Desvantagens]"):
                streamlit.write("``Desorganização e Perda de Informações``")
                streamlit.error("""
                Sem um sistema, os dados da empresa costumam ficar espalhados em planilhas, anotações manuais ou arquivos soltos.
                Isso aumenta as chances de perda de informações importantes e dificulta o controle geral, prejudicando a eficiência do negócio.               
                """)
                streamlit.divider()
                streamlit.write("``Tomada de Decisões Lenta e Pouco Confiável``")
                streamlit.error("""
                A ausência de relatórios automatizados faz com que as decisões sejam baseadas em informações desatualizadas ou incompletas.
                Aumentando o risco de escolhas erradas que podem gerar prejuízos para a empresa.               
                """)
                streamlit.divider()
                streamlit.write("``Maior Risco de Erros Manuais``")
                streamlit.error("""
                Sem automação, o processo de cadastro, controle de estoque e emissão de relatórios depende do preenchimento manual, o que abre espaço para falhas humanas.
                Como digitação errada, duplicidade de dados ou perda de registros.               
                """)
                streamlit.divider()
                streamlit.write("``Controle de Estoque Ineficiente``")
                streamlit.error("""
                Sem um sistema, o acompanhamento de entradas e saídas de produtos é falho e impreciso!
                O que pode gerar tanto falta de produtos essenciais quanto excesso de estoque parado, aumentando custos e desperdícios.               
                """)
                streamlit.divider()
                streamlit.write("``Baixa Produtividade da Equipe``")
                streamlit.error("""
                Sem a automação de tarefas rotineiras, os colaboradores perdem muito tempo com processos manuais e repetitivos. 
                O que reduz a produtividade e desvia o foco de atividades realmente importantes para o crescimento da empresa.               
                """)
                streamlit.divider()
                streamlit.write("``Dificuldade de Acesso e Atualização de Dados``")
                streamlit.error("""
                Sem uma interface web, o acesso aos dados fica restrito a computadores específicos! 
                Dificultando a consulta de informações em tempo real e impedindo o monitoramento remoto, especialmente em situações de urgência.               
                """)
                streamlit.divider()
                streamlit.write("``Falta de Relatórios Confiáveis para Análises e Auditorias``")
                streamlit.error("""
                Empresas que não utilizam sistemas estruturados enfrentam dificuldade para gerar relatórios detalhados! 
                Prejudicando o acompanhamento do desempenho, o planejamento estratégico e a transparência em auditorias.               
                """)
        with streamlit.expander(
            label="Sobre nós",
            icon=':material/contact_page:'
        ):
            streamlit.subheader(":green[Quem somos]", divider="green")
            streamlit.write(
            """
            ✔️``r4gd3j7``                
            """)
        with streamlit.expander(
            label="Contato",
            icon=':material/contact_mail:'
        ):
            with streamlit.form(key='contact_form'):
                streamlit.subheader(":green[Formulário para contato]", divider="green")
                streamlit.text_input(
                    label="Nome completo",
                    type="default",
                    help="Full name.",
                    placeholder="Digite o nome completo."
                )
                streamlit.text_input(
                    label="Assunto",
                    type="default",
                    help="Subject.",
                    placeholder="Digite o motivo para o contato."
                )
                streamlit.text_input(
                    label="E-mail",
                    type="default",
                    help="E-mail.",
                    placeholder="Digite o e-mail."
                )
                streamlit.text_area(
                    label="Corpo do e-mail",
                    help="E-mail body.",
                    placeholder="Digite a mensagem que deseja encaminhar."
                )
                if streamlit.form_submit_button("Enviar", use_container_width=True):
                    pass
        with streamlit.expander(
            label='Ticket de suporte',
            icon=':material/help:'
        ):
            streamlit.subheader(body=':green[Ticket de suporte]', divider='green')
            tab1, tab2 = streamlit.tabs(['Abrir ticket', 'Visualizar tickets'])
            with tab1:
                with streamlit.form(key='ticket_form'):
                    streamlit.text_input(label='Usuario', placeholder='Digite o seu nome de usuario')
                    streamlit.selectbox(
                        label='Prioridade',
                        options=['Baixa', 'Media', 'Alta'],
                        index=None,
                        placeholder='Selecione a prioridade'
                    )
                    streamlit.text_input(
                        label='Assunto',
                        placeholder='Digite o assunto sobre o ticket'
                    )
                    streamlit.text_area(
                        label='Informações sobre o ticket',
                        placeholder='Digite os detalhes sobre o ocorrido'
                    )
                    if streamlit.form_submit_button(
                        label='Enviar ticket',
                        use_container_width=True
                    ):
                        pass
            with tab2:
                pass
        with streamlit.expander(
            label='Entrar',
            icon=':material/login:',
            expanded=True,
        ):
            USERNAME = streamlit.text_input(
                label='Usuario',
                placeholder='Digite seu usuário',
            )
            PASSWORD = streamlit.text_input(
                label='Senha',
                type='password',
                placeholder='Digite sua senha',
            )
            if streamlit.button(
                label='Entrar',
                icon=':material/login:',
                use_container_width=True
            ):
                with SessionLocal() as session:
                    query = text(f"SELECT * FROM Usuarios WHERE Usuario = '{USERNAME}' AND Senha = '{PASSWORD}'")
                    result = session.execute(query).fetchone()
                    if result:
                        streamlit.session_state['login'] = True
                        streamlit.session_state['user'] = USERNAME
                        streamlit.success('Login realizado com sucesso!')
                        streamlit.toast('Login realizado com sucesso!')
                        streamlit.rerun()
                    else:
                        streamlit.error('Usuário ou senha inválidos!')
                        streamlit.toast('Usuário ou senha inválidos!')
