# docs-br

Este projeto implementa a validação, formatação e geração de documentos brasileiros, especificamente CPF e CNPJ, mas a lógica é a mesma para diversos outros documentos que utilizam a mesma classe de algoritmos de validação.

A validação de documentos como CPF e CNPJ é feita utilizando algoritmos que verificam a conformidade dos dígitos verificadores. Esses dígitos são calculados a partir dos demais dígitos do documento utilizando um cálculo de módulo.

## Novo padrão de CNPJ

A partir de 2026, os CNPJs poderão conter números e letras. Este projeto já está preparado para lidar com essa mudança, garantindo a validação correta dos novos formatos de CNPJ.

## Algoritmo de Validação

O algoritmo de validação segue os seguintes passos:

1. **Extrair os dígitos do documento**: Os dígitos são extraídos do documento, ignorando qualquer caractere de formatação.
2. **Calcular os dígitos verificadores**: Utilizando o cálculo de módulo, os dígitos verificadores são gerados.
3. **Comparar os dígitos verificadores**: Os dígitos verificadores calculados são comparados com os dígitos verificadores do documento.
4. **Verificar a validade**: Se os dígitos verificadores coincidirem, o documento é considerado válido.

## Cálculo de Módulo

O cálculo de módulo é uma operação matemática que encontra o resto da divisão de um número por outro. No contexto da validação de documentos, o cálculo de módulo é usado para gerar dígitos verificadores que garantem a integridade do documento.

Para CPF e CNPJ, o cálculo de módulo é feito da seguinte forma:

1. **Multiplicação por pesos**: Cada dígito do documento é multiplicado por um peso específico.
    - **CPF**:
      - Primeiro dígito verificador: (10, 9, 8, 7, 6, 5, 4, 3, 2)
      - Segundo dígito verificador: (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
    - **CNPJ**:
      - Primeiro dígito verificador: (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
      - Segundo dígito verificador: (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

2. **Soma dos resultados**: Somar os resultados das multiplicações.

3. **Cálculo do módulo**: Calcular o módulo da soma pelo número base (geralmente 11).

4. **Transformação do módulo**: Transformar o resultado do módulo em um dígito verificador.
    - Se o resultado for menor que 2, o dígito verificador é 0.
    - Caso contrário, o dígito verificador é 11 menos o resultado do módulo.

## Implementação

A implementação dos algoritmos de validação, formatação e geração de CPF e CNPJ está contida nas classes `DocBrCPF` e `DocBrCNPJ`. Ambas as classes herdam da classe base `DocBr`, que contém a lógica comum para manipulação dos documentos.

- **DocBrCPF**: Implementa a lógica específica para CPF, incluindo os pesos e a máscara de formatação.
- **DocBrCNPJ**: Implementa a lógica específica para CNPJ, incluindo os pesos e a máscara de formatação. Essa classe suporta caracteres alfanuméricos.

Para mais detalhes sobre a implementação, consulte os arquivos de código na pasta `src`.
