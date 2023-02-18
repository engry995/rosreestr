import imaplib


class EmailHandler:

    def __init__(self):
        self.login = 'den.ari'
        self.password = 'akmola2004'
        self.host = 'imap.yandex.ru'
        self.port = 993
        self.directory = 'reestr'
        self.subj = 'Уведомление о завершении обработки запроса'
        self.client = None
        self.__uids = None
        self.links = None

    def get_links(self):
        self.connect()
        self.__get_mail_uid()
        self.__download_email()
        self.__parse_email()
        return self.links

    def connect(self):

        self.client = imaplib.IMAP4_SSL(host=self.host, port=self.port)
        status, result = self.client.login(self.login, self.password)
        if status != 'OK':
            print('Ошибка подключения к почтовому ящику', result)
        print(f'Подключились к {self.login}, server {self.host}:{self.port}')
        status, result = self.client.select(self.directory, readonly=True)
        if status != 'OK':
            print(f'Ошибка поиска папки {self.directory}', result)
        print(f'В папке {self.directory} найдено {result[0].decode("UTF-8")} писем')

    def disconnect(self):
        self.client.logout()

    def __get_mail_uid(self, subj=None):
        if not subj:
            subj = self.subj
        _, emails = self.client.uid('search', 'CHARSET', 'utf-8', f'SUBJECT "{subj}"'.encode('utf-8'))
        self.uids = emails[0].decode('utf-8').split()

    def __download_email(self):
        return []

    def __parse_email(self):
        return []










if __name__ == '__main__':
    mail = EmailHandler()
    mail.connect()
    print(mail.get_mail())
