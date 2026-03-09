def converter_temperatura():
    print("\n--- Conversor de Temperatura ---")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Celsius -> Kelvin")
    print("4. Kelvin -> Celsius")
    try:
        opcao = int(input("Escolha a opção: "))
        valor = float(input("Digite o valor: "))
    except ValueError:
        print("Entrada inválida. Use números.")
        return

    if opcao == 1:
        print(f"{valor} °C = {(valor * 9/5) + 32:.2f} °F")
    elif opcao == 2:
        print(f"{valor} °F = {((valor - 32) * 5/9):.2f} °C")
    elif opcao == 3:
        print(f"{valor} °C = {valor + 273.15:.2f} K")
    elif opcao == 4:
        print(f"{valor} K = {valor - 273.15:.2f} °C")
    else:
        print("Opção inválida.")

def converter_moeda():
    print("\n--- Conversor de Moeda ---")
    print("1. BRL -> USD")
    print("2. USD -> BRL")
    print("3. BRL -> EUR")
    print("4. EUR -> BRL")

    taxa_brl_usd = 0.20
    taxa_brl_eur = 0.18

    try:
        opcao = int(input("Escolha a opção: "))
        valor = float(input("Digite o valor: "))
    except ValueError:
        print("Entrada inválida. Use números.")
        return

    if opcao == 1:
        print(f"R$ {valor:.2f} = US$ {valor * taxa_brl_usd:.2f}")
    elif opcao == 2:
        print(f"US$ {valor:.2f} = R$ {valor / taxa_brl_usd:.2f}")
    elif opcao == 3:
        print(f"R$ {valor:.2f} = € {valor * taxa_brl_eur:.2f}")
    elif opcao == 4:
        print(f"€ {valor:.2f} = R$ {valor / taxa_brl_eur:.2f}")
    else:
        print("Opção inválida.")

def converter_distancia():
    print("\n--- Conversor de Distância ---")
    print("1. Km -> Milhas")
    print("2. Milhas -> Km")
    print("3. Metros -> Pés")
    print("4. Pés -> Metros")

    try:
        opcao = int(input("Escolha a opção: "))
        valor = float(input("Digite o valor: "))
    except ValueError:
        print("Entrada inválida. Use números.")
        return

    if opcao == 1:
        print(f"{valor} km = {valor * 0.621371:.4f} milhas")
    elif opcao == 2:
        print(f"{valor} milhas = {valor / 0.621371:.4f} km")
    elif opcao == 3:
        print(f"{valor} m = {valor * 3.28084:.4f} pés")
    elif opcao == 4:
        print(f"{valor} pés = {valor / 3.28084:.4f} m")
    else:
        print("Opção inválida.")

def main():
    while True:
        print("\n=== Conversor Universal ===")
        print("1. Temperatura")
        print("2. Moeda")
        print("3. Distância")
        print("0. Sair")

        try:
            escolha = int(input("Escolha a categoria: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if escolha == 1:
            converter_temperatura()
        elif escolha == 2:
            converter_moeda()
        elif escolha == 3:
            converter_distancia()
        elif escolha == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
