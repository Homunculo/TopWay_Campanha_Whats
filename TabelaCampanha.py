import gspread
import pandas as pd


class TabelaCampanha:
    def __init__(self, api_key, nome_arquivo='credentials.json'):
        self.worksheet = gspread.service_account(filename=nome_arquivo).open_by_key(key=api_key).sheet1
        valores_lista = self.worksheet.get_all_records()
        self.valores = pd.DataFrame(columns=valores_lista[0].keys(), data=valores_lista)
        self.linha_atual = None

    def get_proxima_mensagem(self):
        """"
            retorna uma struct com os dados da próxima pessoa para mandar mensagem
                caso exista: {"id": id, "nome":nome, "whatsapp_api", whatsapp_api}
                caso não exista: {}
        """

        if not self.linha_atual:
            iter_x = 1
            while self.valores.loc[iter_x]["tel1 - entrado contato"] != '':
                iter_x += 1
                self.linha_atual = iter_x

        return self.valores.loc[self.linha_atual, ['id', "nome", "whatsapp1"]]

    def set_proxima_mensagem(self, existe):
        """
            armazena se o número existe ou não. Também é armazenado a data que foi feito essa operação.
        """
        # +2 pois é a próxima linha e o método conta a primeira linha como sendo 1, ao contrário
        # da datatable que começa a contar do 0
        data_hoje = date.today().strftime("%m/%d/%Y")
        self.worksheet.update_cell(self.linha_atual + 2, 14, data_hoje)

        if existe:
            self.worksheet.update_cell(self.linha_atual + 2, 15, "sim")
        else:
            self.worksheet.update_cell(self.linha_atual + 2, 15, "não")
