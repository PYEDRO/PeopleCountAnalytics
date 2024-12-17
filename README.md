# PeopleCountAnalytics

## People Count Analytics

## Project Overview

Este repositório contém o código para um sistema inovador de contagem de pessoas projetado para analisar vídeos enviados por usuários. Utilizando Python com **Flask** como framework backend, permite que os usuários definam áreas específicas dentro de seus vídeos para análise. O motor analítico é alimentado pelo **YOLOv3** (You Only Look Once versão 3), garantindo detecção precisa de objetos em tempo real. Para uma interação perfeita com o usuário, **React** foi empregado como tecnologia frontend.

## Features

- **Upload de Vídeo:** Os usuários podem enviar seus próprios vídeos para análise.
- **Seleção de Área Personalizada:** Defina áreas específicas dentro do vídeo onde deseja contar pessoas.
- **Integração com YOLOv3:** Utiliza YOLOv3 para detecção precisa e eficiente de objetos.
- **Frontend Interativo:** Construído com React para proporcionar uma experiência de usuário suave e responsiva.
- **Análise em Tempo Real:** Obtenha insights e contagens imediatas com base nas áreas definidas.

## Demo

![People Count Demo](assets/demo_video.gif)

*Assista ao demo acima.*

## Como Funciona

1. **Upload de Vídeo:**
   - Os usuários enviam seus arquivos de vídeo através da interface frontend.
2. **Definir Áreas de Monitoramento:**
   - Usando a ferramenta personalizada, os usuários desenham e selecionam áreas específicas no vídeo onde desejam contar pessoas.
3. **Processar Vídeo:**
   - O backend Flask processa as áreas selecionadas usando YOLOv3 para detectar e contar indivíduos com precisão.
4. **Visualizar Resultados:**
   - Os resultados são exibidos em tempo real na interface frontend baseada em React, mostrando o número de pessoas em cada área definida.

## Instalação & Configuração

### Configuração do Backend

1. **Navegue para o diretório do backend:**
    ```bash
    cd back_end
    ```

2. **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o servidor backend:**
    ```bash
    python main.py
    ```

### Configuração do Frontend

1. **Navegue para o diretório do frontend:**
    ```bash
    cd yolo-person-counter
    ```

2. **Instale os pacotes necessários:**
    ```bash
    npm install
    ```

3. **Inicie a aplicação frontend:**
    ```bash
    npm start
    ```

## Uso

1. **Inicie o Backend:**
   - Certifique-se de que o backend Flask está em execução seguindo os passos de configuração acima.

2. **Inicie o Frontend:**
   - Lance a aplicação React seguindo os passos de configuração acima.

3. **Enviar e Analisar:**
   - Abra o frontend no seu navegador.
   - Envie um vídeo usando a funcionalidade de upload.
   - Desenhe e defina as áreas que deseja monitorar para contagem de pessoas.
   - Veja as contagens e análises em tempo real enquanto o vídeo é processado.

## Tecnologias Utilizadas

- **Backend:**
  - **Flask:** Framework backend para lidar com requisições API e processamento de dados.
  - **YOLOv3:** Implementa detecção de objetos em tempo real para contagem precisa de pessoas.
  - **Python:** Linguagem de programação principal para a lógica do backend.
  - **Bancos de Dados:** PostgreSQL ou MongoDB para armazenamento de dados (escolha conforme sua configuração).

- **Frontend:**
  - **React:** Proporciona uma interface de usuário dinâmica e responsiva.
  - **JavaScript/TypeScript:** Linguagens principais para o desenvolvimento frontend.
  - **HTML/CSS:** Para estruturar e estilizar a aplicação.

## Contribuição

Contribuições são bem-vindas! Siga estes passos para contribuir:

1. **Faça um Fork do Repositório**
2. **Crie uma Branch de Feature**
    ```bash
    git checkout -b feature/SuaFeature
    ```
3. **Commit suas alterações**
    ```bash
    git commit -m "Adicione sua mensagem aqui"
    ```
4. **Push para a Branch**
    ```bash
    git push origin feature/SuaFeature
    ```
5. **Abra um Pull Request**

