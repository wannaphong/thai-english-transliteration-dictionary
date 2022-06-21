thairath_str="""Album / อัลบั้ม
Alcohol / แอลกอฮอล์
Bacteria / แบคทีเรีย
Ball / บอล
Bar / บาร์
Cake / เค้ก
Capsule / แคปซูล
Design / ดีไซน์
Digital / ดิจิทัล
Electronics / อิเล็กทรอนิกส์
Farm / ฟาร์ม
Fax / แฟกซ์
Focus / โฟกัส
Game / เกม
Gas / แก๊ส
Gear / เกียร์
Heroin / เฮโรอีน
Highlight / ไฮไลต์
Ice Cream / ไอศกรีม
Internet / อินเทอร์เน็ต
Jacket / แจ็กเก็ต
Jeans / ยีนส์
Kilo / กิโล
Laser / เลเซอร์
Lens / เลนส์
Microphone / ไมโครโฟน
Motor / มอเตอร์
Note / โน้ต
Nylon / ไนลอน
Office/ ออฟฟิศ
Palm / ปาล์ม
Percent / เปอร์เซ็นต์
Plaster / ปลาสเตอร์
Queue / คิว
Quota/ โควตา
Radar / เรดาร์
Resort / รีสอร์ต
Series / ซีรีส์
Show / โชว์
Tape / เทป
Taxi / แท็กซี่
Unit / ยูนิต
Update / อัปเดต
Vaccine / วัคซีน
Version / เวอร์ชัน
Video / วิดีโอ
Vote / โหวต
Watt / วัตต์
Website / เว็บไซต์
X-ray / เอกซเรย์"""
thairath = []
for l in thairath_str.splitlines():
    #print(l)
    w,t = [i.strip() for i in l.strip().split('/')]
    thairath.append((t,w))