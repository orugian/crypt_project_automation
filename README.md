NETRUNNER // CRYPTO_MODULE
--------------------------

Uma utilidade de criptografia Python baseada em terminal, projetada para o bloqueio imediato de arquivos. Utiliza criptografia simétrica Fernet para proteger arquivos diretamente no terminal, oferecendo uma experiência limpa e amigavel.

### ⚠️ AVISO: CRIPTOGRAFIA DESTRUTIVA

Esta ferramenta realiza criptografia **in-place** (no local). Quando você criptografa um arquivo, ele **sobrescreve os dados originais**. O arquivo permanece no mesmo local, mas torna-se ilegível sem a chave gerada.

> **Não teste isso em arquivos dos quais você não possa perder o acesso imediato.**

* * * * *

### Instalação

Certifique-se de ter o Python instalado. Instale a dependência `cryptography` via pip:

Bash

```
pip install cryptography

```

### Uso

Execute o script diretamente do seu terminal:

Bash

```
python terminal_crypt.py

```

* * * * *

### Guia da Interface

A aplicação inicia um sistema de menu no terminal:

-   **ENCRYPT (OVERWRITE):** Selecione esta opção para bloquear um arquivo.

    1.  Selecione o arquivo de destino (suporta arrastar e soltar).

    2.  Confirme a sobrescrita.

    3.  A ferramenta gera uma chave, salva-a em `[nome_do_arquivo].key` e exibe o hash no terminal.

-   **DECRYPT (RESTORE):** Selecione esta opção para recuperar um arquivo.

    1.  Selecione o arquivo bloqueado.

    2.  Selecione o arquivo `.key` associado.

    3.  A ferramenta restaura o conteúdo original do arquivo.

* * * * *

### Arquivos do Projeto

-   `terminal_crypt.py`: O script executável principal.

-   `README.md`: Este arquivo de documentação.

-   `teste_files/`: (Pasta de exemplo contendo scripts de teste).

-   `images/`: (Capturas de tela da ferramenta em ação).

* * * * *

### Funcionalidades

-   **Bloqueio Instantâneo:** Sem cópias temporárias. O arquivo é criptografado no local.

-   **Persistência de Chave:** Salva automaticamente um arquivo `.key` junto ao arquivo criptografado.

-   **Visibilidade do Hash:** Exibe a chave gerada no terminal para cópia imediata.

-   **UX Robusta:** Gerencia a formatação de caminhos (paths) e valida a existência do arquivo antes da execução.

* * * * *

### Exemplo de Fluxo de Trabalho

#### Criptografia


```
> SELECT TARGET FILE PATH:
>> "C:\Users\LO\Documents\segredos.txt"

[WARNING] THIS WILL OVERWRITE: segredos.txt
> CONFIRM OVERWRITE? [Y/N]: Y

> GENERATING KEY HASH...
[SUCCESS] PAYLOCK ENGAGED.
>> KEY HASH (COPY THIS):
----------------------------------------
gAAAAABlXy...
----------------------------------------

```

#### Descriptografia


```
> SELECT TARGET FILE PATH:
>> "C:\Users\LO\Documents\segredos.txt"

> ENTER KEY FILE PATH: "C:\Users\LO\Documents\segredos.txt.key"

> DECRYPTING STREAM...
[SUCCESS] PAYLOAD RESTORED.

```

* * * * *

### Créditos

Construído com Python e `cryptography.fernet`. Projetado para automação de scripts.
