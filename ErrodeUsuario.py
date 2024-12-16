 except ValueError:
        print("Erro: Por favor, insira um número válido para o tipo de usuário.")
    except UsuarioInvalidoError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
