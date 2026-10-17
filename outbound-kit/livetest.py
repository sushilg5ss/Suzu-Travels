import sys, asyncio, json
from playwright.async_api import async_playwright
async def main(url,w,out):
    async with async_playwright() as p:
        b=await p.chromium.launch(); ctx=await b.new_context(viewport={'width':w,'height':900},user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36')
        pg=await ctx.new_page()
        await pg.goto(url, wait_until='load', timeout=120000); await pg.wait_for_timeout(2000)
        h=await pg.evaluate('document.body.scrollHeight')
        for y in range(0,h,600):
            await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(120)
        await pg.wait_for_timeout(1500)
        r={}
        r['title']=await pg.title()
        r['h1']=await pg.evaluate("document.querySelectorAll('h1').length")
        r['overflow']=await pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
        r['broken']=await pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src).slice(0,10)")
        r['robots']=await pg.evaluate("(document.querySelector('meta[name=robots]')||{}).content")
        if await pg.query_selector('.hx-styles'):
            await pg.click('label[for=hxs2]'); await pg.wait_for_timeout(300)
            r['tab2']=await pg.evaluate("getComputedStyle(document.querySelector('.hx-p2')).display+'/'+getComputedStyle(document.querySelector('.hx-p1')).display")
            await pg.evaluate("window.__o=null;window.open=function(u){window.__o=u;}")
            await pg.select_option('#hxPlan select[name=d]','Bhutan')
            await pg.click('#hxPlan button[type=submit]'); await pg.wait_for_timeout(300)
            r['wa']=await pg.evaluate("window.__o")
        await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(800)
        await pg.screenshot(path=out, full_page=True)
        print(json.dumps(r,indent=1)); await b.close()
asyncio.run(main(sys.argv[1],int(sys.argv[2]),sys.argv[3]))
