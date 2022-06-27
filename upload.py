import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKXO7i8b_qBWrWZ-BrjvRhHpq-V4iYU-1JcCAoYd2bWt9VL-Sd6d7H28MZT97mXluRLFkcv9uD94klcQTYhpooXUj5KUchtGKsdHY_M0O_eTkRG7RbpZ8PDJ5r6hbsIYLhVR0L8'
    transferData = TransferData(access_token)

    file_from = input("Enter Source: ")
    file_to = input("Enter Destination: ")

    transferData.upload_file(file_from, file_to)

main()