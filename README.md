# split-collections-move <a href="https://skillicons.dev"> <img width="30px" align="right" src="https://skillicons.dev/icons?i=python" /> </a>

Este script foi desenvolvido para automatizar a organização de coletas de dados, separando os arquivos por fabricante e modelo correspondente. Após a execução, ele move os arquivos para pastas específicas baseadas nos critérios definidos. Caso algum arquivo não seja movido, isso pode indicar que ele está inválido ou que o modelo ainda não é suportado pelo script.

## **Como Usar**

1. **Execução do Script**  
   Ao executar o script, um prompt será exibido solicitando o caminho da pasta onde estão localizadas as coletas.  
   - Copie o caminho completo da pasta e cole no prompt.

2. **Estrutura de Arquivos**  
   Os arquivos de coleta não precisam estar organizados em uma única pasta. O script realizará uma busca recursiva em todas as subpastas, independentemente da extensão dos arquivos.

## **Tecnologias Suportadas**

Atualmente, o script oferece suporte para as seguintes tecnologias e modelos:

- **Cisco:** IOS, NX, WLC  
- **Dell:** Modelo N, 6200, 8024, 7048, EMC S, OS10  
- **Aruba:** OS, CX  
- **HP:** Comware  
- **3COM**  
- **Huawei**  
- **Enterasys**

## **Observações**
- Arquivos não movidos podem indicar que:  
  - O arquivo está inválido.  
  - O modelo específico ainda não é suportado pelo script.
## Pré-requisitos

- Python 3.10 ou superior

Instale as dependências padrão do Python, caso necessário:

```bash
pip install --upgrade pip
