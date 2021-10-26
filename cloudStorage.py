import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A7HoXtvysVJf2vQq0CYU9Z3wmkWdGWN3dvmvH8YbUyvgWN6Uxxjdu64rk44c5UzD5-UABANHLggFZQ0SFcPT_JS4AlkXpDtAKhg6J477Lc-XD6lHtE--GqVO-q6M0f9V56G6qMTSERg'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter full path to upload to dropbox: ')

    transferData.upload_file(file_from, file_to)
    print('File has been moved successfully')

main()