import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.chnmuseum.cn/'
}

url = 'https://www.chnmuseum.cn/zl/wszl/'
all_data = []

r = requests.get(url, headers=headers, timeout=30)
print(f"页面状态: {r.status_code}")

soup = BeautifulSoup(r.text, 'html.parser')

items = soup.find_all('a', href=re.compile(r'/lszl/'))
added = 0
for a_tag in items:
    polluted_title = a_tag.get_text(strip=True)
    if len(polluted_title) < 10:
        continue
    
    detail_url = urljoin(url, a_tag['href'])
    
    # 提取展厅
    hall_match = re.search(r'([南北]\d+(?:、[南北]\d+)*展厅)', polluted_title)
    hall = hall_match.group(1) if hall_match else ''
    
    # 提取展期
    time_match = re.search(r'展览时间：([\d/-–—]+)', polluted_title)
    publish_time = time_match.group(1) if time_match else ''
    
    # 提取纯标题（移除展厅+时间部分）
    clean_title = re.sub(r'^.*展览时间：[\d/-–—]+', '', polluted_title).strip()
    
    all_data.append({
        "museum": "中国国家博物馆",
        "title": clean_title,
        "hall": hall,
        "publish_time": publish_time,
        "detail_url": detail_url,
        "column_id": "网上展览"
    })
    added += 1

with open('namuseum_online_exhibitions.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 清洗完成！共 {len(all_data)} 条干净数据")
print("title（纯标题）、hall（展厅）、publish_time（展期）已分离")
