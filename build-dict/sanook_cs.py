# from https://www.sanook.com/campus/1390985/
sanook_str="""Acrylic = อะคริลิก
Action = แอ็กชัน
Album = อัลบั้ม
Alcohol = แอลกอฮอล์
Animation = แอนิเมชัน
Apartment = อะพาร์ตเมนต์
Apple = แอปเปิล
Application = แอปพลิเคชัน
Ballet = บัลเลต์
Bank = แบงก์
Battery = แบตเตอรี่
Block = บล็อก
Bowling = โบว์ลิง
Boxer = บ๊อกเซอร์
Brake = เบรก
Broccoli = บรอกโคลี
Browser = เบราว์เซอร์
Built-in = บิวท์อิน
Business = บิสเนส
Caffeine = คาเฟอีน
Cake = เค้ก
Capsule = แคปซูล
Card = การ์ด
Carrot = แคร์รอต
Center = เซนเตอร์
Ceramic = เซรามิก
Chalk = ชอล์ก
Channel = แชนเนล
Chat = แชต
Check = เช็ก
Chill = ชิล
Chocolate = ช็อกโกแลต
Classic = คลาสสิก
Clinic = คลินิก
Cocktail = ค็อกเทล
Comedy = คอมเมดี้
Comment = คอมเมนต์
Computer = คอมพิวเตอร์
Concept = คอนเซ็ปต์
Content = คอนเทนต์
Cookie = คุกกี้
Copy = ก๊อปปี้
Course = คอร์ส
Design = ดีไซน์
Detox = ดีท็อกซ์
Digital = ดิจิทัล
Double = ดับเบิล
Download = ดาวน์โหลด
Effect = เอฟเฟ็กต์
Electronics = อิเล็กทรอนิกส์
Email = อีเมล
Facebook    = เฟซบุ๊ก
Fashion = แฟชั่น
French fries = เฟรนช์ฟรายส์
Galaxy = กาแล็กซี
Gallery = แกลเลอรี
Game = เกม
Gas = แก๊ส
Gift = กิฟต์
Golf = กอล์ฟ
Graph = กราฟ
Graphic = กราฟิก
Guide = ไกด์
Hand made = แฮนด์เมด
Highlight = ไฮไลท์
Image = อิมเมจ
Internet = อินเทอร์เน็ต
Lift = ลิฟต์
Like = ไลก์
Line = ไลน์
Link = ลิงก์
Lipstick = ลิปสติก
Lock = ล็อก
Lotion = โลชัน
Lottery = ลอตเตอรี่
Moment = โมเมนต์
Necktie = เนกไท
Network = เน็ตเวิร์ก
Night club = ไนต์คลับ
Notebook = โน้ตบุ๊ก
Office = ออฟฟิศ
Operator = โอเปอเรเตอร์
Part time = พาร์ทไทม์
Percent = เปอร์เซ็นต์
Perfect = เพอร์เฟกต์
Postcard = โปสต์การ์ด
Power = พาวเวอร์
Profile = โพรไฟล์
Program = โปรแกรม
Project = โปรเจกต์
Quota = โควตา
Remote = รีโมท
Resort = รีสอร์ต
Save = เซฟ
Seafood = ซีฟู้ด
Sensor = เซนเซอร์
Series = ซีรีส์
Shirt = เชิ้ต
Shock = ช็อก
Shopping = ชอปปิง
Smart phone = สมาร์ทโฟน
Social media = โซเชียลมีเดีย
Software = ซอฟต์แวร์
Spaghetti  = สปาเกตตี
Spoil = สปอยล์
Staff = สตาฟ
Start = สตาร์ต
Steak = สเต๊ก
Strawberry = สตรอว์เบอร์รี
Style = สไตล์
Stylist = สไตลิสต์
Subscribe = ซับสไครบ์
Super = ซูเปอร์
Sweater = สเวตเตอร์
Taxi = แท็กซี่
Technology = เทคโนโลยี
Update = อัปเดต
Upload = อัปโหลด
Vaccine = วัคซีน
Version = เวอร์ชัน
Video = วิดีโอ
View = วิว
Vintage = วินเทจ
Wallpaper = วอลล์เปเปอร์
Web browser = เว็บเบราว์เซอร์
Work = เวิร์ก
Workshop = เวิร์กชอป
Yacht = ยอร์ช"""

sanook = []
for l in sanook_str.splitlines():
    w,t = l.strip().split(' = ')
    sanook.append((t,w))