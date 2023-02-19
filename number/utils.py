import imaplib, email


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
        self.links = []

    def get_links(self):
        self.connect()
        self.__get_mail_uid()
        for uid in self.__uids[:10]:
            mail = self.__download_email(uid)
            link = self.__parse_email(mail)
            if link:
                self.links.append(link)
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
        self.__uids = emails[0].decode('utf-8').split()
        print(f'Получено  {len(self.__uids)} uid')

    def __download_email(self, uid):
        res, mess = self.client.uid('fetch', uid, '(RFC822)')
        print(res, 'download', uid)
        if res == 'OK':
            mess = email.message_from_bytes(mess[0][1])
            return mess

    def __parse_email(self, mess):
        text = ''
        for part in mess.walk():
            if part.get_content_type() == 'text/html':
                text = part.get_payload(decode=True).decode()
        start = text.find('https://lk.rosreestr.ru')
        end = text.find('">', start)
        link = text[start:end]
        return link



if __name__ == '__main__':
    reestr = EmailHandler()
    print(reestr.get_links())
