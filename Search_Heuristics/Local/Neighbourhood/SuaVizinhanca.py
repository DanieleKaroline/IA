import math

from Search_Heuristics.Local.Neighbourhood.Vizinhanca import Vizinhanca
from Search_Heuristics.Solucao import Solucao


# Discente/s:

# Mudar nome da classe e do arquivo conforme a vizinhança implementada
class SuaVizinhanca(Vizinhanca):
    def __init__(self, distancias: tuple[tuple[int]]):
        super().__init__("suavizinhanca", distancias, 2)

    # Método que computa e retorna a qualidade da solução vizinha
    # Considera mudança na qualidade da solução atual a partir da mudança de posição nos elementos da solução vizinha
    # (Mais eficiente que computar a qualidade do zero)
    def computar_qualidade(self, solucao: Solucao, i: int, j: int) -> int:
        pass

    # Aplica mudança de elementos na solução atual, retornando solução vizinha
    @staticmethod
    def gerar_novo_ciclo(solucao: Solucao, i: int, j: int) -> list:
        pass

    # Retorna a melhor solução da vizinhança
    def melhor_vizinho(self, solucao: Solucao, tabu: set) -> Solucao:
        pass

    # Retorna o primeiro vizinho que seja melhor que a solução atual
    # Retorna a solução atual se nenhum vizinho for melhor
    def primeiro_vizinho_melhor(self, solucao: Solucao, tabu: set) -> Solucao:
        pass
