import os
import shutil
import time

def obter_caminho():

    caminho = input(r"Insira o caminho da coleta: ").strip()
    
    if not os.path.isdir(caminho):
        print(f"Erro: O caminho '{caminho}' não é válido ou não é um diretório.")
        return None
    return caminho


def mover_arquivo(origem, destino):
    os.makedirs(destino, exist_ok=True)
    
    for _ in range(5):
        try:
            shutil.move(origem, destino)
            return
        except PermissionError:
            print(f"Arquivo em uso, tentando novamente: {origem}")
            time.sleep(1)
        except Exception as e:
            print(f"Erro ao mover {origem}: {e}")
            return


def processar_arquivo(caminho_completo, caminho_base):
    
    try:
      
        with open(caminho_completo, 'r', errors='ignore') as arquivo:
            linhas = arquivo.readlines()  

        
        for linha in linhas:
            if linha.startswith("Cisco IOS Software"):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Cisco', 'IOS')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith("Cisco Nexus Operating System"):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Cisco', 'NX')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('Product Name..................................... Cisco Controller'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Cisco', 'WLC')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('!System Description "Dell EMC Networking N') or linha.startswith('!System Description "Dell Networking N'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Dell', 'Modelo N')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('!System Description "PowerConnect 6'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Dell', '6200')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('!System Description "Powerconnect 80'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Dell', '8000')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('!System Description "PowerConnect 7048'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Dell', '7048')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('Dell EMC Real Time Operating System Software'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Dell', 'EMC S')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('Dell EMC Networking OS10') or linha.startswith('Dell SmartFabric OS10'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Dell', 'OS10')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('!Version ArubaOS-CX'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Aruba', 'CX')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('ArubaOS'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Aruba', 'OS')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('HPE Comware') or linha.startswith('HP Comware') or linha.startswith('H3C Comware'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'HP', 'Comware')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('3Com Corporation'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', '3COM')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('Huawei Versatile Routing') or linha.startswith('Huawei YunShan'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Huawei')
                mover_arquivo(caminho_completo, destino)
                return
            elif linha.startswith('Copyright (c) 2012 by Enterasys') or linha.startswith('Copyright (c) 2005 by Enterasys') or linha.startswith('#***** ALL (DEFAULT and'):
                destino = os.path.join(caminho_base, 'Coleta_Separada', 'Enterasys')
                mover_arquivo(caminho_completo, destino)
                return
    except Exception as e:
        with open('Erro.txt', 'w', encoding='utf8') as erro_txt:
            erro_txt.write(f"Erro ao processar: {caminho_completo}: [ERRO]: {e}")
        print(f"Erro ao processar: {caminho_completo}: [ERRO]: {e}")


def ler_arquivos(caminho_base):
    
    for root, _, files in os.walk(caminho_base):
        for arquivo in files:
            caminho_completo = os.path.join(root, arquivo)
            processar_arquivo(caminho_completo, caminho_base)


def main():
    caminho = obter_caminho()
    if caminho:
        ler_arquivos(caminho)


if __name__ == '__main__':
    main()
