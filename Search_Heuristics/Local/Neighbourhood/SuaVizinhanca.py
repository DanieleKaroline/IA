import math
from Local.Neighbourhood.Vizinhanca import Vizinhanca
from Solucao import Solucao

class SuaVizinhanca(Vizinhanca):
    def __init__(self, distancias: tuple[tuple[int]]):
        super().__init__("node swap", distancias, 2)

    #Método que calcula o ganho da troca de nós
    def calcular_ganho_troca(self, elemento_pre_i, elemento_i, elemento_pos_i, 
                             elemento_pre_j, elemento_j, elemento_pos_j) -> int:
        #Calcula a soma das distâncias removidas e adicionadas
        dist_removidas = self.distancias[elemento_pre_i][elemento_i] + self.distancias[elemento_i][elemento_pos_i] + \
                         self.distancias[elemento_pre_j][elemento_j] + self.distancias[elemento_j][elemento_pos_j]
        dist_adicionadas = self.distancias[elemento_pre_i][elemento_j] + self.distancias[elemento_j][elemento_pos_i] + \
                           self.distancias[elemento_pre_j][elemento_i] + self.distancias[elemento_i][elemento_pos_j]

        #Retorna o ganho de qualidade
        return dist_removidas - dist_adicionadas

    #Método que aplica a troca de nós
    @staticmethod
    def aplicar_troca_nos(tour: list, i: int, j: int):
        # Troca os elementos na posição i e j
        tour[i], tour[j] = tour[j], tour[i]

    #Método que computa a qualidade da solução vizinha após a troca
    def computar_qualidade(self, solucao: Solucao, i: int, j: int) -> int:
        qualidade = solucao.qualidade
        elemento_pre_i, elemento_i, elemento_pos_i, elemento_pre_j, elemento_j, elemento_pos_j = solucao.retornar_elementos(i, j)

        #Calcula o ganho da troca de nós
        ganho = self.calcular_ganho_troca(elemento_pre_i, elemento_i, elemento_pos_i,
                                          elemento_pre_j, elemento_j, elemento_pos_j)
        return qualidade + ganho

    #Gera um novo ciclo após a troca de dois nós
    @staticmethod
    def gerar_novo_ciclo(solucao: Solucao, i: int, j: int) -> list:
        novo_ciclo = solucao.ciclo[:]
        novo_ciclo[i], novo_ciclo[j] = novo_ciclo[j], novo_ciclo[i]
        return novo_ciclo

    #Retorna a melhor solução da vizinhança
    def melhor_vizinho(self, solucao: Solucao, tabu: set) -> Solucao:
        melhor_qualidade = math.inf
        melhor_i = -1
        melhor_j = -1
        
        for i in range(len(solucao.ciclo) - 1):
            if solucao.ciclo[i] not in tabu:
                for j in range(i + 1, len(solucao.ciclo)):
                    if solucao.ciclo[j] not in tabu:
                        try:
                            qualidade = self.computar_qualidade(solucao, i, j)
                            if qualidade < melhor_qualidade:
                                melhor_qualidade = qualidade
                                melhor_i = i
                                melhor_j = j
                        except ValueError as e:
                            print(f"Erro ao computar qualidade: {e}")
        
        if melhor_i == -1 or melhor_j == -1:
            print("Nenhum vizinho melhor encontrado.")
            return solucao  #Retorna a solução original se nenhuma melhor for encontrada
        
        return Solucao(melhor_qualidade, self.gerar_novo_ciclo(solucao, melhor_i, melhor_j), solucao.ciclo[melhor_i], solucao.ciclo[melhor_j])

    #Retorna o primeiro vizinho que seja melhor que a solução atual
    def primeiro_vizinho_melhor(self, solucao: Solucao, tabu: set) -> Solucao:
        for i in range(len(solucao.ciclo) - 1):
            if solucao.ciclo[i] not in tabu:
                for j in range(i + 1, len(solucao.ciclo)):
                    if solucao.ciclo[j] not in tabu:
                        try:
                            qualidade = self.computar_qualidade(solucao, i, j)
                            if qualidade < solucao.qualidade:
                                return Solucao(qualidade, self.gerar_novo_ciclo(solucao, i, j), i, j)
                        except ValueError as e:
                            print(f"Erro ao computar qualidade: {e}")
        return solucao  #Retorna a solução original se nenhuma melhor for encontrada