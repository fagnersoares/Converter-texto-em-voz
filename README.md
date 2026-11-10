# 🎙️ Conversor de Texto em Voz (Edge TTS)

Script em Python que transforma texto em áudio MP3 com as **vozes neurais da Microsoft**, usando a biblioteca [`edge-tts`](https://github.com/rany2/edge-tts). Criei para gerar narrações rápidas para vídeos no CapCut, TikTok e YouTube, sem pagar por serviços de locução.

## ✨ O que ele faz

- Lista todas as vozes disponíveis em português do Brasil, com o gênero de cada uma.
- Gera um arquivo `narracao.mp3` a partir de qualquer texto digitado no terminal.
- Usa por padrão a voz `pt-BR-FranciscaNeural`.
- Funciona de forma assíncrona (`asyncio`), sem precisar de chave de API.

## 🛠️ Tecnologias

- Python 3.7+
- [edge-tts](https://pypi.org/project/edge-tts/)
- asyncio

## 🚀 Como instalar

```bash
git clone https://github.com/fagnersoares/Converter-texto-em-voz.git
cd Converter-texto-em-voz

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## 🕹️ Como usar

**Listar as vozes brasileiras disponíveis:**

```bash
python gerador_voz.py listar
```

```
ID DA VOZ                      | GÊNERO
---------------------------------------------
pt-BR-AntonioNeural            | Male
pt-BR-FranciscaNeural          | Female
...
```

**Gerar um áudio:**

```bash
python gerador_voz.py gerar "Olá! Bem-vindo ao meu canal."
```

O áudio é salvo como `narracao.mp3` na pasta do projeto. Sem texto, o script usa uma frase de exemplo.

Para trocar a voz, altere a constante `VOZ_PADRAO` no início de `gerador_voz.py` por um dos IDs listados.

## 🗺️ Próximos passos

- Escolher a voz e o nome do arquivo pela linha de comando.
- Ler o texto de um arquivo `.txt` para narrações longas.
- Ajustar velocidade e tom da fala.

## 👤 Autor

**Fagner Soares** · [LinkedIn](https://www.linkedin.com/in/fagner-soares-19b400168/) · [GitHub](https://github.com/fagnersoares)
