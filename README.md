# docs-br

Este projeto apresenta a implementação do algoritmo de validação de documentos brasileiros que utilizam a lógica de cálculo de módulo para validação dos dígitos verificadores. Na estrutura atual, ele atende tanto os documentos tradicionais que utilizam apenas números, como também os novos CNPJs que poderão conter letras a partir de 2026.

## Implementações

Atualmente, as seguintes implementações estão disponíveis neste repositório:

| Linguagem      | CPF | CNPJ | CNH | TE | PIS | CERT | RENAVAM |
|----------------|-----|------|-----|----|-----|------|---------|
| Go             | x   | x    |     |    |     |      |         |
| Python         | x   | x    |     |    |     |      |         |
| Python (Numpy) | x   | x    |     |    |     |      |         |
| TypeScript     | x   | x    |     |    |     |      |         |
| C++            |     |      |     |    |     |      |         |
| C#             |     |      |     |    |     |      |         |
| Elixir         |     |      |     |    |     |      |         |
| Kotlin         |     |      |     |    |     |      |         |
| Javascript     |     |      |     |    |     |      |         |
| Java           |     |      |     |    |     |      |         |
| Python (Spark) |     |      |     |    |     |      |         |
| Ruby           |     |      |     |    |     |      |         |
| Rust           |     |      |     |    |     |      |         |

### Contribuições

Sinta-se a vontade para contribuir com novas implementações em outras linguagens ou contribuir com melhorias nas existentes. Toda contribuição é muito bem-vinda!

Para incluir um novo documento, abra uma branch com o nome do documento e da linguagem, por exemplo: `cpf-python`. Após a implementação, abra um pull request para a branch `main`.

Importante que sua implementação siga todos os passos do algoritmo de validação descritos abaixo, assim como os métodos: `generate`, `validate` e `format`. Além de incluir testes unitários para garantir a qualidade da implementação.

## Algoritmo de Validação

O processo de validação dos documentos segue os seguintes passos:

1. **Conversão dos caracteres em números**  
   - Cada caractere da string do documento é convertido em um número correspondente.  
   - Para isso, subtrai-se o valor ASCII de `'0'` (48) do código ASCII de cada caractere.
   - Como resultado:
     - Os caracteres `'0'` a `'9'` são convertidos nos valores `0` a `9`.  
     - Os caracteres `'A'` a `'Z'` geram valores começando em `17`, pois sua faixa ASCII começa em `65` (`65 - 48 = 17`).

2. **Verificação do comprimento**  
   - O documento deve conter um número exato de caracteres (11 para CPF, 14 para CNPJ).  
   - Caso contrário, ele é considerado inválido.

3. **Checagem de dígitos repetidos**  
   - Documentos compostos por todos os dígitos idênticos são inválidos.

4. **Cálculo dos dígitos verificadores**  
   - Multiplicam-se os dígitos por uma sequência de pesos predefinidos para cada documento.  
   - Os produtos são somados.  
   - O módulo da soma é calculado (base 11 para CPF e CNPJ).  
   - O resultado passa por uma função de transformação específica para determinar o dígito verificador.

5. **Comparação dos dígitos verificadores**  
   - Os dígitos verificadores calculados são comparados com os dígitos originais do documento.  
   - Se coincidirem, o documento é válido. Caso contrário, é inválido.

## Variáveis utilizadas para cada tipo de documento

### CPF (Cadastro de Pessoa Física)

- **Comprimento:** 11 caracteres
- **Base para Módulo:** 11  
- **Pesos:**  
  - Primeiro dígito: `(10, 9, 8, 7, 6, 5, 4, 3, 2)`  
  - Segundo dígito: `(11, 10, 9, 8, 7, 6, 5, 4, 3, 2)`  
- **Transformação:**  
  - Se o resultado for `< 2`, o dígito verificador é `0`.  
  - Caso contrário, `11 - resultado`.  
- **Máscara:** `###.###.###-##`
- **Conjunto de Dígitos Aceitos:** `0-9`

Referência: [Wikipedia - Cadastro de Pessoas Físicas](https://pt.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas)

---

### CNPJ (Cadastro Nacional da Pessoa Jurídica)

- **Comprimento:** 14 caracteres
- **Base para Módulo:** 11  
- **Pesos:**  
  - Primeiro dígito: `(5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)`  
  - Segundo dígito: `(6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)`  
- **Transformação:**  
  - Se o resultado for `< 2`, o dígito verificador é `0`.  
  - Caso contrário, `11 - resultado`.  
- **Máscara:** `##.###.###/####-##`  
- **Conjunto de Dígitos Aceitos:** `0-9` (atualmente) e `0-9A-Z` (a partir de 2026).  

Referência: [IN RFB nº 2.229/2024](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=141102)

---
