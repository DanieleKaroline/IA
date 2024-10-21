import math

from Local.Neighbourhood.Vizinhanca import Vizinhanca
from Solucao import Solucao


# Discente/s:

# Mudar nome da classe e do arquivo conforme a vizinhança implementada
class SuaVizinhanca(Vizinhanca):
    def __init__(self, distancias: tuple[tuple[int]]):
        super().__init__("node swap", distancias, 2)

    # Método que computa e retorna a qualidade da solução vizinha
    # Considera mudança na qualidade da solução atual a partir da mudança de posição nos elementos da solução vizinha
    # (Mais eficiente que computar a qualidade do zero)
    def computar_qualidade(self, solucao: Solucao, i: int, j: int) -> int:
        qualidade = solucao.qualidade
        elemento_i = solucao.ciclo[i]
        elemento_j = solucao.ciclo[j]
        elemento_pre_i = solucao.ciclo[i-1] if i > 0 else solucao.ciclo[-1]
        elemento_pos_i = solucao.ciclo[(i+1) % len(solucao.ciclo)]
        elemento_pre_j = solucao.ciclo[j-1] if j > 0 else solucao.ciclo[-1]
        elemento_pos_j = solucao.ciclo[(j+1) % len(solucao.ciclo)]

        qualidade += - self.distancias[elemento_i][elemento_pre_i] - self.distancias[elemento_i][elemento_pos_i]
        qualidade += - self.distancias[elemento_j][elemento_pre_j] - self.distancias[elemento_j][elemento_pos_j]
        qualidade += self.distancias[elemento_j][elemento_pre_i] + self.distancias[elemento_j][elemento_pos_i]
        qualidade += self.distancias[elemento_i][elemento_pre_j] + self.distancias[elemento_i][elemento_pos_j]

        return qualidade

    # Aplica mudança de elementos na solução atual, retornando solução vizinha
    @staticmethod
    def gerar_novo_ciclo(solucao: Solucao, i: int, j: int) -> list:
        novo_ciclo = solucao.ciclo.copy()
        novo_ciclo[i], novo_ciclo[j] = novo_ciclo[j], novo_ciclo[i]
        return novo_ciclo

    # Retorna a melhor solução da vizinhança
    def melhor_vizinho(self, solucao: Solucao, tabu: set) -> Solucao:
        melhor_qualidade = math.inf
        imelhor = -1
        jmelhor = -1
        for i in range(self.tamanho-1):
            if solucao.ciclo[i] not in tabu:
                # i < j para não testar a mesma troca 2opt
                for j in range(i+1, self.tamanho-1):
                    if solucao.ciclo[j] not in tabu:
                        qualidade = self.computar_qualidade(solucao, i, j)
                        if qualidade < melhor_qualidade:
                            melhor_qualidade = qualidade
                            imelhor = i
                            jmelhor = j
        return Solucao(melhor_qualidade, self.gerar_novo_ciclo(solucao, imelhor, jmelhor), solucao.ciclo[imelhor], solucao.ciclo[jmelhor])

    # Retorna o primeiro vizinho que seja melhor que a solução atual
    # Retorna a solução atual se nenhum vizinho for melhor
    def primeiro_vizinho_melhor(self, solucao: Solucao, tabu: set) -> Solucao:
        for i in range(self.tamanho - 1):
            if solucao.ciclo[i] not in tabu:
                for j in range(i + 1, self.tamanho):
                    if solucao.ciclo[j] not in tabu:
                        nova_solucao = Solucao(self.computar_qualidade(solucao, i, j), self.gerar_novo_ciclo(solucao, i, j), i, j)
                        if nova_solucao.qualidade < solucao.qualidade:
                            return nova_solucao
        return solucao
