<h1 align="center">
  <h1 align="center">Sistema de Reconhecimento Facial</h1>
  <br>
</h1>

## 🧠 **Sobre o Projeto**
O Sistema de Reconhecimento Facial é uma aplicação de inteligência artificial desenvolvida para identificar e autenticar rostos humanos a partir da webcam. Utilizando técnicas avançadas de visão computacional e modelos de aprendizado profundo, o sistema é capaz de detectar rostos com precisão, extrair características faciais únicas e compará-las com uma base de dados previamente cadastrada.

### 🔍 Funcionalidades principais:

📸 Captura de imagens ou vídeo em tempo real via webcam;

🧠 Detecção facial com MTCNN ou Haar Cascade (OpenCV);

🔐 Extração de embeddings faciais com modelo pré-treinado (ex: FaceNet ou ResNet);

📂 Comparação de rostos com base local de usuários cadastrados;

✅ Indicação de identidade reconhecida com nível de confiança exibido na tela;

❌ Marcação de rostos não reconhecidos com alerta visual;

⚙️ Sistema totalmente local em Python com arquivos .py, sem uso de servidores externos ou nuvem.

### 🚀 Aplicações e utilidade:

- Sistemas de controle de acesso com reconhecimento facial;

- Autenticação biométrica para softwares e dispositivos;

- Projetos educacionais em IA, visão computacional e segurança digital;

- Protótipos de interfaces interativas com verificação de identidade.

## ⚙️ **Instalação**
### Passo 1: Clonar o repositório

Rode o comando abaixo:

```bash
git clone https://github.com/enzopcz2/reconhecimento_facial.git
cd reconhecimento_facial
```

### Passo 2: Instalar requerimentos

Instale as dependências do projeto usando o pip:

```bash
pip install -r requirements.txt
```

### Passo 3: Cadastrar rosto

Dentro da pasta "rostos", coloque uma foto .jpg do rosto que deseja cadastrar, sendo o nome do arquivo, o nome da pessoa cadastrada, como dado nos rostos de exemplo.

### Passo 4: Rodar o programa

Com os rostos cadastrados. Rode o comando abaixo:

```bash
python reconhecimento_facial.py
```

ou

```bash
python3 reconhecimento_facial.py
```

E pronto, sua webcam aparecerá e em cima do rosto identificado, terá o nome da pessoa.

## ⚠️ **Importante**
Dependendo de como é sua webcam, o seguinte trecho do código pode causar problemas:

```bash
cap = cv2.VideoCapture(0)
```

Caso sua webcam não funcione, tente trocar o 0 por -1, 1 ou 2. Isso deve fazer funcionar perfeitamente.
