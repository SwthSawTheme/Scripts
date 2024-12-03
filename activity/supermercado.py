def calcular_preco_final():
    # Solicita as informações do usuário
    valor_produto = float(input("Digite o valor do produto: R$ "))
    cliente_vip = input("O cliente é VIP? (sim/não): ").strip().lower()
    produto_promocao = input("O produto está em promoção? (sim/não): ").strip().lower()
    quantidade_produtos = int(input("Digite a quantidade de produtos no carrinho: "))
    
    # Inicializa o valor final com o valor original do produto
    valor_final = valor_produto
    
    # Aplica desconto de cliente VIP
    if cliente_vip == "sim":
        valor_final *= 0.90  # 10% de desconto
    
    # Aplica desconto de produto em promoção
    if produto_promocao == "sim":
        valor_final *= 0.95  # 5% de desconto
    
    # Aplica desconto por quantidade no carrinho
    if quantidade_produtos > 5:
        valor_final *= 0.98  # 2% de desconto
    
    # Exibe os resultados
    print(f"\nValor original do produto: R$ {valor_produto:.2f}")
    print(f"Valor final com descontos aplicados: R$ {valor_final:.2f}")

# Chama a função para execução
calcular_preco_final()
