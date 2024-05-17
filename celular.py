class Celular():
    bateria = 'Infinita'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'Cinza'
    modelo = 'Tijolão'

    def ligaçao(self):
        print('Ligando...')

    def mensagem(self):
        print('Enviando Mensagem...')

    def jogo_cobrinha(self):
        print('Ligando...')

print(Celular.bateria)
print(Celular.jogo_cobrinha())