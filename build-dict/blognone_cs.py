# from https://www.blognone.com/glossary
blognone_str="""Adobe - อโดบี
alpha - อัลฟ่า
Amazon - อเมซอน
Android - แอนดรอยด์
AMD - เอเอ็มดี
Apple - แอปเปิล
ASEAN - อาเซียน
Baidu - ไป่ตู้
bandwidth - แบนด์วิดท์
Battery - แบตเตอรี่
Bill Gates - บิล เกตส์
beta - เบต้า
binary - ไบนารี
block - บล็อค
blog - บล็อก
Bluetooth - บลูทูธ
Blu-ray - บลูเรย์
browser - เบราว์เซอร์
bug - บั๊ก
CD-ROM - ซีดีรอม
CD - ซีดี
censor - เซ็นเซอร์
Centrino - เซนทริโน
CEO - ซีอีโอ
CFO - ซีเอฟโอ
CIO - ซีไอโอ
CPU - ซีพียู
code - โค้ด
Creative Commons - ครีเอทีฟส์คอมมอนส์
Debian - เดเบียน
desktop - เดสก์ท็อป
digital - ดิจิทัล
dollar - ดอลลาร์
domain - โดเมน
download - ดาวน์โหลด
drive - ไดรฟ์
DVD - ดีวีดี
eBay - อีเบย์
email - อีเมล
Eric Schmidt - อีริค ชมิดต์
file - ไฟล์
Firefox - ไฟร์ฟ็อกซ์
firewall - ไฟร์วอลล์
font - ฟอนต์
Framework - เฟรมเวิร์ค
Games - เกม
Graphic - กราฟิก
hacker - แฮกเกอร์
harddisk - ฮาร์ดดิสก์
hardware - ฮาร์ดแวร์
HTC - เอชทีซี
IBM - ไอบีเอ็ม
Intel - อินเทล
iPad - ไอแพด
iPhone - ไอโฟน
iPod - ไอพ็อด
JavaScript - จาวาสคริปต์
kernel - เคอร์เนล
keyboard - คีย์บอร์ด
keyword - คีย์เวิร์ด
laptop - แล็ปท็อป
Lenovo - เลอโนโว
LG - แอลจี
link - ลิงก์
Linux - ลินุกซ์
Mac - แมค
mainboard - เมนบอร์ด
malware - มัลแวร์
Microsoft - ไมโครซอฟท์
MP3 - เอ็มพีสาม
Motorola - โมโตโรลา
monitor - มอนิเตอร์
mouse - เมาส์
Nintendo - นินเทนโด
Norway - นอร์เวย์
Novell - โนเวลล์
Obama - โอบามา
Office - ออฟฟิศ
Open Source - โอเพนซอร์ส
Opera - โอเปร่า
Oracle - ออราเคิล
Panasonic - พานาโซนิค
Pentium - เพนเทียม
Podcast - พ็อดคาสต์
Podcast - พ็อดแคสต์
print - พรินต์
process - โพรเซส
processor - โพรเซสเซอร์
Python - ไพธอน
Reuters - รอยเตอร์
Red Hat - เรดแฮท
Ruby - รูบี้
Samsung - ซัมซุง
Safari - ซาฟารี
script - สคริปต์
Seagate - ซีเกท
search engine - เสิร์ชเอ็นจิน
sensor - เซ็นเซอร์
server - เซิร์ฟเวอร์
smartphone - สมาร์ทโฟน
Solaris - โซลาริส
socket - ซ็อกเก็ต
Sony - โซนี่
Sony Ericsson - โซนี่อีริคสัน
source code - ซอร์สโค้ด
spam - สแปม
spyware - สปายแวร์
Steve Ballmer - สตีฟ บัลเมอร์
Steve Jobs - สตีฟ จ็อบส์
Sun - ซัน
tab - แท็บ
Ubuntu - อูบุนตู
update - อัพเดต
upgrade - อัพเกรด
USB - ยูเอสบี
video - วิดีโอ
VDO - วิดีโอ
vector - เวกเตอร์
version - เวอร์ชัน
Vietnam - เวียดนาม
web service - เว็บเซอร์วิส
Wiki - วิกิ
Wikipedia - วิกิพีเดีย
Windows - วินโดวส์
Windows XP - วินโดวส์เอ็กซ์พี
Windows Vista - วินโดวส์วิสตา
Vista - วิสตา
word processor - เวิร์ดโพรเซสเซอร์
Xbox - เอ็กซ์บ็อกซ์
Yahoo - ยาฮู
YouTube - ยูทูบ
Germany - เยอรมนี
Google Talk - กูเกิลทอล์ค"""

bn = []
for l in blognone_str.splitlines():
    w,t = l.strip().split(' - ')
    bn.append((t,w))