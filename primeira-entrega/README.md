# Primeira Entrega

## Arquivos

- `client.py`: Cliente. Lê um arquivo, envia para o servidor e recebe o arquivo de volta.
- `server.py`: Servidor. Recebe um arquivo do cliente, salva e envia de volta para o cliente.
- `test_file.txt` e `imagem.png`: Arquivos de teste que podem ser usados para testar a transferência de arquivos.

## Como usar

1. Execute o servidor:
    ```sh
    python server.py
    ```

2. Em outro terminal, execute o cliente e siga as instruções para enviar um arquivo:
    ```sh
    python client.py
    ```

O cliente enviará o arquivo para o servidor (guardado em received_file no diretório que foi rodado), que por sua vez enviará o arquivo de volta para o cliente (guardado em received_back_file + extensão no diretório que foi rodado).