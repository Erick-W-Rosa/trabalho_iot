import time
import random
import statistics

def simular_dispositivos(qtd_dispositivos=20, prob_falha=0.05):
    """
    qtd_dispositivos: quantidade de dispositivos a simular (5 a 20)
    prob_falha: probabilidade de falha no envio (0.05 = 5%)
    """
    tempos_envio = []
    falhas = 0

    print(f"Simulando {qtd_dispositivos} dispositivos...\n")

    for i in range(1, qtd_dispositivos + 1):
        inicio = time.perf_counter()

        # Simula tempo de envio (rede, processamento etc.)
        time.sleep(random.uniform(0.05, 0.2))

        # Define se o envio teve sucesso ou falha
        sucesso = random.random() > prob_falha

        fim = time.perf_counter()
        tempo_envio = fim - inicio
        tempos_envio.append(tempo_envio)

        if sucesso:
            print(f"[Dispositivo {i}] ✔️ Envio realizado! ({tempo_envio:.4f} s)")
        else:
            falhas += 1
            print(f"[Dispositivo {i}] ❌ Falha no envio! ({tempo_envio:.4f} s)")

    # Métricas
    tempo_medio = statistics.mean(tempos_envio)
    taxa_perda = (falhas / qtd_dispositivos) * 100

    print("\n===== MÉTRICAS =====")
    print(f"⏱️ Tempo médio de envio: {tempo_medio:.4f} s")
    print(f"📉 Taxa de perda: {taxa_perda:.2f}% ({falhas}/{qtd_dispositivos})")

    # Retorna se você quiser usar depois
    return tempo_medio, taxa_perda, falhas


if __name__ == "__main__":
    # Aqui você escolhe entre 5 e 20
    qtd = int(input("Quantos dispositivos deseja simular (5 a 20)? "))
    if qtd < 5 or qtd > 20:
        print("Valor inválido, usando 20 por padrão.")
        qtd = 20

    simular_dispositivos(qtd_dispositivos=qtd, prob_falha=0.05)
