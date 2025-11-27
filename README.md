A simulação de 20 dispositivos IoT foi realizada utilizando um script Python (simulacao_iot.py), onde cada dispositivo enviou um pacote de dados simulados com tempo de rede aleatório entre 0,05 e 0,2 segundos. Uma taxa de falha de 5% foi aplicada para representar perdas reais de transmissão.

Após a execução, obteve-se o seguinte:

<img width="596" height="478" alt="image" src="https://github.com/user-attachments/assets/c5c2d32b-8dd0-49a2-bbee-bc330475d965" />

https://github.com/user-attachments/assets/b1b4be7b-87eb-4a00-9f2c-cdcfca43311c

E se aumentássemos para 1000 dispositivos?

Se o mesmo script fosse rodado sequencialmente (um dispositivo por vez), surgiriam vários problemas:

1️⃣ Tempo total de simulação ficaria muito alto

Com 20 dispositivos → ~2,4 segundos
Com 1000 dispositivos:

📌 1000 × 0.12 s ≈ 120 segundos (2 minutos)
Somente esperando sleep.

Isso inviabiliza cenários “reais”, onde vários dispositivos enviam simultaneamente.

2️⃣ Maior probabilidade de perdas reais de transmissão

Num sistema real (não no script):

- excesso de conexões simultâneas → congestionamento

- timeouts → pacotes descartados

- buffers cheios → falha de processamento

- servidor pode rejeitar requisições

Mesmo que o script use perda aleatória, no mundo real a taxa de perda subiria.

3️⃣ Impacto mais pesado na CPU

Com 1000 dispositivos:

- mais loops

- mais logs

- mais eventos para processar

- possíveis gargalos no interpretador Python

Se usar threads/async, o número de context switches aumenta, consumindo CPU.

4️⃣ Crescimento no uso de RAM

Se você armazenar:

- resultados

- logs

- buffers de mensagens

- filas de envio

O consumo de memória pode subir rápido.

5️⃣ Limites do sistema operacional

Em simulações paralelas reais:

- limite de sockets simultâneos

- limite de file descriptors

- filas de rede podem encher

- risco de travar o programa por thread storm

🧠 Conclusão para entregar no trabalho

Ao escalar de 20 para 1000 dispositivos, o sistema começaria a apresentar problemas de desempenho, principalmente devido ao aumento do tempo total de envio, maior carga na CPU, maior consumo de RAM e possíveis gargalos na capacidade de conexões simultâneas. Em sistemas reais, isso exigiria técnicas como envio assíncrono, filas de mensagens (MQTT, Kafka, RabbitMQ), balanceamento de carga e mecanismos de retry/backoff.



