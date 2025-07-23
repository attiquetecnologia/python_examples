sites = (
    'facebook.com'
    ,'instagram.com'
    ,'friv.com'
    ,'whatsapp.com'
    ,'chat.openai.com'
    ,'netflix.com'
    ,'clickjogos.com'
)

with open("arquivos/sites.txt", 'r') as f:
    for p in sites:
        f.write(f"127.0.0.1\t{p}")
        f.write(f"127.0.0.1\twww.{p}")
