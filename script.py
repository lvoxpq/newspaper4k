from newspaper import Article, configuration

with open('f.html', 'r') as f:
    x = f.read()
cfg = configuration.Configuration()
cfg.fetch_images = False

a = Article("", config=cfg)
a.html = x
a.parse()
print(a.download_state)
print(a.publish_date)
print(a.authors)
