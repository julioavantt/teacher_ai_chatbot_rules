```mermaid
flowchart TD

    A[INICIO] -->|1| B[Responde: reglas["1"] <br> ↺ INICIO]
    A -->|2| C[Responde: reglas["2"] <br> Estado = PEDIDO]
    A -->|3| D[Responde: reglas["3"] <br> ↺ INICIO]
    A -->|4| E[Responde: opciones_menu() <br> ↺ INICIO]
    A -->|otro| F[Responde: no_entendido <br> ↺ INICIO]

    %% Bloque de PEDIDO
    C --> G[PEDIDO]
    G -->|Coincidencia ≥ 80%| H[Responde opción <br> Estado = opción]
    G -->|Coincidencia < 80%| I[Responde: no_entendido <br> Estado sigue en PEDIDO]

    %% Otro estado (cuando queda en una opción específica)
    H --> J[OTRO ESTADO]
    J --> K["🫃 " + reglas["tomar_pedido"] <br> ↺ INICIO]
```
