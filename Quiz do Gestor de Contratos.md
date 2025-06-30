# Quiz do Gestor de Contratos

Um minigame interativo desenvolvido em Python usando Streamlit para identificar perfis de gestores de contratos públicos. Criado especialmente para palestras sobre gestão de contratos na Administração Pública.

## 🎯 Objetivo

Identificar o perfil do gestor participante através de 9 perguntas de múltipla escolha, classificando-o automaticamente em um dos 4 perfis distintos:

- **🎯 Gestor Executor**: Focado em resultados e ação
- **📋 Gestor Burocrata**: Metódico e seguidor de processos
- **😅 Gestor Sobrevivente**: Defensivo e cauteloso
- **🤖 Gestor Futurista**: Inovador e tecnológico

## 🚀 Funcionalidades

- Interface visual atrativa e responsiva
- 9 perguntas de múltipla escolha com navegação fluida
- Barra de progresso em tempo real
- Carregamento animado no resultado
- Exibição do perfil com imagem e descrição personalizada
- Tratamento para casos de empate entre perfis
- Botão para reiniciar o quiz

## 📋 Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes do Python)

## 🛠️ Instalação

1. **Clone ou baixe os arquivos do projeto**

2. **Instale as dependências:**
   ```bash
   pip install streamlit pillow
   ```

3. **Verifique se a estrutura de arquivos está correta:**
   ```
   projeto/
   ├── app.py
   ├── images/
   │   └── characters/
   │       ├── executor_1.jpg
   │       ├── burocrata_1.jpg
   │       ├── sobrevivente_1.jpg
   │       ├── futurista_1.webp
   │       └── empate_1.jpg
   └── README.md
   ```

## ▶️ Como Executar

1. **Abra o terminal/prompt de comando**

2. **Navegue até a pasta do projeto:**
   ```bash
   cd caminho/para/o/projeto
   ```

3. **Execute o aplicativo:**
   ```bash
   streamlit run app.py
   ```

4. **Acesse no navegador:**
   - O Streamlit abrirá automaticamente no navegador
   - Caso não abra, acesse: `http://localhost:8501`

## 🎮 Como Usar

1. **Início**: A tela inicial apresenta o título e descrição do quiz
2. **Perguntas**: Responda as 9 perguntas selecionando uma das 4 opções (A, B, C, D)
3. **Navegação**: Use os botões "Anterior" e "Próxima" para navegar entre as perguntas
4. **Finalização**: Clique em "Finalizar Quiz" na última pergunta
5. **Resultado**: Aguarde o carregamento animado e veja seu perfil
6. **Reiniciar**: Use o botão "Fazer o Quiz Novamente" para uma nova tentativa

## 🎨 Personalização

### Modificar Perguntas
Edite o array `PERGUNTAS` no arquivo `app.py` para alterar as perguntas e opções.

### Alterar Perfis
Modifique o dicionário `PERFIS` no arquivo `app.py` para:
- Mudar descrições dos perfis
- Alterar emojis
- Trocar imagens (coloque novas imagens na pasta `images/characters/`)

### Customizar Visual
Ajuste o CSS personalizado na seção `st.markdown()` do arquivo `app.py` para modificar:
- Cores
- Fontes
- Layout
- Animações

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### Erro: "FileNotFoundError" para imagens
- Verifique se a pasta `images/characters/` existe
- Confirme se todas as imagens estão na pasta correta
- Verifique os nomes dos arquivos no código

### Aplicação não abre no navegador
- Verifique se a porta 8501 está disponível
- Tente acessar manualmente: `http://localhost:8501`
- Use uma porta diferente: `streamlit run app.py --server.port 8502`

## 📱 Compatibilidade

- **Navegadores**: Chrome, Firefox, Safari, Edge
- **Dispositivos**: Desktop, tablet, smartphone
- **Sistemas**: Windows, macOS, Linux

## 🎤 Uso em Palestras

### Dicas para Apresentação:
1. **Teste antes**: Execute o quiz completamente antes da palestra
2. **Tela cheia**: Use F11 para modo tela cheia durante a apresentação
3. **Interação**: Convide participantes para responder em tempo real
4. **Discussão**: Use os resultados para discussões sobre gestão de contratos

### Sugestões de Dinâmica:
- Peça para alguns participantes fazerem o quiz ao vivo
- Discuta cada perfil após os resultados
- Compare diferentes perfis e suas características
- Use como quebra-gelo ou atividade de engajamento

## 📄 Licença

Este projeto foi desenvolvido para uso educacional e em palestras sobre gestão de contratos públicos.

## 🤝 Suporte

Para dúvidas ou problemas:
1. Verifique a seção "Solução de Problemas"
2. Confirme se todos os arquivos estão presentes
3. Teste em um navegador diferente

---

**Desenvolvido para o 12° Contratos Week - Foz do Iguaçu**
*Ferramenta interativa para identificação de perfis de gestores de contratos públicos*

