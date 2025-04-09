usuarios = []
def soma(a,b):
    return a+b

def eh_par(n):
    if (n % 2 == 0):
        return True
    else:
        return False
    
def fatorial_numero(n):
    if n > 0:
        lista =[]
        fatorial = 1
        qtd = 1
        for i in range(n):
            lista.append(i)
        for i in lista:
            fatorial*= qtd
            qtd+=1
        return fatorial
    else:
        False
        
def cadastro_usuario(nome,email): 
    for usuario in usuarios: 
        if usuario["email"] == email:
            return "Email já existe"
    novo_usuario={
        "nome":nome,
        "email":email
    }
    usuarios.append(novo_usuario) 
    return "Sucesso"
        
print(cadastro_usuario("pedro", "pedro@gmail.com"))
        