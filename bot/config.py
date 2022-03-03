class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "Hai **{}.** __Kamu bisa menggunakan bot ini untuk mengupload file / video dari direct link atau telegram ke Google Drive milikmu sendiri.__\n__Untuk informasi lebih lanjut, kamu bisa ketik perintah /help.__"

    HELP_MSG = [
        ".",
        "**Pengenalan Gawr Gdrive Uploader**\n__Bot ini bisa mengupload file dari direct link atau telegram ke google drive milikmu. Kamu hanya perlu login, kemudian kirim file dari direct link atau dari telegram ke sini, dan bot ini akan menguploadnya ke google drivemu.\n\nBot ini punya banyak fitur lhoo... ! Pengen tau ? Kalau emang pengen tau, kamu bisa klik tanda panah di bawah. Klik dengan hati-hati ya :).",
        
        f"**Fitur Login dan Logout**\n__Pertama-tama kamu harus login akun google drivemu terlebih dahulu untuk menggunakan bot ini. Untuk loginnya kamu tinggal ketik perintah /{BotCommands.Authorize[0]} dan kamu akan menerima URL, setelah itu kunjungi URL tersebut dan kamu nanti akan mendapatkan kode, salin kode tersebut ke sini, selesai. Gunakan perintah /{BotCommands.Revoke[0]} untuk logout akun google drive milikmu.__",        

        f"**Fitur Download**\nFitur download bot ini ada 3. Untuk penjelasannya ada di bawah.\n\n__**1. Download File Dari Direct Link**\nKirimkan file dari direct link ke sini, kemudian bot ini akan mendownload dan menguploadnya ke akun google drive milikmu. kamu bisa mengganti nama filemu sebelum diupload. Caranya kirimkan URL dan nama baru dari file yang ingin diganti namanya, keduanya dipisah dengan tanda ' | '.__\n\n__Contoh:__\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```. \n\nBtw perlu diingat bahwa bot ini supportnya direct link, jadi jangan mengirim link macam zippyshare, mega, solidfiles, dkk ke sini. Gunakan @transload untuk mengubah mereka menjadi direct link, kemudian kirim direct linknya ke bot ini. Saya merekomendasikan http://aws.rapidleech.gq/ untuk mengubah linkmu menjadi direct link. \n\n**2. Download File Telegram**\n__Untuk mengupload file dari telegram ke akun google drivemu, caranya cukup mudah. Teruskan file tersebut ke sini, dan bot ini akan menguploadnya. Note: Kamu bisa spam file telegram sekaligus lho, tapi mungkin ada beberapa file yg gagal. Misalnya kamu mengirim 10 file sekaligus, mungkin 8 file yg berhasil dan 2 lainnya gagal. Kamu bisa mengirim ulang file yg gagal tersebut, dan aku akan menguploadnya.__\n\n**3. YouTube-DL Support**\n__Download file melalui youtube-dl.\nGunakan perintah /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)__",
                
        f"**Fitur Memilih Folder Upload**\n__Kamu pengen upload file ke dalam drive atau team drive milikmu ? Gunakan perintah /{BotCommands.SetFolder[0]} (URL FOLDER) untuk mengatur tempat uploadmu. Semua file akan diupload ke dalam folder yang kamu pilih.__\n\n**Fitur Hapus file gdrive**\n__Gunakan perintah /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file.\nKamu juga dapat mengosongkan sampahmu dengan menggunakan perintah /{BotCommands.EmptyTrash[0]}\nNote: File akan dihapus secara permanen. Proses ini tidak bisa dibatalkan.\n\n**Fitur Salin File Gdrive**\n__Yap, mengkloning  atau menyalin file google drive. Gunakan perintah /{BotCommands.Clone[0]} (File id / Folder id or URL) untuk menyalin file google drive orang ke google drive milikmu. Tolong jangan menyalin file/folder google drive dengan jumlah yang besar. Itu mungkin akan menyebabkan filemu rusak atau membuat bot hang.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Owner : @rahmanaja009**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__Batasan harian pengguna terlampau, coba lagi 24 jam mendatang__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder Tidak Ditemukan.**\n__File id - {} Tidak Ditemukan. Untuk memastikannya\'s ada dan dapat diakses dengan logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nPastikan URL Google Drivenya sudah dalam format yang benar."
    
    COPIED_SUCCESSFULLY = "✅ **Salin Berhasil.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Kamu belum login.**\n__Kirim perintah /{BotCommands.Authorize[0]} untuk login.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Mengupload File...**\n**Nama:** ```{}```\n**Ukuran:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Upload Berhasil.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Download Gagal**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Sedang Mendownload File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Kamu Sudah Login.**\n__Gunakan /revoke untuk logout akunmu yang sekarang.__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Gunakan perintah /{BotCommands.Authorize[0]}.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Login Akun Berhasil.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__Kode yang kamu kirim sudah invalid atau sudah tidak bisa digunakan. gunakan kode yang baru dengan mengunjungi Authorization URL__'
    
    AUTH_TEXT = "⛓️ **Untuk login akunmu, kamu bisa kunjungi [URL]({}) dan kirim kode tokennya ke sini.**\n__Caranya kunjungi URL > Berikan izin > kamu akan mendapatkan kode tokennya > salin kode tersebut > kirim ke sini__"
    
    DOWNLOAD_TG_FILE = "📥 **Sedang Mendownload File...**\n**Nama:** ```{}```\n**Ukuran:** ```{}```\n**Jenis:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Memilih folder tempat upload sukses.**\n__Custom folder id milikmu- {}\nGunakan perintah__ ```/{} clear``` __untuk menghapusnya.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Id Folder Berhasil Dihapus.**\n__Gunakan perintah__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __untuk mengaturnya ulang__.'
    
    CURRENT_PARENT = "🆔 **Id Foldermu sekarang - {}**\n__Gunakan perintah__ ```/{} (Folder link)``` __untuk mengubahnya.__"
    
    REVOKED = f"🔓 **Berhasil  logout.**\n__Gunakan perintah /{BotCommands.Authorize[0]} untuk login kembali.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__Link yang kamu kirim bukan dari folder.__"
    
    CLONING = "🗂️ **Kloning Ke Google Drive...**\n__Link G-Drive - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Tolong berikan URL Google Drive yang valid.**"
    
    INSUFFICIENT_PERMISSONS = "❗ **Kamu tidak memiliki izin untuk file ini.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **Berhasil Menghapus File.**\n__Sekarang filemu sudah dihapus !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Tolong coba lagi nanti.__"
    
    EMPTY_TRASH = "🗑️🚮**Mengosongkan Sampah Berhasil !**"
    
    PROVIDE_YTDL_LINK = "❗**Tolong berikan link yang didukung YouTube-DL yang valid.**"
