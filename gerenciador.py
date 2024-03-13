class Tarefa:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    
    def adicionar_tarefa(self, title, description, deadline):
        tarefa = Tarefa(title, description, deadline)
        self.tarefas.append(tarefa)
        print("A tarefa foi adicionada com sucesso.")

    def checar_tarefas(self):
        if len(self.tarefas) == 0:
            print("Não há tarefas cadastradas.")
        else:
            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f"\nTarefa {i}:")
                print(f"Título: {tarefa.title}")
                print(f"Descrição: {tarefa.description}")
                print(f"Prazo: {tarefa.deadline}")
                print(f"Status: {'Concluída' if tarefa.completed == True else "Pendente"}")

    def tarefa_concluida(self, numero_tarefa):
        if numero_tarefa <= len(self.tarefas):
            tarefa = self.tarefas[numero_tarefa - 1]
            tarefa.completed = True
            self.tarefas.remove(tarefa)
            print("Tarefa concluída")
        else:
            print("Tarefa não encontrada")
        


gerenciador_tarefas = GerenciadorTarefas()

while True:
    print("########## GERENCIADOR DE TAREFAS ##########      by Thomaz")
    print("1. Adicionar Tarefas")
    print("2. Visualizar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada")

    if escolha == "1":
        title = input("Digite o título da tarefa")
        description = input("Digite a descrição")
        deadline = input("Digite o prazo final da tarefa")
        gerenciador_tarefas.adicionar_tarefa(title, description, deadline)
    elif escolha == "2":
        gerenciador_tarefas.checar_tarefas()
    elif escolha == "3":
        numero_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída"))
        gerenciador_tarefas.tarefa_concluida(numero_tarefa)
    elif escolha == "4":
        break
    else:
        "Opção inválida. Por favor, tente novamente"