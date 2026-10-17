import asyncio, json, random
from playwright.async_api import async_playwright
PAGES=['international-tour-packages','nepal-tour-packages','bhutan-tour-packages','sri-lanka-tour-packages','maldives-tour-packages','thailand-tour-packages','singapore-tour-packages','malaysia-tour-packages','vietnam-tour-packages','bali-tour-packages','india-tours','golden-triangle-tour','char-dham-yatra-for-nri']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        out={}
        for w in (1440,390):
            ctx=await b.new_context(viewport={'width':w,'height':900},user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36')
            for s in PAGES:
                pg=await ctx.new_page()
                try:
                    await pg.goto(f'https://suzutravels.com/{s}/?v={random.randint(1,10**9)}', wait_until='load', timeout=90000)
                    await pg.wait_for_timeout(1200)
                    h=await pg.evaluate('document.body.scrollHeight')
                    for y in range(0,h,900):
                        await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(60)
                    await pg.wait_for_timeout(1200)
                    r=await pg.evaluate('''()=>{const c=document.querySelector('.entry-content')||document.body;return {h1:document.querySelectorAll('h1').length,ov:document.documentElement.scrollWidth-document.documentElement.clientWidth,broken:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.slice(-50)),vids:c.querySelectorAll('video').length,green:(c.innerHTML.match(/suzu-intl\\/suzu-intl-/g)||[]).length,szs:!!c.querySelector('.szs'),robots:(document.querySelector('meta[name=robots]')||{}).content}}''')
                    if w==390 and s in ('nepal-tour-packages','india-tours'):
                        await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(500)
                        await pg.screenshot(path=f'preview/v_{s}_m.png')
                    if w==1440:
                        await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(500)
                        await pg.screenshot(path=f'preview/v_{s}.png')
                    out[f'{s}@{w}']=r
                except Exception as e:
                    out[f'{s}@{w}']=str(e)[:120]
                await pg.close()
        await b.close()
        for k,v in out.items(): print(k, v)
asyncio.run(main())
