# Explicação do Exercício:
# O objetivo do exercício é usar essa estrutura de pilha para verificar se a sequência de parênteses fornecida é bem-formada.

# Aqui está o que a função deve fazer:

# Passo 1: Percorrer cada caractere da sequência.
# Passo 2: Se encontrar um parêntese de abertura (, empurrá-lo para a pilha.
# Passo 3: Se encontrar um parêntese de fechamento ), verificar se há um parêntese de abertura correspondente na pilha:
# Se a pilha estiver vazia (não há um parêntese de abertura para combinar com este de fechamento), a sequência é malformada.
# Se houver um parêntese de abertura na pilha, removê-lo da pilha (isso significa que encontramos um parêntese
#  correspondente para o fechamento).
# Passo 4: Após percorrer toda a sequência, verificar se a pilha está vazia:
# Se estiver vazia, significa que todos os parênteses foram combinados corretamente e a sequência é bem-formada.
# Se não estiver vazia, significa que há parênteses de abertura sem o correspondente fechamento, então a sequência é malformada.
# Exemplo Prático:
# Para a sequência "(())", a pilha seria utilizada da seguinte forma:

# ( -> Empurrar para a pilha
# ( -> Empurrar para a pilha
# ) -> Verificar e remover da pilha
# ) -> Verificar e remover da pilha
# A pilha está vazia no final, então a sequência é bem-formada.
# Para a sequência "(()", o processo seria:

# ( -> Empurrar para a pilha
# ( -> Empurrar para a pilha
# ) -> Verificar e remover da pilha
# A pilha não está vazia no final (ainda há um (), então a sequência é malformada.
# Este exercício é uma prática comum para ajudar a entender tanto a aplicação da 
# estrutura de pilha quanto o conceito de sequências bem-formadas, que é relevante em diversas áreas,
#  como análise de expressões matemáticas e programação de linguagens.

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self,object):
        self.stack.append(object)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
    
    def getStack(self):
        return self.stack
    


def parenteses(list):
    pilha = Stack()

    for item in list:
        if item == "(":
            pilha.push(item)
        elif item == ")":
            if pilha.pop() is None:
                return False
    return len(pilha.getStack()) == 0

# Exemplos de uso:

print(parenteses("()"))      # Deve retornar True
print(parenteses("(())"))    # Deve retornar True
print(parenteses("(()"))     # Deve retornar False
print(parenteses(")("))      # Deve retornar False