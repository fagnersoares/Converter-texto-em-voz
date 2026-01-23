import asyncio
import edge_tts
import sys

# Configurações padrão
TEXTO_PADRAO = "Olá! Este é um áudio gerado automaticamente."
VOZ_PADRAO = "pt-BR-FranciscaNeural"
ARQUIVO_SAIDA = "narracao.mp3"

async def gerar_audio(texto=TEXTO_PADRAO):
    communicate = edge_tts.Communicate(texto, VOZ_PADRAO)
    await communicate.save(ARQUIVO_SAIDA)
    print(f"✅ Áudio salvo com sucesso: {ARQUIVO_SAIDA}")

async def listar_vozes():
    vozes = await edge_tts.list_voices()
    print(f"{'ID DA VOZ':<30} | {'GÊNERO'}")
    print("-" * 45)
    for v in vozes:
        if v["Locale"] == "pt-BR":
            print(f"{v['ShortName']:<30} | {v['Gender']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()
        if comando == "listar":
            asyncio.run(listar_vozes())
        elif comando == "gerar":
            # Se o usuário digitou texto após 'gerar', usa esse texto
            texto_para_gerar = sys.argv[2] if len(sys.argv) > 2 else TEXTO_PADRAO
            asyncio.run(gerar_audio(texto_para_gerar))
        else:
            print("Comandos: listar | gerar 'seu texto aqui'")
    else:
        print("Use: python gerador_voz.py listar OU python gerador_voz.py gerar")